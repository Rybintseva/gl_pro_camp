from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

from core.config import BROWSER


def get_driver():
    """Get webdriver according to the BROWSER"""
    driver = None
    if BROWSER == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif BROWSER == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif BROWSER == 'edge':
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    elif BROWSER == 'opera':
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    return driver
