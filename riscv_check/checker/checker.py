from enum import Enum
from typing import Protocol

from ..test import Test
from .builder import IBuilder


class OptimizationLevel(Enum):
    O0, O1, O2, O3 = range(4)


class IChecker(Protocol):
    async def check(self, test: Test, optimization_level: OptimizationLevel) -> bool:
        ...


class Checker:
    def __init__(self, builder: IBuilder) -> None:
        self.builder = builder

    async def check(self, test: Test, optimization_level: OptimizationLevel) -> bool:
        asm_code = await self.builder.build_to_asm(test.code, [f"-{optimization_level.name}"])

        # find instuction in asm code
        return any(
            # handle the case when the C function is named as instruction
            word == test.instruction and prev_word != ".globl"
            for prev_word, word in zip(asm_code.split(), asm_code.split()[1:])
        )
