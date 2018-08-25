import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_input = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_input = By.ID, "com.tpshop.malls:id/edit_password"
    login_in_butt = By.ID, "com.tpshop.malls:id/btn_login"
    view_password_butt = By.ID, "com.tpshop.malls:id/img_view_pwd"

    @allure.step(title="输入用户名")
    def input_username(self, text):
        allure.attach('输入用户名:', 'text')
        self.input(self.username_input, text)

    @allure.step(title="输入密码")
    def input_password(self, text):
        allure.attach('输入密码:', 'text')
        self.input(self.password_input, text)

    @allure.step(title="点击登录")
    def click_login_in(self):
        self.click(self.login_in_butt)

    # 判断登录可见
    def is_invisible(self):
        self.is_login_butt_invisible(self.login_in_butt)

    @allure.step(title="点击显示密码")
    def is_view_password(self):
        self.click(self.view_password_butt)
