import csv
import os
import pytest
from pages.login_page import LoginPage


def get_first_user():
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "users.csv")

    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return next(reader)   # ONLY first user

@pytest.mark.smoke
@pytest.mark.order(2)
def test_login(driver):

    user = get_first_user()

    login = LoginPage(driver)
    login.open_login()
    login.login(user["email"], user["password"])

    assert "My Account" in driver.title
