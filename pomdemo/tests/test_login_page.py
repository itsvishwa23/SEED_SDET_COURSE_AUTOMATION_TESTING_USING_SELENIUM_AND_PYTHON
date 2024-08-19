import pytest
from selenium import webdriver

from pomdemo.pages.login_page_display import LoginPageDisplay


class TestLoginPage:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()

    def testloginpage(self, setup):
        t1 = LoginPageDisplay(self.driver)
        t1.loginpagedisplay()
