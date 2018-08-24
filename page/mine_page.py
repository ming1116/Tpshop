from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    login_butt = By.XPATH, "//*[@text='登录/注册']"

    def click_login(self):
        self.click(self.login_butt)