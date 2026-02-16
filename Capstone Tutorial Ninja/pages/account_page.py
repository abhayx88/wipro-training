from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):

    my_account_menu = (By.CSS_SELECTOR, "#top-links a.dropdown-toggle")
    logout_link = (By.LINK_TEXT, "Logout")

    def logout(self):
        # click dropdown fresh each time
        self.click(self.my_account_menu)
        self.click(self.logout_link)
