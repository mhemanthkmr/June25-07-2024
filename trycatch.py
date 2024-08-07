import time
import math

def calculate_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in :", func.__name__, end - begin)
    return inner1

def catchError(main):
    def inner(*args, **kwargs):
        try:
            main(*args, **kwargs)
        except Exception as err:
            print(err)
    return inner
@calculate_time
@catchError
def divide(a,b):
    time.sleep(2)
    z=a/b
    print(z)
divide(5,2)