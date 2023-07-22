from logging import Logger

from .checker.checker import IChecker, OptimizationLevel
from .results_handler import IResultsHandler, Result
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

    def run(self) -> None:
        tests = self.parser.parse_tests()
        results: list[Result] = []

        all_cnt = passed_cnt = 0
        for test in tests:
            for opt_level in OptimizationLevel:
                passed = self.checker.check(test, opt_level)

                self.logger.info(
                    f"Test '{test.name}' for {test.instruction}, {opt_level.name} has "
                    + ("PASSED" if passed else "FAILED")
                )

                results.append(Result(test=test, opt_level=opt_level, passed=passed))

                all_cnt += 1
                passed_cnt += 1 if passed else 0

        self.logger.info(f"{passed_cnt}/{all_cnt} passed")

        self.results_handler.handle(results=results)
