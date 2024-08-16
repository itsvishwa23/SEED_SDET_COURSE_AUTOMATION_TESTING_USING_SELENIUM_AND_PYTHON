from datetime import datetime

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(url="https://www.google.co.in/")
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
driver.save_screenshot(
    f'E:/SEED_PROGRAMING_SDET_COURSE/SEED_SDET_COURSE_AUTOMATION_TESTING_USING_SELENIUM_AND_PYTHON/Day_10/{now}.png')

driver.quit()

actual = "Hi"
expected = "Hi"

print()
try:
    assert actual == expected
    print("Test Case Passed")
except:
    print("Test Case Failed")
