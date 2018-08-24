from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_input = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_input = By.ID, "com.tpshop.malls:id/edit_password"
    login_in_butt = By.ID, "com.tpshop.malls:id/btn_login"

    def click_login(self):
        self.click(self.login_butt)

    def input_username(self, text):
        self.input(self.username_input, text)

    def input_password(self, text):
        self.input(self.password_input, text)

    def click_login_in(self):
        self.click(self.login_in_butt)
