import requests
import pytest
from config import SESSION, APP_URL, ADMIN_USERNAME, ADMIN_PASSWORD, LOG


@pytest.fixture(scope="session")
def login_as_admin():
    # Auth
    LOG.info('login_as_admin()')
    payload = {"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD}
    LOG.debug(f'Login payload: {payload}')
    response = SESSION.post(f'{APP_URL}/auth/login', data=payload)
    assert response.ok

    # Extract token
    token = response.json()["access_token"]
    yield token
