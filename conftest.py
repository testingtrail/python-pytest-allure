import pytest

#Get browser name from arguments, use parser as it is
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome:  ")


#conftest is used to have the fixtures in one place, so this portion was in login_test.py
# just added request param, from selenium import webdriver and request.cls.driver = driver
@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager

    browser = request.config.getoption("--browser")
    if browser == "chrome":
        #only this command is needed to download or look the chromedriver, no need for .exe
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome(executable_path= "C:/Users/jorge/Desktop/Work/Code/Mine/PythonAutomationFramework/drivers/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge(EdgeDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.maximize_window()
    #next line will sent the driver variable to the class
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test completed.")

