from selenium.webdriver.common.by import By

from utilities.base_element import BaseElement


class Example(BaseElement):
    search = (By.NAME, "btnK")
    amazon = (By.NAME, "q")

    def __init__(self, driver):
        super().__init__(driver)

    def send_key2(self, get_data):
        return self.do_send_keys(self.amazon, get_data)

    def search1(self):
        return self.do_click(self.search)
