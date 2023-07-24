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
    def __init__(self, out_file_path: Path, merge_tests: bool):
        self.out_file_path = out_file_path
        self.merge_tests = merge_tests

    @dataclass
    class MergedResult:
        test: Test
        opt_levels: list[OptimizationLevel]
        passed: bool

    def __merge_tests(self, results: list[Result]) -> list[MergedResult]:
        """Takes results sorted by instruction and name"""

        merged_results: list[CSVResultsHandler.MergedResult] = []
        base_index = 0

        while base_index < len(results):
            passed_opt_level_list: list[OptimizationLevel] = []
            not_passed_opt_level_list: list[OptimizationLevel] = []

            add_index = 0
            while base_index + add_index < len(results):
                if results[base_index].test == results[base_index + add_index].test:
                    if results[base_index + add_index].passed:
                        passed_opt_level_list.append(results[base_index + add_index].opt_level)
                    else:
                        not_passed_opt_level_list.append(
                            results[base_index + add_index].opt_level
                        )
                else:
                    break

                add_index += 1

            if not_passed_opt_level_list:
                merged_results.append(
                    self.MergedResult(
                        results[base_index].test, not_passed_opt_level_list, False
                    )
                )

            if passed_opt_level_list:
                merged_results.append(
                    self.MergedResult(results[base_index].test, passed_opt_level_list, True)
                )

            base_index += add_index

        return merged_results

    def handle(self, results: Iterable[Result]) -> None:
        results = sorted(
            results, key=lambda r: (r.test.instruction, r.test.name, r.opt_level.name)
        )

        with open(self.out_file_path, "w") as f:
            writer = csv.writer(f)

            writer.writerow(("instruction", "test", "-O", "result"))

            if self.merge_tests:
                [
                    writer.writerow(
                        (
                            r.test.instruction,
                            r.test.name,
                            "".join([lvl.name.removeprefix("O") for lvl in r.opt_levels]),
                            "passed" if r.passed else "failed",
                        ),
                    )
                    for r in self.__merge_tests(results)
                ]

            else:
                [
                    writer.writerow(
                        (
                            r.test.instruction,
                            r.test.name,
                            r.opt_level.name.removeprefix("O"),
                            "passed" if r.passed else "failed",
                        ),
                    )
                    for r in results
                ]
