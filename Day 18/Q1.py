import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

class LoginPage(BasePage):

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")
    success_msg = (By.ID, "flash")

    def login(self, user, pwd):
        self.enter_text(self.username, user)
        self.enter_text(self.password, pwd)
        self.click(self.login_btn)

    def success_message(self):
        return self.get_text(self.success_msg)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/login")

    yield driver
    driver.quit()


def test_valid_login(driver):

    login = LoginPage(driver)

    login.login("tomsmith", "SuperSecretPassword!")

    assert "secure area" in login.success_message().lower()

    print("\nTEST PASSED — Login Successful")
