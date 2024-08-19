from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPageDisplay:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def loginpagedisplay(self):
        self.driver.get("https://www.google.co.in/")
        self.driver.find_element(By.XPATH, value="//a[contains(@aria-label,'Search for Images')]").click()
        