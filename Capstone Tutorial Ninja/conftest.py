import pytest
from utilities.driver_factory import get_driver
from utilities.config_reader import get_url
import os
from datetime import datetime


@pytest.fixture
def driver():

    driver = get_driver()
    driver.get(get_url())

    yield driver

    driver.quit()


# -------- ADD THIS PART BELOW --------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        driver = item.funcargs.get("driver")

        if driver:
            folder = "screenshots"
            os.makedirs(folder, exist_ok=True)

            file_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
            driver.save_screenshot(os.path.join(folder, file_name))
