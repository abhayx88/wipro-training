from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from utilities.config_reader import get_explicit_wait
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, get_explicit_wait())

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        for _ in range(3):
            try:
                element = self.wait.until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
                time.sleep(1.2)   # demo visible speed
                return
            except StaleElementReferenceException:
                time.sleep(1)

        raise Exception("Element not clickable")

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        time.sleep(1.2)

    def get_text(self, locator):
        return self.find(locator).text
