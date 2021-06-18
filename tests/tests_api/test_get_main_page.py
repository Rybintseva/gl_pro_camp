import allure

from api_client.methods_api import ApiClient
from core.settings import BASE_FE_URL, OK


class TestGetMainPage:
    @allure.story('Get Mainpage')
    def test_get_mainpage(self):
        api_page = ApiClient()
        response = api_page.get(BASE_FE_URL)
        assert response == OK, f'Actual status code: {response}\nExpected: {OK}.'
