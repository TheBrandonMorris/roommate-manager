from const import WEB_SERVICE_NAME
from env import working_dir_path, compose_file_path
from tests._utils import assert_file_exists, assert_in


def test_working_dir_is_project_root_containing_setup_file():
    assert_file_exists(working_dir_path / "setup.py")


def test_docker_compose_file_exists_in_working_dir():
    assert_file_exists(compose_file_path)


def test_compose_file_contains_web_service(compose_file_services):
    assert_in(WEB_SERVICE_NAME, compose_file_services.keys())

