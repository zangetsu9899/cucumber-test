import requests
from lib.utils import build_request_header


def test_get_all_comments(login_as_admin):
    # Get comments
    request_header = build_request_header(login_as_admin)
    response = requests.get('http://localhost:8080/comments/', headers=request_header)
    assert response.ok
