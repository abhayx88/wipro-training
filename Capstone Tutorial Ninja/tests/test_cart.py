import pytest
import csv
import os

from pages.search_page import SearchPage
from pages.product_page import ProductPage
from utilities.auth_helper import login_or_register


BASE = os.path.dirname(os.path.dirname(__file__))


# ---------- LOAD USERS ----------
def load_users():

    path = os.path.join(BASE, "data", "users.csv")
    users = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            email = row.get("email","").strip()
            password = row.get("password","").strip()

            if email and password:
                users.append({"email":email,"password":password})

    return users


# ---------- LOAD PRODUCTS ----------
def load_products():

    path = os.path.join(BASE, "data", "products.csv")
    products = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            product = row.get("product","").strip()
            if product:
                products.append(product)

    return products


# ---------- ADD TO CART TEST ----------
@pytest.mark.smoke
@pytest.mark.order(4)

@pytest.mark.parametrize("user", load_users(), ids=lambda x: x["email"])
@pytest.mark.parametrize("product_name", load_products())

def test_add_to_cart(driver, user, product_name):

    # LOGIN OR REGISTER
    login_or_register(driver, user["email"], user["password"])

    # SEARCH
    search = SearchPage(driver)
    search.search_product(product_name)
    search.open_first_product()

    # ADD
    product = ProductPage(driver)
    product.add_to_cart()

    #  VERIFY
    msg = product.get_success_message()
    assert "Success" in msg
