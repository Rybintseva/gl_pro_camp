import json
import os

import pytest
import yaml

from api_client.methods_api import ApiClient
from core.config import Configuration as config, HOME_PATH
from core.webdriver_factory import get_driver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Please choose a browser as a required parameter: --browser')


@pytest.fixture(scope='session')
def browser(request):
    browser = config.get_config('BROWSER')
    if not browser:
        browser = request.config.getoption('--browser')
    return browser


@pytest.fixture(scope='session')
def config_data():
    with open(os.path.join(HOME_PATH, 'core', 'config.yaml'), encoding='utf-8') as yaml_file:
        data = yaml.load(yaml_file)
    return data


@pytest.fixture(scope='session')
def user_data():
    with open(os.path.join(HOME_PATH, 'data', 'user_data.json'), encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@pytest.fixture(scope='session')
def token():
    api = ApiClient()
    token = api.get_token()
    return token


@pytest.fixture()
def driver(browser):
    driver = get_driver(browser)
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
