import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class login_to_website:

    def login(self):
        driver = webdriver.Chrome()
        driver.get(url="https://telosa.in/Login")
        driver.find_element(By.XPATH, value="//input[@placeholder='Enter Username']").send_keys("vabizacy@cyclelove.cc")
        driver.find_element(By.XPATH, value="//input[@id='password']").send_keys("Reviews@123")
        time.sleep(3)
        driver.find_element(By.XPATH, value="//button[@type='submit']").click()
        time.sleep(3)
        if driver.current_url == "https://telosa.in/review-moderation/dashboard?status=1":
            print("Login Success")
        else:
            print("Login Failed")

        driver.find_element(By.XPATH, value="//a[@id='navbardrop']").click()
        driver.find_element(By.XPATH, value="//a[normalize-space()='Logout']").click()
        time.sleep(3)
        if driver.current_url == "https://telosa.in/Login":
            print("Logout Success")
        else:
            print("Logout Failed")


l1 = login_to_website()
l1.login()
