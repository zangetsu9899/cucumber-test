import requests
from config import SESSION, APP_URL
import pytest


def test_health():
    response = SESSION.get(f'{APP_URL}/health')
    assert response.ok
