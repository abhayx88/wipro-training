from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.config_reader import get_browser, get_implicit_wait

def get_driver():

    browser = get_browser().lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    else:
        raise Exception("Browser not supported")

    driver.implicitly_wait(get_implicit_wait())

    return driver