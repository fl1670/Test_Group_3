from selenium.webdriver.common.by import By

from FW.any_page import AnyPage


class MainPage(AnyPage):

    def send_keys_in_search_input(self, text):
        self.get_driver().find_element(By.XPATH, '//*[@id="text"]').send_keys(text)

    def click_btn_submit(self):
        self.get_driver().find_element(By.XPATH, '//*[@type="submit"]').click()
