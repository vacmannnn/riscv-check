from os import scandir
from os.path import basename
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
        result: list[Test] = []

        for dirpath in [
            f.path
            for f in scandir(self.tests_dir)
            if f.is_dir() and not basename(f.path).startswith("_")
        ]:
            # dirpath contains instruction name

            for filepath in [f.path for f in scandir(dirpath) if f.is_file()]:
                # filename contains test name

                if filepath.endswith(".c") and not basename(filepath).startswith("_"):
                    with open(filepath, "r") as f:
                        result.append(
                            Test(
                                name=basename(filepath).removesuffix(
                                    ".c"
                                ),  # filename w/o .c is test name
                                instruction=basename(dirpath),  # dir name is insn name
                                code=f.read(),
                            )
                        )

        return result
