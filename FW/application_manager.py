from FW.API.users.users import Users
from FW.main_page_ya import MainPageYa
from FW.main_page_yandex import MainPageYandex
from FW.search.search import Search
from FW.web_driver import WebDriver
from FW.API.token.token import Token
from data.settings import Settings


class ApplicationManager:

    driver = None

    def stop_driver(self):
        self.web_driver.driver_exit(self.driver)
        self.driver = None

    def __init__(self):
        self.settings = Settings()
        self.web_driver = WebDriver()
        self.main_page_ya = MainPageYa(self)
        self.main_page_yandex = MainPageYandex(self)
        self.search = Search(self)
        self.api_token = Token(self)
        self.api_users = Users(self)
