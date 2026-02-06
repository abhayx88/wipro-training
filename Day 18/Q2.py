from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Open iframe site
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")

time.sleep(3)

# Switch to outer iframe
driver.switch_to.frame("iframeResult")

# Switch to inner iframe
driver.switch_to.frame(0)

# Enter text inside iframe
driver.find_element(By.TAG_NAME, "body").send_keys("Hello! Typing inside iframe.")

# Switch back to main content
driver.switch_to.default_content()

# Open new tab
driver.execute_script("window.open('https://www.selenium.dev');")

parent = driver.current_window_handle
all_windows = driver.window_handles

# Switch between windows and print titles
for window in all_windows:
    driver.switch_to.window(window)
    print(driver.title)

# Close child window
for window in all_windows:
    if window != parent:
        driver.switch_to.window(window)
        driver.close()

# Return to parent
driver.switch_to.window(parent)
print("Returned to Parent:", driver.title)

time.sleep(2)
driver.quit()
