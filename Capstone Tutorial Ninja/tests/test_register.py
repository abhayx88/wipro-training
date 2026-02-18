import csv
import os
import pytest

from pages.register_page import RegisterPage


def load_users():

    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "users.csv")

    with open(path, newline="") as f:
        return list(csv.DictReader(f))


@pytest.mark.smoke
@pytest.mark.parametrize("user", load_users())
def test_register_user(driver, user):

    register = RegisterPage(driver)
    register.open_register()

    register.register_user(
        "Test",
        "User",
        user["email"],
        user["password"]
    )

    # verify registration success
    assert (
            "Your Account Has Been Created" in driver.page_source
            or
            "Warning: E-Mail Address is already registered!" in driver.page_source
    )

