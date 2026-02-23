import pytest

from pytest_utils.config import PROJECT_ROOT
from pytest_utils.data_loader import load_scenario_data
from pytest_utils.logger import log_step


DATA = load_scenario_data(PROJECT_ROOT / "testdata" / "e2e_master_data.csv")


@pytest.mark.ui
@pytest.mark.parametrize("row", DATA, ids=[d["case_name"] for d in DATA])
def test_scenario_1_registration_login(driver, account_page, row):
    email = row["email"]
    password = row["password"]
    log_step(f"[Login] Scenario 1 uses manual email: {email}")
    account_page.login_or_register_then_login(
        row["firstname"], row["lastname"], email, row["phone"], password
    )
    account_page.logout_user()
    account_page.assert_logged_out()
    account_page.login_user(email, password)

