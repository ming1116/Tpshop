import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    mine_butt = By.XPATH, "//*[@text='我的']"

    @allure.step(title="点击我的")
    def click_mine(self):
        self.click(self.mine_butt)
