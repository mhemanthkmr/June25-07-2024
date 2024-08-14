def printpattern(num):
    for i  in range(1,num + 1):
        print(" ")
        for j in range(1,i+1):
            print(end="*")
            
            
num=int(input("enter the num value:"))  
printpattern(num)         