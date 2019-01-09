from selenium import webdriver
import pytest

class TestLogin():

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed.")

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()

    def test_logout(self, test_setup):
        driver.find_element_by_id("welcome").click()
        driver.find_element_by_link_text("Logout").click()




