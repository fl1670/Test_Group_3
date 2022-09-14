import allure
from selenium.webdriver.common.by import By

from FW.any_page import AnyPage


class Search(AnyPage):

    @allure.step('Получить текст get_text_title')
    def get_text_title(self):
        return self.get_driver().find_element(By.XPATH, '//li[@data-fast="1"]//h2[contains(@class, "OrganicTitle-LinkText")]').text

    @allure.step('Получить текст get_text_title_123')
    def get_text_title_123(self):
        return self.get_driver().find_element(By.XPATH, '//li[@data-fast="1"]//h2[contains(@class, "OrganicTitle-LinkText")]').text

    @allure.step('Получить текст get_text_title_222')
    def get_text_title_222(self):
        return self.get_driver().find_element(By.XPATH, '//li[@data-fast="1"]//h2[contains(@class, "OrganicTitle-LinkText")]').text
