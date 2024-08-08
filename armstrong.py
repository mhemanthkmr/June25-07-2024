n=int(input(""))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum +=digit**3
    temp//=10
if(n==sum):
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")
    
