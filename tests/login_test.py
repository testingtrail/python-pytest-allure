from selenium import webdriver
import pytest

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as environment

#to link the setup in conftest.py
@pytest.mark.usefixtures("test_setup")

class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(environment.URL)

        login = LoginPage(driver)
        login.enter_username(environment.USERNAME)
        login.enter_password(environment.PASSWORD)
        login.click_login()

    def test_logout(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()





