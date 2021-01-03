import requests
import time


def test_web_service_home_returns_status_code_200(web_service_up):
    time.sleep(10)
    assert requests.get("http://127.0.0.1:5000/").status_code == 200
