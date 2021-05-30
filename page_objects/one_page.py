from selenium.webdriver.common.by import By
from utilities.object_repository import ObjectRepository


class ObjectTest():
    search = (By.XPATH, "//a[contains(text(),'Gmail')]")

    def click_gmail(self):
        a = ObjectRepository(self.driver)
        a.click1(*ObjectTest.search)
