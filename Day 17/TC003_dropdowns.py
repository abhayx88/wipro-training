from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.get("https://tutorialsninja.com/demo/")

driver.find_element(By.LINK_TEXT, "Desktops").click()
driver.find_element(By.LINK_TEXT, "Mac (1)").click()

dropdown = Select(driver.find_element(By.ID, "input-sort"))
dropdown.select_by_index(4)

# wait for page reload
time.sleep(2)

# ✅ locate again (VERY IMPORTANT)
dropdown = Select(driver.find_element(By.ID, "input-sort"))

for option in dropdown.options:
    print(option.text)
