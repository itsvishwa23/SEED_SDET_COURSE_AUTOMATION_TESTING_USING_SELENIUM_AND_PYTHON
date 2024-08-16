from selenium import webdriver


class open_telosa_login_page:
    def login_page(self):
        driver = webdriver.Chrome()
        driver.get(url="https://telosa.in/Login")
        print(driver.current_url)
        driver.quit()


o1 = open_telosa_login_page()
o1.login_page()
