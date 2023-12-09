import requests
import pytest


@pytest.fixture(scope="session")
def login_as_admin():
    # Auth
    payload = {"username": "admin", "password": "admin"}
    response = requests.post('http://localhost:8080/auth/login', data=payload)
    assert response.ok

    # Extract token
    token = response.json()["access_token"]
    yield token
