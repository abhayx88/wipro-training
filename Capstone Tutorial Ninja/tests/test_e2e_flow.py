from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.account_page import AccountPage


def test_full_ecommerce_flow(driver):

    # LOGIN
    login = LoginPage(driver)
    login.open_login()
    login.login("abhay+1@gmail.com", "Test@123")

    # SEARCH PRODUCT
    search = SearchPage(driver)
    search.search_product("iphone")
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
