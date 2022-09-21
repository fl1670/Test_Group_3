import allure
from selenium.webdriver.common.by import By

from FW.any_page import AnyPage


class Locator:
    search_input = (By.XPATH, '//*[@id="text"]')
    btn_submit = (By.XPATH, '//*[@type="submit"]')
    text_weather = (By.XPATH, '//div[@class="informers3"]/a[1]')


class MainPage(AnyPage):

    @allure.step('Ввод текста в строку поиска')
    def send_keys_in_search_input(self, text):
        self.send_keys(Locator.search_input, text)
        return self

    @allure.step('Нажать кнопку Найти')
    def click_btn_submit(self):
        self.click(Locator.btn_submit)
        return self.manager.search

    @allure.step('Получить текст погоды')
    def get_text_weather(self):
        return self.get_text(Locator.text_weather)
