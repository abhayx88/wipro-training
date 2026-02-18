import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    cart_btn = (By.CSS_SELECTOR, "#cart > button")
    view_cart = (By.LINK_TEXT, "View Cart")
    quantity_box = (By.CSS_SELECTOR, "input[name*='quantity']")
    update_btn = (By.CSS_SELECTOR, "button[data-original-title='Update']")
    remove_btn = (By.CSS_SELECTOR, "button[data-original-title='Remove']")

    def open_cart(self):
        self.click(self.cart_btn)
        time.sleep(2)  # allow dropdown animation
        self.click(self.view_cart)

    def update_quantity(self, qty):
        self.type(self.quantity_box, qty)
        self.click(self.update_btn)

    def remove_item(self):
        self.click(self.remove_btn)
