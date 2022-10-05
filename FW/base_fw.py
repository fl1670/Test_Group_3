import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    @allure.step('send_keys')
    def send_keys(self, locator, text):
        self.get_driver().find_element(locator[0], locator[1]).send_keys(text)

    @allure.step('click')
    def click(self, locator):
        self.get_driver().find_element(locator[0], locator[1]).click()

    @allure.step('get_text')
    def get_text(self, locator):
        return self.get_driver().find_element(locator[0], locator[1]).text

    def find_element(self, locator):
        try:
            return WebDriverWait(self.get_driver(), 10).until(EC.presence_of_element_located(locator))
        except:
            self.allure_screenshot()
            raise

    def find_elements(self, locator):
        try:
            return WebDriverWait(self.get_driver(), 10).until(EC.presence_of_all_elements_located(locator))
        except:
            self.allure_screenshot()
            raise
