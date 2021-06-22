import allure
import pytest

from pages.account_page import AccountPage


class TestAccount:
    @pytest.mark.ui
    @pytest.mark.account
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story('Open profile page')
    def test_open_profile_page(self, driver, login):
        login()
        account_page = AccountPage(driver)
        with allure.step('Open profile page'):
            account_page.open_profile()
            assert account_page.is_profile_open(), 'Profile page is not open.'

    @pytest.mark.ui
    @pytest.mark.account
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story('Open payments page')
    def test_open_payments_page(self, driver, logout):
        account_page = AccountPage(driver)
        with allure.step('Open payments page'):
            account_page.open_payments_page()
            assert account_page.is_payments_page_open(), 'Payments page is not open.'
            logout()
