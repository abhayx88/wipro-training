from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time


def browser_navigation():

    service = Service()
    driver = webdriver.Edge(service=service)

    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://tutorialsninja.com/demo/")
    print("Title:", driver.title)
    time.sleep(2)

    driver.get("https://tutorialsninja.com/demo/index.php?route=product/category&path=20")
    print("Title:", driver.title)
    time.sleep(2)

    driver.back()
    print("Back Title:", driver.title)
    time.sleep(2)

    driver.forward()
    print("Forward Title:", driver.title)
    time.sleep(2)

    driver.refresh()
    print("Refresh Title:", driver.title)
    time.sleep(2)

    assert "Desktops" in driver.title

    time.sleep(3)
    driver.quit()


def test_browser_navigation():
    browser_navigation()


if __name__ == "__main__":
    browser_navigation()
