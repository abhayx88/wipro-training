from selenium.webdriver.common.by import By

from pytest_pages.base_page import BasePage
from pytest_utils.logger import log_step


class ProductPage(BasePage):
    def __init__(self, driver, timeout: int):
        super().__init__(driver, timeout)
        self.search_field = (By.NAME, "search")
        self.search_button = (By.XPATH, "//button[@class='btn btn-default btn-lg']")
        self.product_title = (By.CSS_SELECTOR, "div#content h1")
        self.add_to_cart = (By.ID, "button-cart")
        self.success_alert = (By.CSS_SELECTOR, ".alert-success")

    def search(self, product_name: str):
        log_step(f"[Product] Searching product: {product_name}")
        self.find_visible(self.search_field)
        self.find_visible(self.search_button)
        self.type(self.search_field, product_name)
        self.click(self.search_button)
        self.assert_product_in_results(product_name)

    def assert_product_in_results(self, product_name: str):
        if "There is no product that matches the search criteria." in self.driver.page_source:
            raise AssertionError(f"Product not found: '{product_name}'.")
        locator = (
            By.XPATH,
            f"//div[contains(@class,'product-thumb')]//a[contains(normalize-space(),'{product_name}')]",
        )
        self.find_visible(locator)

    def open_product_details(self, product_name: str):
        log_step(f"[Product] Opening product details: {product_name}")
        locator = (
            By.XPATH,
            f"//div[contains(@class,'product-thumb')]//a[contains(normalize-space(),'{product_name}')]",
        )
        self.click(locator)
        self.assert_product_page(product_name)

    def assert_product_page(self, product_name: str):
        heading = self.find_visible(self.product_title).text.strip()
        if heading != product_name:
            raise AssertionError(f"Product details mismatch. Expected '{product_name}', got '{heading}'.")

    def add_current_product_to_cart(self):
        log_step("[Cart] Adding current product to cart")
        self.click(self.add_to_cart)
        if "Success" not in self.find_visible(self.success_alert).text:
            raise AssertionError("Add to cart failed: success message not shown.")

