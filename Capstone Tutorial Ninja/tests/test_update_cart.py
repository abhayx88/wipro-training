import pytest
import csv
import os
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def load_products():
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "products.csv")

    with open(path, newline="") as f:
        return [row["product"] for row in csv.DictReader(f)]


@pytest.mark.smoke
@pytest.mark.order(5)
@pytest.mark.parametrize("product_name", load_products())
def test_update_and_remove_cart(driver, product_name):

    # SEARCH
    search = SearchPage(driver)
    search.search_product(product_name)
    search.open_first_product()

    # ADD
    product = ProductPage(driver)
    product.add_to_cart()

    # OPEN CART
    cart = CartPage(driver)
    cart.open_cart()

    # UPDATE
    cart.update_quantity("2")

    # REMOVE
    cart.remove_item()

    assert "Shopping Cart" in driver.title
