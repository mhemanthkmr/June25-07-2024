from threading import Thread
import time

def fun1():
    time.sleep(5)
    print("Hello World")

def fun2():
    time.sleep(5)
    print("Hello World")

t1 = Thread(target=fun1)
t2 = Thread(target=fun2)

t1.start()
t2.start()