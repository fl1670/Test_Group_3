import allure
from allure_commons.types import AttachmentType


class BaseFW:

    def __init__(self, ApplicationManager):
        self.manager = ApplicationManager

    def get_driver(self):
        if self.manager.driver is None:
            self.manager.driver = self.manager.web_driver.driver_start()
        return self.manager.driver

    @allure.step('Открыть страницу {url}')
    def open_main_page(self, url):
        self.get_driver().get(url)

    @allure.step('screenshot')
    def allure_screenshot(self):
        try:
            allure.attach(self.get_driver().get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(str(e))
