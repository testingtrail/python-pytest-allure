import inspect

#CONSTANTS

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"

#FUNCTIONS
def whoami():
    return inspect.stack()[1][3]