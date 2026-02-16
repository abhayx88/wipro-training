from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    add_to_cart_btn = (By.ID, "button-cart")
    success_alert = (By.CSS_SELECTOR, ".alert-success")

    def add_to_cart(self):
        self.click(self.add_to_cart_btn)

    def get_success_message(self):
        return self.get_text(self.success_alert)
