import asyncio
from logging import Logger
from typing import Iterable

from .checker.checker import IChecker, OptimizationLevel
from .results_handler import IResultsHandler, Result
from .test import Test
from .tests_parser import ITestsParser


class Application:
    def __init__(
        self,
        logger: Logger,
        parser: ITestsParser,
        checker: IChecker,
        results_handler: IResultsHandler,
    ):
        self.logger = logger
        self.parser = parser
        self.checker = checker
        self.results_handler = results_handler

    async def __run_test(self, test: Test, opt_level: OptimizationLevel) -> Result:
        passed = await self.checker.check(test, opt_level)

        self.logger.info(
            f"Test '{test.name}' for {test.instruction}, {opt_level.name} has "
            + ("PASSED" if passed else "FAILED")
        )

        return Result(test=test, opt_level=opt_level, passed=passed)

    async def __run_tests(self, tests: Iterable[Test]) -> list[Result]:
        return await asyncio.gather(
            *(
                self.__run_test(test, opt_level)
                for test in tests
                for opt_level in OptimizationLevel
            )
        )

    def run(self) -> None:
        tests = self.parser.parse_tests()
        results = asyncio.run(self.__run_tests(tests))

        self.results_handler.handle(results=results)
