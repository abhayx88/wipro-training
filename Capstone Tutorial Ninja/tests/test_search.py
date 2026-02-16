import json
from pages.search_page import SearchPage


def test_search_product(driver):

    with open("data/products.json") as f:
        data = json.load(f)

    product_name = data["search_product"]

    search = SearchPage(driver)

    search.search_product(product_name)

    assert "Search" in driver.title

    search.open_first_product()

    assert "iPhone" in driver.page_source
