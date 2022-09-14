import allure
from selenium.webdriver.common.by import By

from FW.any_page import AnyPage


class MainPage(AnyPage):

    @allure.step('Ввод текста в строку поиска')
    def send_keys_in_search_input(self, text):
        self.get_driver().find_element(By.XPATH, '//*[@id="text"]').send_keys(text)

    @allure.step('Нажать кнопку Найти')
    def click_btn_submit(self):
        self.get_driver().find_element(By.XPATH, '//*[@type="submit"]').click()

    @allure.step('Получить текст погоды')
    def get_text_weather(self):
        return self.get_driver().find_element(By.XPATH, '//div[@class="informers3"]/a[1]').text

