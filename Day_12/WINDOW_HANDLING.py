import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class WindowHandling():
    driver = webdriver.Chrome()
    driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
    driver.implicitly_wait(time_to_wait=3)
    orignal_window = driver.current_window_handle
    print(orignal_window)
    driver.find_element(By.XPATH, value="//button[@id='newWindowBtn']").click()
    for window_handles in driver.window_handles:
        if window_handles != orignal_window:
            driver.switch_to.window(window_handles)
            print(driver.title)
            time.sleep(5)
            driver.switch_to.window(orignal_window)
            print(driver.title)
