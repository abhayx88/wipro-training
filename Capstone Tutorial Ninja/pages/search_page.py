from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):

    search_box = (By.NAME, "search")
    search_btn = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
    first_product = (By.CSS_SELECTOR, ".product-thumb h4 a")

    def search_product(self, product):
        self.type(self.search_box, product)
        self.click(self.search_btn)

    def open_first_product(self):
        self.click(self.first_product)
