from selenium.webdriver.common.by import By

from utilities.object_repository import ObjectRepository


class OneTest(ObjectRepository):
    search = (By.XPATH, "//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[3]/center[1]/input[1]")

    def click_search(self):
        return self.click(*OneTest.search)
