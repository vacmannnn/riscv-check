from os.path import basename
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
    logger = get_logger("main")
    compiler_error_logger = get_logger(
        name="compile_errors", console_log=False, logfile_path=Path("compiler_errors.log")
    )

    Application(
        logger=logger,
        compiler_error_logger=compiler_error_logger,
        parser=TestsParser(tests_dir=config.tests_dir_path),
        checker=Checker(
            builder=Builder(
                compiler=Compiler(
                    compiler_path=config.compiler_path,
                    compiler_args=list(config.compiler_args)
                    + ["-Werror=implicit-function-declaration"],
                )
            )
        ),
        results_handler=CSVResultsHandler(
            logger=logger,
            out_file_path=Path(f"{basename(config.compiler_path)}.csv"),
            merge_tests=config.csv_merge_tests_by_opt,
        ),
        optimization_levels=config.optimization_levels,
    ).run()
