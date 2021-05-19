import pytest

from core.webdriver_factory import get_driver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default=None,
                     help='Please choose a browser as a required parameter: --browser')


@pytest.fixture()
def driver():
    driver = get_driver()
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
