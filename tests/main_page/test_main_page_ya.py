import allure
import pytest

from tests.test_base import TestBase


@allure.epic('Web')
@allure.feature('MainPage')
@allure.story('Ya')
class TestMainPageYa(TestBase):

    @allure.title('Проверка кнопки Найти (Test #1)')
    @pytest.mark.WebTest
    @pytest.mark.YaRu
    def test_temp_1(self):
        main_page = self.APP.main_page
        main_page.send_keys_in_search_input('Test 12312312')
        main_page.click_btn_submit()

        search = self.APP.search
        search.get_text_title()

    @allure.title('Проверка кнопки Найти (Test #2)')
    @pytest.mark.WebTest
    @pytest.mark.YaRu
    def test_temp_2(self):
        self.APP.main_page.send_keys_in_search_input('qwerty')
        self.APP.main_page.click_btn_submit()

    @allure.title('Проверка кнопки Найти (Test #3)')
    @pytest.mark.WebTest
    @pytest.mark.YaRu
    def test_temp_3(self):
        main_page = self.APP.main_page
        main_page.send_keys_in_search_input('Погода').click_btn_submit()

    @allure.title('Тест получения погоды')
    @pytest.mark.WebTest
    @pytest.mark.YaRu
    def test_get_weather(self):
        test_main_page = self.APP.main_page
        text_weather = test_main_page.get_text_weather().replace('°', '')

        assert int(text_weather) > 0
