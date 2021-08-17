from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator) -> list:
        return self.driver.find_elements(*locator)

    def is_element_present(self, *locator):
        try:
            self.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def wait_for_element_appears(self, *locator, delay=30):
        try:
            element = WebDriverWait(self.driver, delay).until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise NoSuchElementException(f'Element does not appear after {delay} seconds.')
        return element

    def wait_for_element_and_click(self, *locator, delay=30):
        element = self.wait_for_element_appears(*locator, delay=delay)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click();', element)

    def clear_field_and_fill(self, text, *locator):
        element = self.wait_for_element_appears(*locator)
        self.wait_for_element_and_click(*locator)
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(text)
