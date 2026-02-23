import pytest

from pytest_pages.cart_page import CartPage
from pytest_pages.product_page import ProductPage
from pytest_utils.config import BASE_URL, PROJECT_ROOT, TIMEOUT
from pytest_utils.data_loader import load_scenario_data
from pytest_utils.logger import log_step


DATA = load_scenario_data(PROJECT_ROOT / "testdata" / "e2e_master_data.csv")


@pytest.mark.ui
@pytest.mark.parametrize("row", DATA, ids=[d["case_name"] for d in DATA])
def test_scenario_3_add_to_cart(driver, account_page, shared_users, row):
    user = shared_users[row["user_index"] - 1]
    product_page = ProductPage(driver, TIMEOUT)
    cart_page = CartPage(driver, BASE_URL, TIMEOUT)
    log_step(f"[Login] Using shared user index {user['index']}: {user['email']}")
    account_page.login_user(user["email"], user["password"])
    cart_page.clear_cart()
    product_page.search(row["product"])
    product_page.open_product_details(row["product"])
    product_page.add_current_product_to_cart()
    cart_page.open_cart()
    cart_page.assert_product_present(row["product"])

