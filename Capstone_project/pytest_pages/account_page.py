from selenium.webdriver.common.by import By
import time

from pytest_pages.base_page import BasePage
from pytest_utils.logger import log_step


class AccountPage(BasePage):
    def __init__(self, driver, base_url: str, timeout: int):
        super().__init__(driver, timeout)
        self.base_url = base_url
        self.register_url = f"{base_url}index.php?route=account/register"
        self.login_url = f"{base_url}index.php?route=account/login"
        self.account_url = f"{base_url}index.php?route=account/account"
        self.logout_url = f"{base_url}index.php?route=account/logout"

        self.first_name = (By.ID, "input-firstname")
        self.last_name = (By.ID, "input-lastname")
        self.email = (By.ID, "input-email")
        self.phone = (By.ID, "input-telephone")
        self.password = (By.ID, "input-password")
        self.confirm = (By.ID, "input-confirm")
        self.agree = (By.NAME, "agree")
        self.continue_btn = (By.XPATH, "//input[@value='Continue']")
        self.login_btn = (By.XPATH, "//input[@value='Login']")
        self.account_menu = (By.XPATH, "//span[text()='My Account']")
        self.logout_link = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[text()='Logout']")
        self.form_error = (By.CSS_SELECTOR, ".text-danger")

    def open_register(self):
        self.driver.get(self.register_url)
        self.find_visible(self.first_name)
        self.find_visible(self.email)

    def open_login(self):
        self.driver.get(self.login_url)
        self.find_visible(self.email)
        self.find_visible(self.password)

    def register_user(self, first: str, last: str, email: str, phone: str, password: str):
        log_step(f"[Registration] Registering {first} {last} ({email})")
        self.open_register()
        self.type(self.first_name, first)
        self.type(self.last_name, last)
        self.type(self.email, email)
        self.type(self.phone, phone)
        self.type(self.password, password)
        self.type(self.confirm, password)
        self._submit_registration_once()
        if not self._registration_successful():
            # Retry only when still on registration page.
            if "route=account/register" in self.driver.current_url:
                self._submit_registration_once()
        self.assert_registration_successful()

    def _submit_registration_once(self):
        self.find_visible(self.agree).click()
        self.find_visible(self.continue_btn).click()

    def _registration_successful(self) -> bool:
        return (
            "route=account/success" in self.driver.current_url
            or "Your Account Has Been Created!" in self.driver.page_source
        )

    def assert_registration_successful(self):
        page = self.driver.page_source
        if "Warning: E-Mail Address is already registered!" in page:
            raise AssertionError("User not registered: e-mail already exists.")
        if "Warning: You must agree to the Privacy Policy!" in page:
            raise AssertionError("User not registered: privacy policy agreement was not accepted.")
        errors = self.driver.find_elements(*self.form_error)
        if errors:
            raise AssertionError(f"User not registered: form validation error - {errors[0].text}")
        if not self._registration_successful():
            raise AssertionError("User not registered: registration success was not confirmed.")

    def login_user(self, email: str, password: str):
        log_step(f"[Login] Logging in with {email}")
        self.open_login()
        self.type(self.email, email)
        self.type(self.password, password)
        self.find_visible(self.login_btn).click()
        self.assert_logged_in()

    def try_login_user(self, email: str, password: str) -> bool:
        log_step(f"[Login] Trying login with {email}")
        self.open_login()
        self.type(self.email, email)
        self.type(self.password, password)
        self.find_visible(self.login_btn).click()
        for _ in range(6):
            page = self.driver.page_source
            url = self.driver.current_url
            if "Warning: No match for E-Mail Address and/or Password." in page:
                return False
            if "route=account/account" in url or "Edit your account information" in page:
                return True
            time.sleep(1)
        return False

    def login_or_register_then_login(
        self, first: str, last: str, email: str, phone: str, password: str
    ):
        if self.try_login_user(email, password):
            return
        log_step(f"[Registration] Login failed for {email}; registering and retrying login")
        self.register_user(first, last, email, phone, password)
        self.logout_user()
        self.assert_logged_out()
        self.login_user(email, password)

    def assert_logged_in(self):
        for _ in range(6):
            page = self.driver.page_source
            url = self.driver.current_url
            if "Warning: No match for E-Mail Address and/or Password." in page:
                raise AssertionError("Login failed: user not found or password is invalid.")
            if "route=account/account" in url or "Edit your account information" in page:
                return
            time.sleep(1)
        raise AssertionError("Login failed: account page was not reached.")

    def logout_user(self):
        log_step("[Account] Logging out current user")
        try:
            self.find_visible(self.account_menu).click()
            self.find_visible(self.logout_link).click()
        except Exception:
            self.driver.get(self.logout_url)

    def assert_logged_out(self):
        self.driver.get(self.account_url)
        page = self.driver.page_source
        url = self.driver.current_url
        if "route=account/account" in url:
            raise AssertionError("Session is still active.")
        if "route=account/login" not in url and "Returning Customer" not in page:
            raise AssertionError("Login redirection was not confirmed.")
