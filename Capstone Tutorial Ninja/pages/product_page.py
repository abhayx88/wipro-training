from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    add_to_cart_btn = (By.ID, "button-cart")
    success_alert = (By.CSS_SELECTOR, ".alert-success")

    def add_to_cart(self):

        print("[Product] Clicking Add To Cart")

        self.click(self.add_to_cart_btn)

        print("[Assert] Add to cart button should work")

        # wait for success alert
        msg = self.get_success_message()

        assert msg, "STEP FAIL → No success message after Add To Cart"

        print("[Assert] Product should be added successfully")

        assert "success" in msg.lower(), \
            f"ADD TO CART FAILED → Message was: {msg}"


    def get_success_message(self):

        print("[Product] Reading success message")

        msg = self.get_text(self.success_alert)

        print(f"[INFO] Success message: {msg}")

        return msg
