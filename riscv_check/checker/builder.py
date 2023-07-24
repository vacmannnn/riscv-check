import asyncio
from dataclasses import dataclass
from os import path
from pathlib import Path
from typing import Iterable, Protocol

import aiofiles


class CompileError(Exception):
    pass


@dataclass
class Compiler:
    compiler_path: Path
    compiler_args: Iterable[str]


class IBuilder(Protocol):
    async def build_to_asm(self, code: str, additional_args: Iterable[str]) -> str:
        ...


class Builder:
    def __init__(self, compiler: Compiler) -> None:
        self.compiler = compiler

    async def build_to_asm(self, code: str, additional_args: Iterable[str]) -> str:
        async with aiofiles.tempfile.TemporaryDirectory() as temp_dir:
            async with aiofiles.open(path.join(temp_dir, "code.c"), "w") as f:
                await f.write(code)

            proc = await asyncio.create_subprocess_exec(
                self.compiler.compiler_path,
                *list(self.compiler.compiler_args)
                + list(additional_args)
                + [
                    "-S",
                    "-o",
                    path.join(temp_dir, "asm_code.s"),
                    path.join(temp_dir, "code.c"),
                ],
                stdin=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            _, stderr = await proc.communicate()

            if proc.returncode != 0:
                raise CompileError(stderr.decode())

            async with aiofiles.open(path.join(temp_dir, "asm_code.s"), "r") as f:
                return await f.read()
