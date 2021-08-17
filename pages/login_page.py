from selenium.webdriver.common.by import By

from core.settings import LOGIN_PAGE_URL
from pages.base_page import BasePage


class LoginPageLocators:
    HOMEPAGE_LINK = By.XPATH, '//a[@href="https://cosmosid.com"]'
    TITLE = By.XPATH, '//h1[text()="Sign in"]'
    EMAIL_LABEL = By.XPATH, '//label[@for="email"]'
    EMAIL_FIELD = By.XPATH, '//input[@id="email"]'
    PASSWORD_LABEL = By.XPATH, '//label[@for="password"]'
    PASSWORD_FIELD = By.XPATH, '//input[@id="password"]'
    SIGN_IN_BTN_DISABLED = By.XPATH, '//button[@id="signInButton" and @disabled]'
    FORGOT_PASSWORD_LINK = By.XPATH, '//a[@href="/forgot_password"]'
    REGISTER_LINK = By.XPATH, '//a[@href="/register"]'
    CHAT_WIDGET = By.XPATH, '//div[@id="hubspot-messages-iframe-container"]'
    SIGN_IN_BTN_ACTIVE = By.XPATH, '//button[@id="signInButton" and not(@disabled)]'
    LOGOUT_BTN = By.XPATH, '//button[@id="topbar-logout-button"]'
    CLOSE_NEW_FEATURES_POPUP = By.XPATH, '//span[text()="Do not show again"]'
    ERROR_MESSAGE = By.XPATH, '(//span[@id="message-id"])[1]'


class LoginPage(BasePage):
    def get_login_page_missed_elements(self):
        self.open_url(LOGIN_PAGE_URL)
        elements = {
            'homepage_link': self.is_element_present(*LoginPageLocators.HOMEPAGE_LINK),
            'title': self.is_element_present(*LoginPageLocators.TITLE),
            'email_label': self.is_element_present(*LoginPageLocators.EMAIL_LABEL),
            'email_field': self.is_element_present(*LoginPageLocators.EMAIL_FIELD),
            'password_label': self.is_element_present(*LoginPageLocators.PASSWORD_LABEL),
            'password_field': self.is_element_present(*LoginPageLocators.PASSWORD_FIELD),
            'sign_in_btn_disabled': self.is_element_present(*LoginPageLocators.SIGN_IN_BTN_DISABLED),
            'forgot_password_link': self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_LINK),
            'register_link': self.is_element_present(*LoginPageLocators.REGISTER_LINK),
            'chat_widget': self.is_element_present(*LoginPageLocators.CHAT_WIDGET)
        }
        missed_elements = [k for k, v in elements.items() if not v]
        return missed_elements

    def fill_email_and_password_fields(self, username, password):
        if not self.is_element_present(*LoginPageLocators.TITLE):
            self.open_url(LOGIN_PAGE_URL)
        try:
            self.clear_field_and_fill(username, *LoginPageLocators.EMAIL_FIELD)
        except Exception:
            self.wait_for_element_and_click(*LoginPageLocators.CLOSE_NEW_FEATURES_POPUP)
        self.clear_field_and_fill(username, *LoginPageLocators.EMAIL_FIELD)
        self.clear_field_and_fill(password, *LoginPageLocators.PASSWORD_FIELD)

    def login(self, username, password):
        self.fill_email_and_password_fields(username, password)
        self.wait_for_element_and_click(*LoginPageLocators.SIGN_IN_BTN_ACTIVE)

    def is_sign_in_button_active(self):
        return self.is_element_present(*LoginPageLocators.SIGN_IN_BTN_ACTIVE)

    def is_user_logged_in(self):
        return self.is_element_present(*LoginPageLocators.LOGOUT_BTN)

    def is_error_message(self):
        return self.is_element_present(*LoginPageLocators.ERROR_MESSAGE)
