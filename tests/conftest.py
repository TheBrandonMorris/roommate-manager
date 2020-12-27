import time

from pytest import fixture

from tests._utils import get_compose_file_contents, start_web_service, stop_web_service


@fixture
def web_service_up(scope="module") -> None:
    stop_web_service()
    time.sleep(1)
    start_web_service()
    time.sleep(1)
    yield
    stop_web_service()


@fixture
def compose_file_services(compose_file_contents) -> dict:
    return compose_file_contents["services"]


@fixture
def compose_file_contents() -> dict:
    return get_compose_file_contents()
