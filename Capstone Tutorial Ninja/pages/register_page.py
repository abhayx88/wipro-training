from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):

    # MENU
    my_account = (By.XPATH, "//span[text()='My Account']")
    register_link = (By.LINK_TEXT, "Register")

    # FORM
    firstname = (By.ID, "input-firstname")
    lastname = (By.ID, "input-lastname")
    email = (By.ID, "input-email")
    telephone = (By.ID, "input-telephone")
    password = (By.ID, "input-password")
    confirm = (By.ID, "input-confirm")

    agree_checkbox = (By.NAME, "agree")
    continue_btn = (By.CSS_SELECTOR, "input[value='Continue']")

    # OPEN REGISTER PAGE
    def open_register(self):
        self.click(self.my_account)
        self.click(self.register_link)

    # REGISTER USER
    def register_user(self, firstname, lastname, email, password):

        self.type(self.firstname, firstname)
        self.type(self.lastname, lastname)
        self.type(self.email, email)
        self.type(self.telephone, "9999999999")
        self.type(self.password, password)
        self.type(self.confirm, password)

        self.click(self.agree_checkbox)
        self.click(self.continue_btn)
