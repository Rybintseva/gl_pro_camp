from requests import Session

from core.logger import LOGGER
from core.settings import OK, LOGIN_API_URL, HEADERS


class ApiClient:
    def __init__(self):
        self.session = Session()

    @staticmethod
    def log_pre(method, url, headers, data, expected_status):
        LOGGER.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
                    f'Expected status: {expected_status}\n\n')

    @staticmethod
    def log_post(response):
        log_str = f'Got response:\n' \
                  f'RESPONSE STATUS: {response.status_code}'
        LOGGER.info(f'{log_str}\n'
                    f'RESPONSE CONTENT: {response.text}\n\n')

    def request(self, method, url, headers=None, data=None, expected_status=200):
        self.log_pre(method, url, headers, data, expected_status)
        response = self.session.request(method, url, headers=headers, data=data)
        self.log_post(response)
        assert response.status_code == expected_status, \
            f'Got {response.status_code} {response.reason} for URL "{url}"!\n' \
            f'Expected status_code: {expected_status}.'
        return response

    def post_login(self, headers, expected_status):
        result = self.request('POST', LOGIN_API_URL, headers, expected_status=expected_status)
        return result

    def get_files_number(self, url, token, expected_status=OK):
        result = self.request('GET', url, headers={"x-token": token}, expected_status=expected_status).json()
        if expected_status == OK:
            return result['name'], result['total']
        else:
            return result['message']

    def get_statuses(self, url, token, artifact):
        result = self.request('GET', url, headers={"x-token": token}).json()
        statuses = [status['status'] for status in result[artifact]]
        return statuses

    def get_token(self):
        token = self.request('POST', LOGIN_API_URL, HEADERS).json()['token']
        return token
