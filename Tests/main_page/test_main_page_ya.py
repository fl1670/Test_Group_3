from Tests.test_base import TestBase


class TestMainPageYa(TestBase):

    def test_temp_1(self):
        self.APP.main_page.send_keys_in_search_input('Test 12312312')
        self.APP.main_page.click_btn_submit()
        self.APP.search.get_text_title()

    def test_temp_2(self):
        self.APP.main_page.send_keys_in_search_input('qwerty')
        self.APP.main_page.click_btn_submit()

    def test_temp_3(self):
        self.APP.main_page.send_keys_in_search_input('Погода')
        self.APP.main_page.click_btn_submit()
