import time
from FW.application_manager import ApplicationManager


class TestBase:

    APP = ApplicationManager()

    def setup_method(self):
        self.APP.main_page.open_main_page('https://ya.ru/')

    def teardown_method(self):
        time.sleep(2)

    def setup_class(self):
        pass

    def teardown_class(self):
        self.APP.stop_driver()
