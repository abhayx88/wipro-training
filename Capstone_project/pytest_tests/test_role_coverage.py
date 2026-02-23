import time

import pytest

from pytest_utils.logger import log_step


@pytest.mark.ui
def test_customer_role_validation(driver, account_page):
    email = f"qa_pytest_{int(time.time() * 1000)}@example.com"
    password = "Password123"
    account_page.register_user("Test", "User", email, "9999999999", password)
    account_page.logout_user()
    account_page.assert_logged_out()
    account_page.login_user(email, password)
    account_page.logout_user()
    account_page.assert_logged_out()
