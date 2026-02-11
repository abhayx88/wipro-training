from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

GRIDURL = "http://localhost:4444"


def getdriver(browser):

    if browser.lower() == "chrome":
        options = ChromeOptions()

    elif browser.lower() == "firefox":
        options = FirefoxOptions()

    else:
        raise ValueError("Browser not supported")

    driver = webdriver.Remote(
        command_executor=GRIDURL,
        options=options
    )

    driver.maximize_window()
    return driver
