import subprocess
from dataclasses import dataclass
from os import path
from pathlib import Path
from shutil import rmtree
from tempfile import mkdtemp
from typing import Iterable, Protocol


class CompileError(Exception):
    pass


@dataclass
class Compiler:
    compiler_path: Path
    compiler_args: Iterable[str]


class IBuilder(Protocol):
    def build_to_asm(self, code: str, additional_args: Iterable[str]) -> str:
        ...


class Builder:
    def __init__(self, compiler: Compiler) -> None:
        self.compiler = compiler

    def build_to_asm(self, code: str, additional_args: Iterable[str]) -> str:
        temp_dir = mkdtemp()

        Path(temp_dir, "code.c").write_text(code)

        try:
            result = subprocess.run(
                [self.compiler.compiler_path]
                + list(self.compiler.compiler_args)
                + list(additional_args)
                + [
                    "-S",
                    "-o",
                    path.join(temp_dir, "asm_code.s"),
                    path.join(temp_dir, "code.c"),
                ],
                capture_output=True,
                text=True,
            )

            if result.returncode != 0:
                raise CompileError(result.stderr)

            return Path(temp_dir, "asm_code.s").read_text()

        finally:
            rmtree(temp_dir)
