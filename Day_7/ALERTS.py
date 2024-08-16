import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url="https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)
driver.find_element(By.XPATH, value="//button[@onclick='jsAlert()']").click()
time.sleep(5)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
