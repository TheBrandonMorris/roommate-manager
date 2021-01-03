import subprocess

import pytest

from tests._utils import (
    assert_docker_command_runs_and_exits_ok,
    list_running_containers,
)


def test_local_docker_server_is_up():
    cmd = ["docker", "info"]
    assert_docker_command_runs_and_exits_ok(cmd)


def test_web_service_runs(web_service_up):
    if "roommate-manager_web_1" not in list_running_containers():
        cmd = ["docker-compose", "logs", "--tail=1"]
        out = subprocess.run(cmd, capture_output=True).stdout
        pytest.fail(out.decode("utf8"), pytrace=False)
