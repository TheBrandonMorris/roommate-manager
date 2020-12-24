import subprocess
from pathlib import Path
from typing import Iterable

import pytest
import yaml

from env import compose_file_path


def assert_file_exists(f: Path) -> None:
    try:
        assert f.is_file()
    except AssertionError:
        pytest.fail(f'"{f.name}" not found in "{f.parent.absolute()}"', pytrace=False)


def assert_in(item, collection: Iterable) -> None:
    if item not in collection:
        pytest.fail(f"{item} not found in {collection}", pytrace=False)


def get_compose_file_contents() -> dict:
    return yaml.safe_load(compose_file_path.read_text())


def assert_command_runs_and_exits_ok(cmd: list[str], fail_msg="", timeout=10) -> None:
    try:
        subprocess.check_call(cmd, timeout=timeout)
    except subprocess.SubprocessError:
        pytest.fail(fail_msg, pytrace=False)


def stop_web_service() -> None:
    cmd = ["docker-compose", "stop", "web"]
    subprocess.check_call(cmd)
    return


def start_web_service() -> None:
    cmd = ["docker-compose", "start", "web"]
    subprocess.check_call(cmd)
    return
