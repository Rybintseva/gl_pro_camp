from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


def get_driver(requested_driver: str):
    browsers_dict = {
        'chrome': __get_chrome,
        'remote_chrome': __get_remote_chrome,
        'firefox': __get_firefox,
        'edge': __get_edge,
        'opera': __get_opera
    }
    try:
        return browsers_dict[requested_driver]()
    except ValueError:
        raise Exception('Browser is not supported.')


def __get_chrome():
    options = webdriver.ChromeOptions()
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return chrome_driver


def __get_remote_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    chrome_driver = webdriver.Remote("http://selenium:4444/wd/hub", options.to_capabilities())
    return chrome_driver


def __get_firefox():
    options = webdriver.FirefoxOptions()
    firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                       options=options)
    return firefox_driver


def __get_edge():
    capabilities = webdriver.DesiredCapabilities().EDGE
    edge_driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(),
                                 capabilities=capabilities)
    return edge_driver


def __get_opera():
    opera_driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    return opera_driver
