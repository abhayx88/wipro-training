import csv
import os
import pytest

from pages.search_page import SearchPage
from utilities.auth_helper import login_or_register


# ---------- BASE PATH ----------
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
            name = row.get("product","").strip()
            if name:
                products.append(name)

    return products


# ---------- SEARCH TEST ----------
@pytest.mark.smoke
@pytest.mark.order(3)

@pytest.mark.parametrize("user", load_users(), ids=lambda x: x["email"])
@pytest.mark.parametrize("product_name", load_products())

def test_search_product(driver, user, product_name):

    # 🔐 LOGIN OR REGISTER AUTO
    login_or_register(driver, user["email"], user["password"])

    # 🔎 SEARCH
    search = SearchPage(driver)
    search.search_product(product_name)

    # ✅ VERIFY
    assert "search" in driver.current_url.lower()
