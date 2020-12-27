import requests


def test_web_service_home_returns_status_code_200(web_service_up):
    assert requests.get("http://localhost:5000/").status_code == 200
