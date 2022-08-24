from Tests.test_base import TestBase


class TestMainPageYandex(TestBase):

    def setup_method(self):
        self.APP.main_page.open_main_page('https://yandex.ru/')

    def test_temp_1(self):
        self.APP.main_page.send_keys_in_search_input('Test')
        self.APP.main_page.click_btn_submit()

    def test_temp_2(self):
        self.APP.main_page.send_keys_in_search_input('qwerty')
        self.APP.main_page.click_btn_submit()

    def test_temp_3(self):
        self.APP.main_page.send_keys_in_search_input('Погода')
        self.APP.main_page.click_btn_submit()
