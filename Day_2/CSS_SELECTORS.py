import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.swiggy.com/")
time.sleep(5)  # Wait for the page to load

reviews = driver.find_elements(By.CSS_SELECTOR, "span.sc-aXZVg.kIcQre")
hotel_names = driver.find_elements(By.CSS_SELECTOR, "div.sc-aXZVg.kVQudY")

print(f"Number of reviews: {len(reviews)}")
print(f"Number of hotel names: {len(hotel_names)}")
