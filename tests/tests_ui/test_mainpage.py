import allure
import pytest

from pages.mainpage import MainPage


class TestMainPage:
    @pytest.mark.ui
    @pytest.mark.mainpage
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story('Check title presence')
    def test_check_title(self, driver):
        mainpage = MainPage(driver)
        with allure.step('Check title presence'):
            assert mainpage.is_block_title_present(), 'Title is not present on the mainpage.'
