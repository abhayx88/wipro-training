from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    my_account = (By.LINK_TEXT, "My Account")
    login_link = (By.LINK_TEXT, "Login")
    email = (By.ID, "input-email")
    password = (By.ID, "input-password")
    login_btn = (By.XPATH, "//input[@value='Login']")

    def open_login(self):

        print("[Login] Opening My Account menu")
        self.click(self.my_account)

        print("[Assert] My Account dropdown should open")
        assert "account" in self.driver.page_source.lower(), \
            "STEP FAIL → My Account dropdown did not open"

        print("[Login] Opening Login page")
        self.click(self.login_link)

        print("[Assert] Login page should be visible")
        assert "login" in self.driver.current_url.lower(), \
            "STEP FAIL → Login page did not open"


    def login(self, user, pwd):

        print(f"[Login] Logging in with {user}")

        print("[Assert] Email should exist")
        assert user, "TEST DATA ERROR → Email is empty"

        print("[Assert] Password should exist")
        assert pwd, "TEST DATA ERROR → Password is empty"

        print("[Login] Typing email")
        self.type(self.email, user)

        print("[Assert] Email field should be filled")
        assert self.driver.find_element(*self.email).get_attribute("value"), \
            "STEP FAIL → Email not typed"

        print("[Login] Typing password")
        self.type(self.password, pwd)

        print("[Assert] Password field should be filled")
        assert self.driver.find_element(*self.password).get_attribute("value"), \
            "STEP FAIL → Password not typed"

        print("[Login] Clicking Login button")
        self.click(self.login_btn)

        print("[Assert] Login should respond")
        assert (
            "account" in self.driver.current_url.lower()
            or "warning" in self.driver.page_source.lower()
        ), "LOGIN ACTION FAILED → No navigation / no response from site"
