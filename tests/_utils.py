import subprocess
from pathlib import Path
from typing import Iterable

import pytest
import yaml

from roommate_manager.env import compose_file_path


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


def assert_docker_command_runs_and_exits_ok(cmd: list[str], *, timeout=10.0):
    proc = subprocess.run(cmd, timeout=timeout)
    if proc.returncode is not 0:
        err_out = f"{proc.stderr.decode()}"
        pytest.fail(err_out, pytrace=False)


def stop_web_service() -> None:
    cmd = ["docker-compose", "stop", "web"]
    subprocess.check_call(cmd)
    return


def start_web_service() -> None:
    subprocess.call(["docker-compose", "up", "-d", "web"], timeout=120)


def list_running_containers() -> list[str]:
    cmd = ["docker", "ps"]
    return list(
        map(
            lambda x: x.split()[-1],
            subprocess.check_output(cmd).decode("UTF-8").splitlines(),
        )
    )[1:]
