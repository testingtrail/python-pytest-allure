import inspect

#CONSTANTS

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"

#FUNCTIONS

#function to get the name of current function being used
def whoami():
    return inspect.stack()[1][3]