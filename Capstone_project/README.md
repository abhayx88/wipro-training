# E-Commerce Application - End-to-End UI Automation Capstone Project

## Overview
This project automates end-to-end user journeys on the TutorialNinja e-commerce site using:
- Python
- Selenium WebDriver (via `SeleniumLibrary`)
- Robot Framework
- Pytest

The framework is keyword-driven, modular, and designed for reuse across standard e-commerce flows.

## Application Under Test
- URL: `https://tutorialsninja.com/demo/`
- Primary automated role: `Customer / End User`

## Implemented Scenarios
1. User Registration and Login
2. Product Search and Product Details
3. Add to Cart
4. Update Cart and Remove Item
5. User Logout and Session Validation

Primary execution style:
- Modular scenario suites with separate files and datasets.

Additional strict-evaluation coverage:
- Modular scenario suites:
  - `tests/scenario_1_registration_login.robot`
  - `tests/scenario_2_product_search_details.robot`
  - `tests/scenario_3_add_to_cart.robot`
  - `tests/scenario_4_update_remove_cart.robot`
  - `tests/scenario_5_logout_session_validation.robot`
- Role coverage suite:
  - `tests/role_coverage.robot` (Customer automated; Vendor/Admin availability checks with explicit skip when AUT does not expose flows)

## Framework Structure
```text
Capstone_project/
|- config/
|- tests/
|- pytest_tests/
|- keywords/
|- pages/
|- pytest_pages/
|- resources/
|- variables/
|- testdata/
|- pytest_utils/
|- reports/
|- .github/workflows/
|- conftest.py
|- pytest.ini
```

## Key Design Choices
- POM-style page resources:
  - `pages/account_page.resource`
  - `pages/product_page.resource`
  - `pages/cart_page.resource`
  - `pages/checkout_page.resource`
- Reusable common wrappers in `resources/base.resource`
- Externalized configuration in `variables/config.py`
- Failure screenshot handling:
  - failed Selenium steps capture screenshots
  - one screenshot captured if a test fails (`Close Application`)
- Explicit waits and retry-safe checks for dynamic DOM behavior

## Data-Driven Testing
- Shared user pool strategy:
  - suite setup registers 5 readable users once per run
  - `ScenarioX User 1..5` map consistently to shared users `1..5` across all scenario suites
- Single shared CSV dataset (5 users, reused by all scenarios):
  - `testdata/e2e_master_data.csv`

## Execution
Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run all tests:

```powershell
robot -d reports tests/
```

Run and generate separate report folders per scenario suite:

```powershell
python run_robot_per_scenario.py
```

Run all pytest tests:

```powershell
pytest
```

Pytest externalized config:
- `config/config.ini` (base URL, timeout, browser)
- env vars `URL`, `TIMEOUT`, `BROWSER` override `config.ini` values

Run with specific browser:

```powershell
robot -d reports --variable BROWSER:chrome tests/
robot -d reports --variable BROWSER:firefox tests/
robot -d reports --variable BROWSER:edge tests/
pytest --browser=edge
```

Or with environment variable (PowerShell):

```powershell
$env:BROWSER="edge"
robot -d reports tests/
```

## Reporting
Robot Framework generates:
- `reports/output.xml`
- `reports/log.html`
- `reports/report.html`
- screenshot artifacts (one per suite + on failed tests)

Pytest generates:
- console report from pytest runner
- screenshots in `reports/pytest/`:
  - one evidence screenshot per module
  - one screenshot on failed tests

Optional pytest HTML report:

```powershell
pytest --html=reports/pytest/report.html --self-contained-html
```

## CI Ready
GitHub Actions workflow is available at:
- `.github/workflows/robot-framework.yml`

It runs tests on both Chrome and Firefox and uploads reports as artifacts.
