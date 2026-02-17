import csv
import os
import pytest
from pages.search_page import SearchPage


def load_products():
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "products.csv")

    products = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row["product"])
    return products

@pytest.mark.smoke
@pytest.mark.order(3)
@pytest.mark.parametrize("product_name", load_products())
def test_search_product(driver, product_name):

    search = SearchPage(driver)
    search.search_product(product_name)

    # verify search results page opened
    assert "Search" in driver.title
