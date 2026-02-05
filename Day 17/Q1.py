from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

    email = f"abhay{random.randint(10000,99999)}@gmail.com"

    wait.until(EC.visibility_of_element_located((By.ID, "input-firstname"))).send_keys("Abhay")
    driver.find_element(By.ID, "input-lastname").send_keys("Gupta")
    driver.find_element(By.ID, "input-email").send_keys(email)
    driver.find_element(By.ID, "input-telephone").send_keys("9876543210")
    driver.find_element(By.ID, "input-password").send_keys("Test@123")
    driver.find_element(By.ID, "input-confirm").send_keys("Test@123")

    driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()

    driver.find_element(By.NAME, "agree").click()

    driver.find_element(By.XPATH, "//input[@value='Continue']").click()

    confirmation = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='content']/h1"))
    ).text

    print("Message Found:", confirmation)

    assert "Your Account Has Been Created!" in confirmation

    print("TEST PASSED")

except Exception as e:
    print("TEST FAILED")
    print("Error:", e)

finally:
    driver.quit()
