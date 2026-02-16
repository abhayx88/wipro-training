from pages.search_page import SearchPage
from pages.product_page import ProductPage


def test_add_to_cart(driver):

    search = SearchPage(driver)
    search.search_product("iphone")
    search.open_first_product()

    product = ProductPage(driver)
    product.add_to_cart()

    assert "Success" in product.get_success_message()
