import logging
from pathlib import Path
from typing import Optional


def get_logger(
    name: str, console_log: bool = True, logfile_path: Optional[Path] = None
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s :: %(message)s", "%y-%m-%d %H:%M:%S"
    )

    if console_log:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if logfile_path is not None:
        file_handler = logging.FileHandler(logfile_path, "w")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
