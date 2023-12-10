import requests
from lib.utils import build_request_header
from config import SESSION


class Comments:

    def __init__(self):
        self.comments = '/comments'

    def get_all_comments(self, app_url, access_token):
        request_header = build_request_header(access_token)
        response = SESSION.get(f'{app_url}{self.comments}/', headers=request_header)
        return response

