#fibonicci series

n=int(input("Enter any number:"))
if n<=0:
    print("please enter number > 0:")
else:
    n1,n2=0,1
    for i in range(0,n):
        print(n1,end=" ")
        n1,n2=n2,n1+n2


#odd and even no.

n=int(input("Enter the number:"))
if(n%2==0):
    print(f"{n} is a even number")
else:
    print(f"{n} is a odd number")
        


    
 




