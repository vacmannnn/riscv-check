import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .checker.checker import OptimizationLevel


@dataclass
class AppConfig:
    tests_dir_path: Path

    compiler_path: Path
    compiler_args: Iterable[str]

    csv_merge_tests_by_opt: bool
    optimization_levels: Iterable[OptimizationLevel]


def get_config() -> AppConfig:
    with open("config.json", "r") as f:
        json_conf = json.load(f)
        opt_lvls_map = {
            "O0": OptimizationLevel.O0,
            "O1": OptimizationLevel.O1,
            "O2": OptimizationLevel.O2,
            "O3": OptimizationLevel.O3,
        }
        user_opt_lvls = json_conf["optimization_levels"]

        return AppConfig(
            tests_dir_path=Path(json_conf["tests_dir_path"]),
            compiler_path=Path(json_conf["compiler_path"]),
            compiler_args=json_conf["compiler_args"],
            csv_merge_tests_by_opt=json_conf["csv_merge_tests_by_opt"],
            optimization_levels=[
                opt_lvls_map[lvl] for lvl in user_opt_lvls if user_opt_lvls[lvl]
            ],
        )
