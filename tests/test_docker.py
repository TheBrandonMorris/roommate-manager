import pytest

from tests._utils import assert_command_runs_and_exits_ok


def test_local_docker_server_is_up():
    cmd = ["docker", "info"]
    assert_command_runs_and_exits_ok(cmd, "check that Docker is running")
