import pytest

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    def test_login_in(self, args):
        username = args["username"]
        password = args["password"]
        expect = args["expect"]
        self.page.mine.click_mine()
        self.page.login.click_login()
        self.page.login_in.input_username(username)
        self.page.login_in.input_password(password)
        self.page.login_in.click_login_in()
        assert self.page.login_in.is_exists(expect)

    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login_invisible"))
    def test_login_invisible(self, args):
        username = args["username"]
        password = args["password"]
        self.page.mine.click_mine()
        self.page.login.click_login()
        self.page.login_in.input_username(username)
        self.page.login_in.input_password(password)
        assert not self.page.login_in.is_invisible()
