import allure
from selenium.webdriver.common.by import By

from FW.any_page import AnyPage


class Locator:
    search_input = (By.XPATH, '//*[@name="text"]')
    locator_frame = (By.XPATH, '//form[@action="https://yandex.ru/search/"]/iframe')
    btn_submit = (By.XPATH, '//*[@type="submit"][contains(@class, "dzen-search")]')
    text_weather = (By.XPATH, '//div[@class="informers3"]/a[1]')


class MainPageYandex(AnyPage):

    @allure.step('Ввод текста в строку поиска')
    def send_keys_in_search_input(self, text):
        frame = self.find_element(Locator.locator_frame)
        self.get_driver().switch_to.frame(frame)
        self.send_keys(Locator.search_input, text)
        self.get_driver().switch_to.default_content()
        return self


    @allure.step('Нажать кнопку Найти')
    def click_btn_submit(self):
        self.click(Locator.btn_submit)
        return self.manager.search

    @allure.step('Получить текст погоды')
    def get_text_weather(self):
        return self.get_text(Locator.text_weather)
