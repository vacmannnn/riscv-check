import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class AppConfig:
    tests_dir_path: Path

    compiler_path: Path
    compiler_args: Iterable[str]

    csv_merge_tests_by_opt: bool


def get_config() -> AppConfig:
    with open("config.json", "r") as f:
        json_conf = json.load(f)

        return AppConfig(
            tests_dir_path=Path(json_conf["tests_dir_path"]),
            compiler_path=Path(json_conf["compiler_path"]),
            compiler_args=json_conf["compiler_args"],
            csv_merge_tests_by_opt=json_conf["csv_merge_tests_by_opt"],
        )
