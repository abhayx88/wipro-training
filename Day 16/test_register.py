from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def register_test():

    driver = webdriver.Edge()
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

    email = f"test{random.randint(10000,99999)}@gmail.com"

    wait.until(EC.visibility_of_element_located((By.ID, "input-firstname"))).send_keys("Abhay")
    driver.find_element(By.NAME, "lastname").send_keys("Gupta")
    driver.find_element(By.CSS_SELECTOR, "input#input-email").send_keys(email)
    driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("9876543210")
    driver.find_element(By.ID, "input-password").send_keys("Test@123")
    driver.find_element(By.ID, "input-confirm").send_keys("Test@123")

    driver.find_element(By.CLASS_NAME, "radio-inline").click()
    driver.find_element(By.XPATH, "//input[@name='agree']").click()
    driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()

    success_text = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='content']/h1"))
    ).text

    assert "Your Account Has Been Created!" in success_text

    driver.quit()


def test_register():
    register_test()


if __name__ == "__main__":
    register_test()
    print("TEST PASSED — Account Created Successfully!")
