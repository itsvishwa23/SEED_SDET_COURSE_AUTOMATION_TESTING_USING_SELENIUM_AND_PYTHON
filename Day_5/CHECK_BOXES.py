from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url="https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH, value="//input[@id='sunday']").click()
