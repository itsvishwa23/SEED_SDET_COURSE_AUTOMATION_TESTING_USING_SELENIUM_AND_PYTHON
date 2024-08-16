import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/jqueryui/menu")
time.sleep(10)
a = ActionChains(driver)
m = driver.find_element(By.XPATH, value="//a[normalize-space()='Enabled']")
a.move_to_element(m).click().perform()
n = driver.find_element(By.XPATH, value="//a[normalize-space()='Back to JQuery UI']")
a.move_to_element(n).click().perform()
print(driver.current_url)
print(driver.title)
