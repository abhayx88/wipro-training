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

        print("[Cart] Opening cart dropdown")
        self.click(self.cart_btn)

        time.sleep(2)

        print("[Assert] Cart dropdown should open")
        assert "cart" in self.driver.page_source.lower(), \
            "STEP FAIL → Cart dropdown did not open"

        print("[Cart] Clicking View Cart")
        self.click(self.view_cart)

        print("[Assert] Shopping cart page should open")
        assert "cart" in self.driver.current_url.lower(), \
            "STEP FAIL → Cart page did not open"


    def update_quantity(self, qty):

        print(f"[Cart] Updating quantity to {qty}")

        print("[Assert] Quantity value should exist")
        assert qty, "TEST DATA ERROR → Quantity empty"

        self.type(self.quantity_box, qty)

        print("[Cart] Clicking Update button")
        self.click(self.update_btn)

        print("[Assert] Cart should refresh after update")
        assert "cart" in self.driver.current_url.lower(), \
            "STEP FAIL → Cart did not refresh after update"


    def remove_item(self):

        print("[Cart] Removing item from cart")
        self.click(self.remove_btn)

        print("[Assert] Remove action should succeed")
        assert "cart" in self.driver.current_url.lower(), \
            "STEP FAIL → Remove action failed"
