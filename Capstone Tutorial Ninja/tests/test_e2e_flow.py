import csv
import os
import pytest

from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.account_page import AccountPage


# ---------- SAFE PATH BUILD ----------
BASE = os.path.dirname(os.path.dirname(__file__))
USERS = os.path.join(BASE, "data", "users.csv")
PRODUCTS = os.path.join(BASE, "data", "products.csv")


# ---------- MASTER USER ----------
def get_master_user():
    with open(USERS, newline="") as f:
        return next(csv.DictReader(f))


# ---------- LOAD PRODUCTS ----------
def load_products():
    with open(PRODUCTS, newline="") as f:
        return [row["product"] for row in csv.DictReader(f)]


MASTER = get_master_user()


# ---------- ORDERED TEST ----------
@pytest.mark.flow
@pytest.mark.order(7)
@pytest.mark.parametrize("product_name", load_products())
def test_full_ecommerce_flow(driver, product_name):

    # LOGIN
    login = LoginPage(driver)
    login.open_login()
    login.login(MASTER["email"], MASTER["password"])

    # SEARCH
    search = SearchPage(driver)
    search.search_product(product_name)
    search.open_first_product()

    # ADD TO CART
    product = ProductPage(driver)
    product.add_to_cart()

    # CART UPDATE + REMOVE
    cart = CartPage(driver)
    cart.open_cart()
    cart.update_quantity("2")
    cart.remove_item()

    # LOGOUT
    account = AccountPage(driver)
    account.logout()

    # VERIFY LOGOUT
    assert "Account Logout" in driver.page_source
