import allure

from api_client.methods_api import ApiClient
from core.config import Configuration


class TestGetMainPage:
    @allure.story('Get Mainpage')
    def test_get_mainpage(self):
        api_page = ApiClient()
        response = str(api_page.get(Configuration.BASE_URL))
        assert '200' in response, f'Actual status code: {response}\nExpected: 200.'
