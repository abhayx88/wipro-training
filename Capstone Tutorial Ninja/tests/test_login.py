import csv
import os
import pytest
from utilities.auth_helper import login_or_register


# ---------- SAFE USER LOADER ----------
def load_users():

    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "users.csv")

    users = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            email = row.get("email", "").strip()
            password = row.get("password", "").strip()

            # ignore blank rows
            if email and password:
                users.append({"email": email, "password": password})

    return users


# ---------- LOGIN TEST ----------
@pytest.mark.smoke
@pytest.mark.order(2)
@pytest.mark.parametrize("user", load_users())
def test_login(driver, user):

    login_or_register(driver, user["email"], user["password"])

    assert "My Account" in driver.title
