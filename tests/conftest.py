import json
import os

import allure
import pytest
import yaml

from api_client.methods_api import ApiClient
from core.config import Configuration as config, HOME_PATH
from core.logger import LOGGER
from core.settings import HEADERS, USERNAME, PASSWORD
from core.webdriver_factory import get_driver
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.login_page import LoginPage, LoginPageLocators


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Please choose a browser as a required parameter: --browser')


@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption('--browser')
    if not browser:
        browser = config.get_config('BROWSER')
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


@pytest.fixture(scope='class')
def account_page(driver):
    account_page = AccountPage(driver)

    def _login():
        login_page = LoginPage(driver)
        with allure.step('Login step'):
            LOGGER.info(f'Login step with {USERNAME} and {PASSWORD}')
        login_page.login(USERNAME, PASSWORD)
    _login()

    yield account_page

    def _logout():
        logout_page = BasePage(driver)
        with allure.step('Logout step'):
            LOGGER.info('Logout')
        logout_page.wait_for_element_and_click(*LoginPageLocators.LOGOUT_BTN)
    _logout()
