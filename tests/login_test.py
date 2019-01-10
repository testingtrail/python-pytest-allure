from selenium import webdriver
import pytest

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as environment


class TestLogin():

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path= "C:/Users/jorge/Desktop/Work/Code/Mine/Python/AutomationFramework_1/drivers/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed.")

    def test_login(self, test_setup):
        driver.get(environment.URL)

        login = LoginPage(driver)
        login.enter_username(environment.USERNAME)
        login.enter_password(environment.PASSWORD)
        login.click_login()

    def test_logout(self, test_setup):
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()





