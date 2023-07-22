import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Protocol

from .checker.checker import OptimizationLevel
from .test import Test


@dataclass
class Result:
    test: Test
    opt_level: OptimizationLevel
    passed: bool


class IResultsHandler(Protocol):
    def handle(self, results: Iterable[Result]) -> None:
        ...


class CSVResultsHandler:
    def __init__(self, out_file_path: Path):
        self.out_file_path = out_file_path

    def handle(self, results: Iterable[Result]) -> None:
        with open(self.out_file_path, "w") as f:
            writer = csv.writer(f)

            # header
            writer.writerow(("instruction", "test", "-O", "result"))

            # content
            for res in sorted(
                results, key=lambda r: (r.test.instruction, r.test.name, r.opt_level.name)
            ):
                writer.writerow(
                    (
                        res.test.instruction,
                        res.test.name,
                        res.opt_level.name,
                        "passed" if res.passed else "failed",
                    )
                )
