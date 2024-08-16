import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)
driver.find_element(By.XPATH, value="//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, value="//input[@placeholder='Password']").send_keys("admin123")
time.sleep(5)
driver.find_element(By.XPATH, value="//button[@type='submit']").click()
time.sleep(10)
actual_url = driver.current_url
expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
assert actual_url == expected_url
