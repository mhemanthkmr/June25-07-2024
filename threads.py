from threading import Thread
import time 

def model1():
    time.sleep(4)
    print("My heaven")

def model2():
    time.sleep(5)
    print("your object")

t1 = Thread(target= model1)
t2 = Thread(target= model2)

t1.start()
t2.start()
