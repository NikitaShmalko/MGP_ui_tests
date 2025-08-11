from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import allure


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("""
            arguments[0].scrollIntoView({ 
                behavior: 'instant',  // или 'smooth'
                block: 'center'
            });
        """, element)

    def take_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    def click(self, locator):
        self.scroll_to_element(locator)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.take_screenshot()
        element.click()

    def get_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
        return element

    def load(self, url):
        self.driver.get(url)

    def send_keys(self, locator, value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(value)