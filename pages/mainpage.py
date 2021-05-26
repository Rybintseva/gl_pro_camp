from selenium.webdriver.common.by import By

from core.config import Configuration
from pages.base_page import BasePage


class MainPageLocators:
    BLOCK_TITLE = By.XPATH, '//h1[text()="Need Metagenomics Analysis?"]'


class MainPage(BasePage):
    def is_block_title_present(self):
        self.open_url(Configuration.BASE_URL)
        is_title = self.is_element_present(*MainPageLocators.BLOCK_TITLE)
        return is_title
