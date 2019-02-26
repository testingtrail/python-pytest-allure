# PythonAutomationFramework
This is a project for a web automation framework using Selenium, Python, allure reports and page object model. This automates the free demo HRM https://opensource-demo.orangehrmlive.com/.

# How to install it
* Make sure you have python installed on your machine by typing in console "python --version" if not go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.
* Clone the repository to any local path.
* Note: This has been created using Python environment in order to have all dependencies in the same folder rather than taking the packages for the global python configuration. If you wish to clone without env folder you have to download following python packages by running following pip commands:
  - pip install selenium (for webdriver)
  - pip install pytest (for pytest framework)
  - pip install pytest-html (for pytest html report)
  - pip install allure-pytest (for allure reporting)
  - pip install moment (for time functions)
  - pip install webdriver_manager ](for web driver download without need of .exe)

# How to run it
enter the following command in cmd being located in the folder path
  - python -m pytest 
* Optional parameters
  - --html=reports/report1.html For Pytest html reporting
  - --self-contained-html For having Pytest html report with inline CSS
  - --browser <firefox, chrome> To choose different browser, default is chrome
  - --alluredir=<path> To create files needed for allure reports, run this every time your code changes
    or new funtionality exists, in this case "alluredir=reports/allure-reports"
* To generate allure reports you need to type the following in the project path
  - allure serve <path where allure files are>, in this case "allure serve reports/allure-reports"

* Example: python -m pytest --alluredir=reports/allure-reports --browser=chrome
   

# Technologies used
* Python 3.
* Selenium Package.
* Chromedriver.exe and geckodriver.exe for Chrome and Firefox web drivers respectively.
* Pytest in order to have test cases, init and tear down.
