from selenium.webdriver.support.select import Select


class ObjectRepository:

    def __init__(self, driver):
        self.driver = driver

    def click(self,element):
        self.driver.find_element_by_xpath(element).click()

    def print_text(self,element):
        x = self.driver.find_element_by_xpath(element).text()
        print(x)

    def drop_down_text(self,element,text):
        drop_down = Select(self.driver.find_element_by_xpath(element))
        drop_down.select_by_visible_text(text)

    def drop_down_index(self, element, index):
        drop_down = Select(self.driver.find_element_by_xpath(element))
        drop_down.select_by_index(index)

