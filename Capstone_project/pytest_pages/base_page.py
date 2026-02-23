from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, timeout: int):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.find_visible(locator)
        element.click()

    def type(self, locator, text: str):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def is_text_present(self, text: str) -> bool:
        return text in self.driver.page_source

