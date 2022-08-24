

class BaseFW:

    def __init__(self, ApplicationManager):
        self.manager = ApplicationManager

    def get_driver(self):
        if self.manager.driver is None:
            self.manager.driver = self.manager.web_driver.driver_start()
        return self.manager.driver

    def open_main_page(self, url):
        self.get_driver().get(url)
