import pytest
import csv
import os
from pages.search_page import SearchPage
from pages.product_page import ProductPage


def load_products():
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "products.csv")

    with open(path, newline="") as f:
        return [row["product"] for row in csv.DictReader(f)]


@pytest.mark.smoke
@pytest.mark.order(4)
@pytest.mark.parametrize("product_name", load_products())
def test_add_to_cart(driver, product_name):

    search = SearchPage(driver)
    search.search_product(product_name)
    search.open_first_product()

    product = ProductPage(driver)
    product.add_to_cart()

    msg = product.get_success_message()
    assert "Success" in msg
