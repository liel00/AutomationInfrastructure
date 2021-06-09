from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def move_mouse_to_element(self, text):
        action = ActionChains(self.driver)
        action.move_to_element(text).perform()

    def move_mouse_to_element_click(self, text):
        action = ActionChains(self.driver)
        action.move_to_element(text).click().perform()
