import csv
import os
import pytest
from pages.login_page import LoginPage
from pages.account_page import AccountPage


def get_first_user():
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "users.csv")

    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return next(reader)

@pytest.mark.smoke
@pytest.mark.order(6)
def test_logout(driver):

    user = get_first_user()

    # LOGIN
    login = LoginPage(driver)
    login.open_login()
    login.login(user["email"], user["password"])

    # LOGOUT
    account = AccountPage(driver)
    account.logout()

    # VERIFY LOGOUT PAGE
    assert "Account Logout" in driver.page_source
