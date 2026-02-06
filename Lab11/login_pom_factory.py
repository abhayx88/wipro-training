from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lab11.login_locators import LoginLocators


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.username = LoginLocators.USERNAME
        self.password = LoginLocators.PASSWORD
        self.login_btn = LoginLocators.LOGIN_BTN
        self.dashboard = LoginLocators.DASHBOARD

    def enter_username(self, user):
        self.wait.until(
            EC.visibility_of_element_located(LoginLocators.USERNAME)
        ).send_keys(user)

    def enter_password(self, pwd):
        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(pwd)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(LoginLocators.LOGIN_BTN)
        ).click()

    def login_factory(self, user, pwd):

        self.wait.until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(user)

        self.driver.find_element(*self.password).send_keys(pwd)

        self.wait.until(
            EC.element_to_be_clickable(self.login_btn)
        ).click()


    def verify_dashboard(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.dashboard)
        )
