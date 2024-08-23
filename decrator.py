def catcherror(func):
    def abc(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except Exception as err:
            print(err)
    return abc
def divide(a,b):
    return a /b
divide(5,8)