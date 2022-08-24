from selenium.webdriver.common.by import By

from FW.any_page import AnyPage


class Search(AnyPage):

    def get_text_title(self):
        return self.get_driver().find_element(By.XPATH, '//li[@data-fast="1"]//h2[contains(@class, "OrganicTitle-LinkText")]').text

    def get_text_title_2(self):
        return self.get_driver().find_element(By.XPATH, '//li[@data-fast="1"]//h2[contains(@class, "OrganicTitle-LinkText")]').text

    def get_text_title_3(self):
        return self.get_driver().find_element(By.XPATH, '//li[@data-fast="1"]//h2[contains(@class, "OrganicTitle-LinkText")]').text
