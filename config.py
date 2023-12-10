import requests
import logging

SESSION = requests.session()
APP_URL = 'http://localhost:8080'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'

LOG = logging.getLogger()


class HideSensitiveData(logging.Filter):
    def filter(self, record):
        record.msg = str(record.msg).replace(ADMIN_PASSWORD, "*******")
        return True


LOG.addFilter(HideSensitiveData())
