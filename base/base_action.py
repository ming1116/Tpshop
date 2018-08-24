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
