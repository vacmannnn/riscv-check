from dataclasses import dataclass
from enum import Enum
from typing import Protocol

from ..test import Test
from .builder import IBuilder


class OptimizationLevel(Enum):
    O0, O1, O2, O3 = range(4)


class IChecker(Protocol):
    def check(self, test: Test, optimization_level: OptimizationLevel) -> bool:
        ...


class Checker:
    def __init__(self, builder: IBuilder) -> None:
        self.builder = builder

    def check(self, test: Test, optimization_level: OptimizationLevel) -> bool:
        opt_arg = ""
        match (optimization_level):
            case OptimizationLevel.O0:
                opt_arg = "-O0"
            case OptimizationLevel.O1:
                opt_arg = "-O1"
            case OptimizationLevel.O2:
                opt_arg = "-O2"
            case OptimizationLevel.O3:
                opt_arg = "-O3"

        asm_code = self.builder.build_to_asm(test.code, opt_arg)
        return any(word == test.instruction for word in asm_code.split())
