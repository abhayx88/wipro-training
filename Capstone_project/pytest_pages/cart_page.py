import time

from selenium.webdriver.common.by import By

from pytest_pages.base_page import BasePage
from pytest_utils.logger import log_step


class CartPage(BasePage):
    def __init__(self, driver, base_url: str, timeout: int):
        super().__init__(driver, timeout)
        self.base_url = base_url
        self.cart_url = f"{base_url}index.php?route=checkout/cart"

        self.shopping_cart_link = (By.XPATH, "//span[text()='Shopping Cart']")
        self.cart_content = (By.XPATH, "//div[@id='content']")
        self.quantity_field = (By.XPATH, "//input[contains(@name,'quantity')]")
        self.update_button = (By.XPATH, "//button[@data-original-title='Update']")
        self.remove_first_button = (By.XPATH, "(//button[@data-original-title='Remove'])[1]")

    def open_cart(self):
        log_step("[Cart] Opening shopping cart")
        self.click(self.shopping_cart_link)
        if "Shopping Cart" not in self.driver.page_source:
            raise AssertionError("Shopping cart page did not open.")

    def clear_cart(self):
        log_step("[Cart] Clearing cart before scenario")
        self.driver.get(self.cart_url)
        for _ in range(30):
            buttons = self.driver.find_elements(*self.remove_first_button)
            if not buttons:
                break
            buttons[0].click()
            time.sleep(0.4)

    def assert_product_present(self, product_name: str):
        log_step(f"[Cart] Verifying product present: {product_name}")
        text = self.find_visible(self.cart_content).text
        if product_name not in text:
            raise AssertionError(f"Item not found in cart: '{product_name}'.")

    def update_quantity(self, quantity: int):
        log_step(f"[Cart] Updating quantity to {quantity}")
        for _ in range(5):
            try:
                field = self.find_visible(self.quantity_field)
                field.clear()
                field.send_keys(str(quantity))
                self.click(self.update_button)
                refreshed = self.find_visible(self.quantity_field)
                if refreshed.get_attribute("value") == str(quantity):
                    return
            except Exception:
                time.sleep(1)
        raise AssertionError(f"Cart quantity update failed. Expected '{quantity}'.")

    def remove_product(self, product_name: str):
        log_step(f"[Cart] Removing product from cart: {product_name}")
        locator = (
            By.XPATH,
            f"//div[@id='content']//tr[.//a[contains(normalize-space(),'{product_name}')]]//button[@data-original-title='Remove']",
        )
        self.click(locator)

    def assert_product_not_present(self, product_name: str):
        log_step(f"[Cart] Verifying product removed: {product_name}")
        for _ in range(5):
            text = self.find_visible(self.cart_content).text
            if product_name not in text:
                return
            time.sleep(1)
        raise AssertionError(f"Item still present in cart: '{product_name}'.")
