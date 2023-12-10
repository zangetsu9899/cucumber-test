import requests
from lib.utils import build_request_header
from lib.comments import Comments
from config import APP_URL, LOG


def test_get_all_comments(login_as_admin):
    # Get comments
    LOG.info('test_get_all_comments()')
    response = Comments().get_all_comments(APP_URL, login_as_admin)
    LOG.debug(response.json())
    assert response.ok
