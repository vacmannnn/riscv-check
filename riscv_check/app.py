from logging import Logger

from .checker.checker import IChecker, OptimizationLevel
from .tests_parser import ITestsParser


class Application:
    def __init__(self, logger: Logger, parser: ITestsParser, checker: IChecker):
        self.logger = logger
        self.parser = parser
        self.checker = checker

    def run(self) -> None:
        tests = self.parser.parse_tests()

        all_cnt = passed_cnt = 0
        for test in tests:
            for opt_level in OptimizationLevel:
                passed = self.checker.check(test, opt_level)

                self.logger.info(
                    f"Test '{test.name}' for {test.instruction}, {opt_level.name} has "
                    + ("PASSED" if passed else "FAILED")
                )

                all_cnt += 1
                passed_cnt += 1 if passed else 0

        self.logger.info(f"{passed_cnt}/{all_cnt} passed")
