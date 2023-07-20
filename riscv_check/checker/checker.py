from dataclasses import dataclass
from enum import Enum
from typing import Protocol

from ..test import Test
from .builder import IBuilder


@dataclass
class CheckResult:
    test: Test


class OptimizationLevel(Enum):
    O0, O1, O2, O3 = range(4)


class IChecker(Protocol):
    def check(self, test: Test, optimization_level: OptimizationLevel) -> CheckResult:
        ...


class Checker:
    def __init__(self, builder: IBuilder) -> None:
        self.builder = builder

    def check(self, test: Test, optimization_level: OptimizationLevel) -> CheckResult:
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

        self.builder.build_to_asm(test.code, opt_arg)

        raise NotImplementedError
