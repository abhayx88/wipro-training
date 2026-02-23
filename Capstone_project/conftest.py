import shutil
import logging
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pytest_pages.account_page import AccountPage
from pytest_utils.config import BASE_URL, BROWSER, PROJECT_ROOT, REPORTS_DIR, TIMEOUT
from pytest_utils.data_loader import load_scenario_data
from pytest_utils.logger import log_step


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=BROWSER, help="chrome|firefox|edge")


def pytest_sessionstart(session):
    if REPORTS_DIR.exists():
        shutil.rmtree(REPORTS_DIR, ignore_errors=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    session.config._evidence_modules = set()
    log_file = REPORTS_DIR / "execution.log"
    logger = logging.getLogger("pytest_steps")
    logger.handlers.clear()
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s | %(message)s"))
    logger.addHandler(file_handler)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


def _create_driver(browser_name: str):
    name = browser_name.strip().lower()
    if name in ("msedge", "microsoftedge"):
        name = "edge"
    if name == "chrome":
        return webdriver.Chrome(options=ChromeOptions())
    if name == "firefox":
        return webdriver.Firefox(options=FirefoxOptions())
    if name == "edge":
        return webdriver.Edge(options=EdgeOptions())
    raise ValueError(f"Unsupported browser '{browser_name}'. Use chrome, firefox, or edge.")


@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    return pytestconfig.getoption("--browser")


@pytest.fixture(scope="session")
def shared_users(browser_name):
    data = load_scenario_data(PROJECT_ROOT / "testdata" / "e2e_master_data.csv")
    users = []

    driver = _create_driver(browser_name)
    driver.maximize_window()
    driver.set_page_load_timeout(60)
    page = AccountPage(driver, BASE_URL, TIMEOUT)
    log_step(f"[Setup] Preparing {len(data)} shared users from CSV emails")

    for i, row in enumerate(data, start=1):
        email = row.get("email", "").strip()
        if not email:
            raise AssertionError(f"Missing manual email in CSV for row {i}.")
        password = row["password"]
        page.login_or_register_then_login(row["firstname"], row["lastname"], email, row["phone"], password)
        page.logout_user()
        page.assert_logged_out()
        users.append(
            {
                "index": i,
                "firstname": row["firstname"],
                "lastname": row["lastname"],
                "email": email,
                "password": password,
            }
        )

    driver.quit()
    return users


@pytest.fixture()
def driver(request, browser_name):
    browser = _create_driver(browser_name)
    browser.maximize_window()
    browser.set_page_load_timeout(60)
    log_step(f"[Browser] Launching tests on {browser_name}")
    yield browser

    module_key = request.node.module.__name__
    evidence_modules = request.config._evidence_modules
    if module_key not in evidence_modules:
        safe = module_key.replace(".", "_")
        browser.save_screenshot(str(REPORTS_DIR / f"evidence_{safe}.png"))
        evidence_modules.add(module_key)

    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        fail_name = request.node.nodeid.replace("/", "_").replace("::", "__")
        fail_name = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in fail_name)
        browser.save_screenshot(str(REPORTS_DIR / f"failed_{fail_name}.png"))
    browser.quit()


@pytest.fixture()
def account_page(driver):
    return AccountPage(driver, BASE_URL, TIMEOUT)
