import allure

from pages.mainpage import MainPage


class TestMainPage:
    @allure.story('Check title presence')
    def test_check_title(self, driver):
        mainpage = MainPage(driver)
        assert mainpage.is_block_title_present(), 'Title is not present on the mainpage.'
