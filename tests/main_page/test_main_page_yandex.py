import allure
import pytest
from selenium.webdriver import Keys

from tests.test_base import TestBase


@allure.epic('Web')
@allure.feature('MainPage')
@allure.story('Yandex')
class TestMainPageYandex(TestBase):

    def setup_method(self):
        self.APP.main_page_yandex.open_main_page('https://yandex.ru/')

    data_2 = [
        ('Test'),
        ('qwerty'),
        ('Погода'),
    ]

    @allure.title('Тест получения погоды')
    @pytest.mark.WebTest
    @pytest.mark.YandexRu
    @pytest.mark.parametrize("search_input", data_2)
    def test_parametrize(self, search_input):
        self.APP.main_page_yandex.send_keys_in_search_input(search_input)
        self.APP.main_page_yandex.send_keys_in_search_input(Keys.ENTER)

