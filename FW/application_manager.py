from FW.main_page import MainPage
from FW.search.search import Search
from FW.web_driver import WebDriver


class ApplicationManager:

    driver = None

    def stop_driver(self):
        self.web_driver.driver_exit(self.driver)
        self.driver = None

    def __init__(self):
        self.web_driver = WebDriver()
        self.main_page = MainPage(self)
        self.search = Search(self)
