import csv
import os
import pytest

from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.account_page import AccountPage
from pages.register_page import RegisterPage


BASE = os.path.dirname(os.path.dirname(__file__))
USERS = os.path.join(BASE, "data", "users.csv")
PRODUCTS = os.path.join(BASE, "data", "products.csv")


# ---------- SAFE USER LOADER ----------
def load_users():

    users = []

    with open(USERS, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            email = row.get("email", "").strip()
            password = row.get("password", "").strip()

            # skip blank CSV rows
            if email and password:
                users.append({"email": email, "password": password})

    return users


# ---------- SAFE PRODUCT LOADER ----------
def load_products():

    products = []

    with open(PRODUCTS, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row.get("product", "").strip()
            if name:
                products.append(name)

    return products


# ---------- E2E ----------
@pytest.mark.flow
@pytest.mark.order(7)
@pytest.mark.parametrize("user", load_users(), ids=lambda x: x["email"])
@pytest.mark.parametrize("product_name", load_products())
def test_full_ecommerce_flow(driver, user, product_name):

    email = user["email"]
    password = user["password"]

    # ---------- LOGIN ----------
    login = LoginPage(driver)
    login.open_login()
    login.login(email, password)

    # ---------- IF LOGIN FAILED ----------
    # safer detection than "Warning"
    if "account/login" in driver.current_url.lower():

        register = RegisterPage(driver)
        register.open_register()
        register.register_user("Test", "User", email, password)

        # wait for account page
        driver.get("https://tutorialsninja.com/demo/index.php?route=account/account")

    # ---------- SEARCH ----------
    search = SearchPage(driver)
    search.search_product(product_name)
    search.open_first_product()

    # ---------- ADD ----------
    product = ProductPage(driver)
    product.add_to_cart()

    # ---------- CART ----------
    cart = CartPage(driver)
    cart.open_cart()
    cart.update_quantity("2")
    cart.remove_item()

    # ---------- LOGOUT ----------
    account = AccountPage(driver)
    account.logout()

    assert "Account Logout" in driver.page_source
