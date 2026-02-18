import csv
import os
import pytest

from pages.account_page import AccountPage
from utilities.auth_helper import login_or_register


# ---------- LOAD USERS ----------
def load_users():

    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "users.csv")

    users = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            email = row.get("email","").strip()
            password = row.get("password","").strip()

            # skip blank rows
            if email and password:
                users.append({"email": email, "password": password})

    return users


# ---------- TEST ----------
@pytest.mark.smoke
@pytest.mark.order(6)
@pytest.mark.parametrize("user", load_users(), ids=lambda x: x["email"])

def test_logout(driver, user):

    #  LOGIN OR REGISTER
    login_or_register(driver, user["email"], user["password"])

    #  LOGOUT
    account = AccountPage(driver)
    account.logout()

    #  VERIFY
    assert "Account Logout" in driver.page_source
