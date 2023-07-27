import asyncio
from logging import Logger
from typing import Iterable, Optional

from riscv_check.checker.builder import CompileError

from .checker.checker import IChecker, OptimizationLevel
from .results_handler import IResultsHandler, Result
from .test import Test
from .tests_parser import ITestsParser


class Application:
    def __init__(
        self,
        logger: Logger,
        compiler_error_logger: Logger,
        parser: ITestsParser,
        checker: IChecker,
        results_handler: IResultsHandler,
        optimization_levels: Iterable[OptimizationLevel],
    ):
        self.logger = logger
        self.compiler_error_logger = compiler_error_logger
        self.parser = parser
        self.checker = checker
        self.results_handler = results_handler
        self.optimization_levels = optimization_levels

    async def __run_test(self, test: Test, opt_level: OptimizationLevel) -> Optional[Result]:
        try:
            passed = await self.checker.check(test, opt_level)
        except CompileError as e:
            self.logger.warning(
                f"Failed to compile test '{test.name}' "
                f"for {test.instruction}, {opt_level.name}"
            )
            self.compiler_error_logger.warning(
                f"'{test.name}' for {test.instruction}, {opt_level.name}:\n{e}"
            )
            return None

        self.logger.info(
            f"Test '{test.name}' for {test.instruction}, {opt_level.name} has "
            + ("PASSED" if passed else "FAILED")
        )

        return Result(test=test, opt_level=opt_level, passed=passed)

    async def __run_tests(self, tests: Iterable[Test]) -> list[Result]:
        results: list[Optional[Result]] = await asyncio.gather(
            *(
                self.__run_test(test, opt_level)
                for test in tests
                for opt_level in self.optimization_levels
            )
        )
        return [r for r in results if r is not None]

    def run(self) -> None:
        tests = self.parser.parse_tests()
        results = asyncio.run(self.__run_tests(tests))

        self.logger.info(f"{sum(r.passed for r in results)}/{len(results)} passed")

        self.results_handler.handle(results=results)
