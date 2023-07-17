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
        raise NotImplementedError
