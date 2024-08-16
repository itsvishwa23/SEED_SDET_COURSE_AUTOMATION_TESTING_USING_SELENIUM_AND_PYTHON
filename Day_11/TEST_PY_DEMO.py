import time

from selenium import webdriver


def test_login_page_display():
    driver = webdriver.Chrome()
    driver.get("https://telosa.in/Login")
    expected_title = driver.title
    actual_title = "Telosa"
    assert expected_title == actual_title
    time.sleep(5)
    driver.quit()


def test_login_page_display_2():
    driver = webdriver.Chrome()
    driver.get("https://telosa.in/Login")
    expected_title = driver.title
    actual_title = "Telosa"
    assert expected_title == actual_title
    time.sleep(5)
    driver.quit()
