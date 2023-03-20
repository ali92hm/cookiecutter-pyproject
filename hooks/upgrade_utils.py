from typing import Tuple
from pathlib import Path

LATEST_VERSION_MAJOR = 0
LATEST_VERSION_MINOR = 1
LATEST_VERSION_PATCH = 0


def get_latest_version() -> str:
    return "f{LATEST_VERSION_MAJOR}.{LATEST_VERSION_MINOR}.{LATEST_VERSION_PATCH}"


def parse_version(version: str) -> Tuple(int, int, int):
    return map(int, version.split("."))


def is_upgradable(current_version: str) -> bool:
    return True


def post_gen_upgrade(cookiecutterrc, project_dir: Path):
    cookiecutterrc["cookiecutter"]["_template_version"] = "0.1.0"

    return cookiecutterrc
