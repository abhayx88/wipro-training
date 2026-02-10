from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
start_button.click()

wait = WebDriverWait(driver, 15)
hello_text = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='finish']/h4"))
)

print("Explicit Wait: Element is clickable and ready!")

fluent_wait = WebDriverWait(
    driver,
    timeout=20,
    poll_frequency=2,
    ignored_exceptions=[Exception]
)

element = fluent_wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
)

# 4. Print message
print("Fluent Wait: Element is available for interaction!")
print("Text on screen:", element.text)

driver.quit()
