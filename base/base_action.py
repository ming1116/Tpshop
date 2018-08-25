from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, wait=10, time=1):
        by, value = location
        wait = WebDriverWait(self.driver, wait, time)
        return wait.until(lambda x: x.find_element(by, value))

    def find_elements(self, location, wait=10, time=1):
        by, value = location
        wait = WebDriverWait(self.driver, wait, time)
        return wait.until(lambda x: x.find_elements(by, value))

    def click(self, location):
        self.find_element(location).click()

    def input(self, location, text):
        self.find_element(location).send_keys(text)

    # 点击返回4
    def press_back(self):
        self.driver.press_keycode(4)

    # 回车键
    def press_enter(self):
        self.driver.press_keycode(66)

    # 获取toast
    def find_toast(self, message, timeout=3):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位

        element = WebDriverWait(self.driver, timeout, 0.1).until(lambda x: x.find_element(By.XPATH, message))
        return element.text
