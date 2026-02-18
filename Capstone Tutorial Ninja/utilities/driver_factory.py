from selenium import webdriver

# try reading config, but don't crash if missing
try:
    from utilities.config_reader import get_browser
    browser = get_browser().lower()
except Exception:
    # fallback default
    browser = "chrome"


def get_driver():

    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
        # default always chrome
        driver = webdriver.Chrome()

    driver.maximize_window()
    return driver
