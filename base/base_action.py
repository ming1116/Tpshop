from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    # 定位元素
    def find_element(self, location, wait=10.0, time=1.0):
        by, value = location
        wait = WebDriverWait(self.driver, wait, time)
        return wait.until(lambda x: x.find_element(by, value))

    # 点位多个元素
    def find_elements(self, location, wait=10.0, time=1.0):
        by, value = location
        wait = WebDriverWait(self.driver, wait, time)
        return wait.until(lambda x: x.find_elements(by, value))

    # 点击
    def click(self, location):
        self.find_element(location).click()

    # 输入
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

        element = self.find_element((By.XPATH, message), timeout, 0.1)
        return element.text

    # 获取内容
    def is_exists(self, massage):
        try:
            self.find_toast(massage)
            return True
        except Exception:
            return False

    # 判断登录按钮可见
    def is_login_butt_invisible(self, location):
        return self.find_element(location).get_attribute("enabled") == "true"

    # 判断显示密码按钮是否可用
    def is_login_in_password(self, location):
        try:
            self.find_element(location)
            return True
        except:
            return False
