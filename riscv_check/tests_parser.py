from pathlib import Path
from typing import Protocol

from .test import Test


class ITestsParser(Protocol):
    def parse_tests(self) -> list[Test]:
        ...


class TestsParser:
    def __init__(self, tests_dir: Path):
        self.tests_dir = tests_dir

    def parse_tests(self) -> list[Test]:
        raise NotImplementedError
