from page.home_page import HomePage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def mine(self):
        return HomePage(self.driver)
