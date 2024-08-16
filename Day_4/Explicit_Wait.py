import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get(url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
driver.find_element(By.XPATH, value="//input[@placeholder='Username']").send_keys("Admin")
   