import json

from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.account_page import AccountPage


def test_full_ecommerce_flow(driver):

    # LOAD USER DATA
    with open("data/users.json") as f:
        user_data = json.load(f)

    email = user_data["valid_user"]["email"]
    password = user_data["valid_user"]["password"]

    # LOAD PRODUCT DATA
    with open("data/products.json") as f:
        product_data = json.load(f)

    product_name = product_data["search_product"]

    # LOGIN
    login = LoginPage(driver)
    login.open_login()
    login.login(email, password)

    # SEARCH PRODUCT
    search = SearchPage(driver)
    search.search_product(product_name)
    search.open_first_product()

    # ADD TO CART
    product = ProductPage(driver)
    product.add_to_cart()

    # UPDATE & REMOVE CART
    cart = CartPage(driver)
    cart.open_cart()
    cart.update_quantity("2")
    cart.remove_item()

    # LOGOUT
    account = AccountPage(driver)
    account.logout()

    assert "Account Logout" in driver.page_source
