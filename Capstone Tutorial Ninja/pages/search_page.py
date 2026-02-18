from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):

    search_box = (By.NAME, "search")
    search_btn = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
    first_product = (By.CSS_SELECTOR, ".product-thumb h4 a")

    # SEARCH PRODUCT
    def search_product(self, product):

        print(f"[Search] Searching product → {product}")

        assert product, "SEARCH FAIL → product name empty"

        self.type(self.search_box, product)
        self.click(self.search_btn)

        # ASSERT results opened
        assert "search" in self.driver.current_url.lower(), \
            "SEARCH FAIL → search page not opened"


    # OPEN FIRST PRODUCT
    def open_first_product(self):

        print("[Search] Opening first product")

        self.click(self.first_product)

        # ASSERT product page opened
        assert "product" in self.driver.current_url.lower(), \
            "PRODUCT OPEN FAIL → product page not opened"

