from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")


driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

alert = driver.switch_to.alert

print("Alert Message:", alert.text)
alert.accept()

time.sleep(2)


driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

confirm_alert = driver.switch_to.alert
print("Confirmation Message:", confirm_alert.text)

confirm_alert.dismiss()

time.sleep(2)


driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("Hello Abhay!")
prompt_alert.accept()

time.sleep(2)


result = driver.find_element(By.ID, "result").text

print("Result on page:", result)

if "Hello Abhay!" in result:
    print("Prompt handled successfully!")
else:
    print("Prompt handling failed!")

# Close browser
driver.quit()
