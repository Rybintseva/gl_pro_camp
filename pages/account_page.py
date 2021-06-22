from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPageLocators:
    ACCOUNT_INFO_LINK = By.XPATH, '//a[@id="topbar-user-info-link"]'
    PAYMENTS_LINK = By.XPATH, '//a[@id="topbar-user-payment-link"]'
    PROFILE_TITLE = By.XPATH, '//h4[text()="My Profile"]'
    PROCEED_TO_CHECKOUT_BTN = By.XPATH, '//a[@class="buy-button"]'


class AccountPage(BasePage):
    def open_profile(self):
        self.wait_for_element_and_click(*AccountPageLocators.ACCOUNT_INFO_LINK)

    def is_profile_open(self):
        return self.is_element_present(*AccountPageLocators.PROFILE_TITLE)

    def open_payments_page(self):
        self.wait_for_element_and_click(*AccountPageLocators.PAYMENTS_LINK)

    def is_payments_page_open(self):
        return self.is_element_present(*AccountPageLocators.PROCEED_TO_CHECKOUT_BTN)
