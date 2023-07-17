from dataclasses import dataclass
from pathlib import Path


@dataclass
class AppConfig:
    tests_dir_path: Path

    compiler_path: Path
    march: str


def get_config() -> AppConfig:
    return AppConfig(
        tests_dir_path=Path(),
        compiler_path=Path(),
        march="abc",
    )
