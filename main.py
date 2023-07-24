from pathlib import Path

from riscv_check.app import Application
from riscv_check.checker.builder import Builder, Compiler
from riscv_check.checker.checker import Checker
from riscv_check.config import get_config
from riscv_check.logger import get_logger
from riscv_check.results_handler import CSVResultsHandler
from riscv_check.tests_parser import TestsParser

if __name__ == "__main__":
    config = get_config()

    Application(
        logger=get_logger(),
        parser=TestsParser(tests_dir=config.tests_dir_path),
        checker=Checker(
            builder=Builder(
                compiler=Compiler(
                    compiler_path=config.compiler_path,
                    compiler_args=[f"-march={config.march}"] if config.march else [],
                )
            )
        ),
        results_handler=CSVResultsHandler(out_file_path=Path("results.csv"), merge_tests=True),
    ).run()
