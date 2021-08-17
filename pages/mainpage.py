from selenium.webdriver.common.by import By

from core.settings import BASE_FE_URL
from pages.base_page import BasePage


class MainPageLocators:
    BLOCK_TITLE = By.XPATH, '(//h1//span[text()="Unlocking the Microbiome"])[1]'


class MainPage(BasePage):
    def is_block_title_present(self):
        self.open_url(BASE_FE_URL)
        is_title = self.is_element_present(*MainPageLocators.BLOCK_TITLE)
        return is_title
