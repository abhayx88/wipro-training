import pytest

from pytest_utils.config import PROJECT_ROOT
from pytest_utils.data_loader import load_scenario_data
from pytest_utils.logger import log_step


DATA = load_scenario_data(PROJECT_ROOT / "testdata" / "e2e_master_data.csv")


@pytest.mark.ui
@pytest.mark.parametrize("row", DATA, ids=[d["case_name"] for d in DATA])
def test_scenario_5_logout_session_validation(driver, account_page, shared_users, row):
    user = shared_users[row["user_index"] - 1]
    log_step(f"[Login] Using shared user index {user['index']}: {user['email']}")
    account_page.login_user(user["email"], user["password"])
    account_page.logout_user()
    account_page.assert_logged_out()

