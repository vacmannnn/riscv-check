from .checker.builder import Builder, Compiler
from .checker.checker import Checker, IChecker
from .config import get_config
from .tests_parser import ITestsParser, TestsParser


class Application:
    def __init__(self) -> None:
        config = get_config()

        self.parser: ITestsParser = TestsParser(tests_dir=config.tests_dir_path)
        self.checker: IChecker = Checker(
            builder=Builder(
                compiler=Compiler(compiler_path=config.compiler_path, compiler_args="")
            )
        )

    def run(self) -> None:
        pass
