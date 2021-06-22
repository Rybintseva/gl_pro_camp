import allure
import pytest

from core.settings import USERNAME, PASSWORD
from pages.login_page import LoginPage


class TestLoginPage:

    @pytest.mark.ui
    @pytest.mark.login
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story('Validate Login page elements')
    def test_login_page_elements(self, driver):
        login_page = LoginPage(driver)
        with allure.step('Validate Login page elements displaying'):
            missed_elements = login_page.get_login_page_missed_elements()
            assert len(missed_elements) == 0, f'Missed elements on the Login page are: {missed_elements}'

    @pytest.mark.ui
    @pytest.mark.login
    @pytest.mark.regression
    @pytest.mark.negative
    @allure.story('Login with invalid username')
    def test_login_invalid_username(self, driver):
        login_page = LoginPage(driver)
        with allure.step('Login to the site with invalid username'):
            login_page.login(f'not{USERNAME}', PASSWORD)
            assert login_page.is_error_message(), 'The error message is not shown.'

    @pytest.mark.ui
    @pytest.mark.login
    @pytest.mark.regression
    @pytest.mark.negative
    @allure.story('Login with invalid password')
    def test_login_invalid_password(self, driver):
        login_page = LoginPage(driver)
        with allure.step('Login to the site with invalid password'):
            login_page.login(USERNAME, f'not{PASSWORD}')
            assert login_page.is_error_message(), 'The error message is not shown.'

    @pytest.mark.ui
    @pytest.mark.login
    @pytest.mark.regression
    @pytest.mark.negative
    @allure.story('Login with invalid username and password')
    def test_login_invalid_username_and_password(self, driver):
        login_page = LoginPage(driver)
        with allure.step('Login to the site with invalid username and password'):
            login_page.login(f'not{USERNAME}', f'not{PASSWORD}')
            assert login_page.is_error_message(), 'The error message is not shown.'

    @pytest.mark.ui
    @pytest.mark.login
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story('Sign In button becomes active')
    def test_login_sign_in_btn_active(self, driver):
        login_page = LoginPage(driver)
        with allure.step('Sign In button becomes active after filling out username and password'):
            login_page.fill_email_and_password_fields(USERNAME, PASSWORD)
            assert login_page.is_sign_in_button_active(), 'Sign In button is not active.'

    @pytest.mark.ui
    @pytest.mark.login
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story('Successful login')
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        with allure.step('Login to the site with valid credentials'):
            login_page.login(USERNAME, PASSWORD)
            assert login_page.is_user_logged_in(), 'Login failed.'
