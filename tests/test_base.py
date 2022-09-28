import time
import allure

from FW.application_manager import ApplicationManager


class TestBase:

    APP = ApplicationManager()

    def setup_method(self):
        self.APP.main_page_ya.open_main_page('https://ya.ru/')

    def teardown_method(self):
        self.APP.main_page_ya.allure_screenshot()

    def setup_class(self):
        print('setup class')

    def teardown_class(self):
        self.APP.stop_driver()
