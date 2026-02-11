import pytest
import time
from Day20.driverfactory import getdriver


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_google_title(browser):
    driver = getdriver(browser)
    driver.get("https://www.google.com/")
    assert "Google" in driver.title
    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_search(browser):
    driver = getdriver(browser)
    driver.get("https://www.bing.com/")

    searchbox = driver.find_element("name", "q")
    searchbox.send_keys("Selenium Grid")
    searchbox.submit()

    import time
    time.sleep(20)
    assert "Selenium Grid" in driver.title
    driver.quit()
