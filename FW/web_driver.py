import allure
from selenium import webdriver


class WebDriver:

    def driver_start(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver

    def driver_exit(self, driver):
        driver.quit()