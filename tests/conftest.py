import pytest

from core.config import Configuration as config
from core.webdriver_factory import get_driver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Please choose a browser as a required parameter: --browser')


@pytest.fixture(scope='session')
def browser(request):
    browser = config.get_config('browser')
    if not browser:
        browser = request.config.getoption('--browser')
    return browser


@pytest.fixture()
def driver(browser):
    driver = get_driver(browser)
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
