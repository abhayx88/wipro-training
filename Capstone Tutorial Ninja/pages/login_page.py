from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    my_account = (By.LINK_TEXT, "My Account")
    login_link = (By.LINK_TEXT, "Login")
    email = (By.ID, "input-email")
    password = (By.ID, "input-password")
    login_btn = (By.XPATH, "//input[@value='Login']")

    def open_login(self):
        self.click(self.my_account)
        self.click(self.login_link)

    def login(self, user, pwd):
        self.type(self.email, user)
        self.type(self.password, pwd)
        self.click(self.login_btn)
