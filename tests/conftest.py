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
    location = 'v1/login'
    result = api.request('POST', location, HEADERS).json()['token']
    return result


@pytest.fixture(scope='function')
def test_reports_dir(request):
    test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    reports_dir = os.path.join(HOME_PATH, 'reports', test_name)
    os.makedirs(reports_dir)
    return reports_dir


@pytest.fixture(scope='class')
def driver(browser, request):
    driver = get_driver(browser)
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)

    failed_tests_count = request.session.testsfailed

    yield driver

    if request.session.testsfailed > failed_tests_count:
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        screenshot_file = os.path.join(test_reports_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)
        browser_logfile = os.path.join(test_reports_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)

    driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    def _login():
        login_page = LoginPage(driver)
        with allure.step('Login step'):
            LOGGER.info(f'Login step with {USERNAME} and {PASSWORD}')
        login_page.login(USERNAME, PASSWORD)
    return _login


@pytest.fixture(scope='function')
def logout(driver):
    def _logout():
        logout_page = BasePage(driver)
        with allure.step('Logout step'):
            LOGGER.info('Logout')
        logout_page.wait_for_element_and_click(*LoginPageLocators.LOGOUT_BTN)
    return _logout
