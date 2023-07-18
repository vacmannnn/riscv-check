from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Protocol


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
        raise NotImplementedError
