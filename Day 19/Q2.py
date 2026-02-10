import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

GRID_URL = "http://localhost:4444"


def start_driver(browser):
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    else:
        raise ValueError("Unsupported browser")

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )
    return driver


def run_test(browser):
    driver = start_driver(browser)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print(f"{browser.upper()} Test Passed ✅ | Title: {driver.title}")
    driver.quit()


if __name__ == "__main__":
    browsers = ["chrome", "firefox"]
    for browser in browsers:
        run_test(browser)


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_google_title(browser):
    run_test(browser)
