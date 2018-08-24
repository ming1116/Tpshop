import time

from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_login_in(self):
        self.page.mine.click_mine()
        self.page.login.click_login()
        self.page.login_in.input_username("13800138006")
        self.page.login_in.input_password("123456")
        self.page.login_in.click_login_in()
