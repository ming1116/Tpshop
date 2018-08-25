import random

import allure
import pytest
import time

from allure.constants import AttachmentType
from selenium.webdriver.common.by import By

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file


def random_password():
    password = ""
    for i in range(0, 8):
        password += str(random.randint(0, 9))
        return password


def show_password_data():
    temp_list = list()
    for i in range(0, 2):
        temp_list.append(random_password())
        return temp_list


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    # def test_login_in(self, args):
    #     username = args["username"]
    #     password = args["password"]
    #     expect = args["expect"]
    #     self.page.mine.click_mine()
    #     self.page.login.click_login()
    #     self.page.login_in.input_username(username)
    #     self.page.login_in.input_password(password)
    #     self.page.login_in.click_login_in()
    #     assert self.page.login_in.is_exists(expect)
    #
    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login_invisible"))
    # def test_login_invisible(self, args):
    #     username = args["username"]
    #     password = args["password"]
    #     self.page.mine.click_mine()
    #     self.page.login.click_login()
    #     self.page.login_in.input_username(username)
    #     self.page.login_in.input_password(password)
    #     assert not self.page.login_in.is_invisible()
    @pytest.mark.parametrize("password", show_password_data())
    def test_password(self, password):
        password_location = (By.XPATH, "//*[@text='%s']" % password)
        self.page.mine.click_mine()
        self.page.login_member.click_login_member()
        self.page.login.input_password(password)
        # 点击显示密码之前查看是否存在
        assert not self.page.login.is_login_butt_invisible(password_location)
        self.page.login.is_view_password()
        # 截图
        allure.attach("显示密码:", self.driver.get_screenshot_as_png(), AttachmentType.PNG)
        time.sleep(2)
        assert self.page.login.is_login_butt_invisible(By.XPATH, password_location)
