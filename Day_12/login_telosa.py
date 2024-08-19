import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTelosa:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(time_to_wait=3)
        self.driver.get(url="https://telosa.in/Login")
        self.driver.maximize_window()

    def login(self):
        self.driver.find_element(By.XPATH, value="//input[@placeholder='Enter Username']").send_keys(
            "vabizacy@cyclelove.cc")
        self.driver.find_element(By.XPATH, value="//input[@id='password']").send_keys("Reviews@123")
        self.driver.find_element(By.XPATH, value="//button[@type='submit']").click()
        time.sleep(3)
        if self.driver.current_url == "https://telosa.in/review-moderation/dashboard?status=1":
            print("Login Success")
            self.driver.find_element(By.XPATH,
                                     value="//a[@class='navbar-brand subTab my_class2 ng-star-inserted']").click()
            self.driver.find_element(By.XPATH,
                                     value="//a[normalize-space()='My Customers']//i[@class='pi pi-chevron-down']").click()
            self.driver.find_element(By.XPATH,
                                     value="//button[@class='btn btn-primary']").click()
            self.driver.find_element(By.XPATH,
                                     value="//input[@placeholder='Example: Jermey']").send_keys("First Name")
            self.driver.find_element(By.XPATH,
                                     value="//input[@placeholder='Example: Vargas']").send_keys("Last Name")
            self.driver.find_element(By.XPATH,
                                     value="//label[@class='checkBox pos-relative mr-20 pad-l-25'][normalize-space()='Email']//span[@class='checkmark']").click()

            self.driver.find_element(By.XPATH,
                                     value="//label[@class='checkBox pos-relative mr-20 pad-l-25'][normalize-space()='SMS']//span[@class='checkmark']").click()
          
            self.driver.find_element(By.XPATH,
                                     value="//label[@class='checkBox pos-relative mr-20 pad-l-25'][normalize-space()='WhatsApp']//span[@class='checkmark']").click()

            time.sleep(5)


        else:
            print("Login Failed")


l = LoginTelosa()
l.login()
