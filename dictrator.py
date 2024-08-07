# def catcherror(main):
#     def hello():
#         try:
#             main()
#         except Exception as err:
#             print(err)
#     return hello
def catcherror(func):
    def abc(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except Exception as err:
            print(err)
    return abc

@catcherror
def divide(a,b):
    z=a/b
    print(z)
divide(5,0)
 
import time
 
def calculate_time(func):
    def inner1(*args,**kwargs):
        begin = time.time()
        func(*args,**kwargs)
        End = time.time()
        print("Total time taken in : ",func.__name__, End - begin)
    return inner1
 
@calculate_time
def divide(a,b):
    time.sleep(5)
    z=a/b
    print(z)
divide(45,89)


 
