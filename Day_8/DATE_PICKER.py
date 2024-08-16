import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url="https://jqueryui.com/datepicker/")
time.sleep(5)
driver.switch_to.frame(0)
driver.find_element(By.XPATH, value="//input[@id='datepicker']").click()
time.sleep(5)
for i in range(0, 5):
    driver.find_element(By.XPATH, value="//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

driver.find_element(By.XPATH, value="/html/body/div/table/tbody/tr[2]/td[1]/a").click()
time.sleep(5)
date = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[2]/td[1]/a").text

print(date)
