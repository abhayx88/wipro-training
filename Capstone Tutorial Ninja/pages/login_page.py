from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    my_account = (By.LINK_TEXT, "My Account")
    login_link = (By.LINK_TEXT, "Login")
    email = (By.ID, "input-email")
    password = (By.ID, "input-password")
    login_btn = (By.XPATH, "//input[@value='Login']")

    def open_login(self):

        # CLICK MY ACCOUNT
        self.click(self.my_account)

        # ASSERT dropdown opened
        assert "account" in self.driver.page_source.lower(), \
            "STEP FAIL → My Account dropdown did not open"

        # CLICK LOGIN
        self.click(self.login_link)

        # ASSERT login page opened
        assert "login" in self.driver.current_url.lower(), \
            "STEP FAIL → Login page did not open"


    def login(self, user, pwd):

        # ASSERT TEST DATA EXISTS
        assert user, "TEST DATA ERROR → Email is empty"
        assert pwd, "TEST DATA ERROR → Password is empty"

        # TYPE EMAIL
        self.type(self.email, user)

        # ASSERT email field filled
        assert self.driver.find_element(*self.email).get_attribute("value"), \
            "STEP FAIL → Email not typed"

        # TYPE PASSWORD
        self.type(self.password, pwd)

        # ASSERT password field filled
        assert self.driver.find_element(*self.password).get_attribute("value"), \
            "STEP FAIL → Password not typed"

        # CLICK LOGIN
        self.click(self.login_btn)

        # ASSERT LOGIN RESPONSE HAPPENED
        assert (
            "account" in self.driver.current_url.lower()
            or "warning" in self.driver.page_source.lower()
        ), "LOGIN ACTION FAILED → No navigation / no response from site"
