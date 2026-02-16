from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_update_and_remove_cart(driver):

    search = SearchPage(driver)
    search.search_product("iphone")
    search.open_first_product()

    product = ProductPage(driver)
    product.add_to_cart()

    cart = CartPage(driver)
    cart.open_cart()

    cart.update_quantity("2")

    cart.remove_item()

    assert "Shopping Cart" in driver.title
