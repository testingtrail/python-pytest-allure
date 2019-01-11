import inspect

# functions
def whoami():
    return inspect.stack()[1][3]

def MyFunc():
    x = whoami()
    print(x)

MyFunc()