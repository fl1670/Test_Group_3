import allure
import pytest

from tests.test_base import TestBase


@allure.epic('Web')
@allure.feature('MainPage')
@allure.story('Yandex')
class TestMainPageYandex(TestBase):

    def setup_method(self):
        self.APP.main_page.open_main_page('https://yandex.ru/')

    @allure.title('Проверка кнопки Найти (Test #1)')
    @pytest.mark.WebTest
    @pytest.mark.YandexRu
    def test_temp_1(self):
        self.APP.main_page.send_keys_in_search_input('Test')
        self.APP.main_page.click_btn_submit()

    @allure.title('Проверка кнопки Найти (Test #2)')
    @pytest.mark.WebTest
    @pytest.mark.YandexRu
    def test_temp_2(self):
        self.APP.main_page.send_keys_in_search_input('qwerty')
        self.APP.main_page.click_btn_submit()

    @allure.title('Тест получения погоды')
    @pytest.mark.WebTest
    @pytest.mark.YandexRu
    def test_temp_3(self):
        self.APP.main_page.send_keys_in_search_input('Погода')
        self.APP.main_page.click_btn_submit()
