from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

box = driver.find_element(By.NAME, "q")
box.send_keys("selenium (software)")
time.sleep(5)
box.submit()
time.Sleep(10)
driver.quit()