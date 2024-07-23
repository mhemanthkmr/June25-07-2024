n=153
temp=153
sum=0
while(n!=0):
    lastvalue=n % 10
    sum+=lastvalue**3
    n=n//10
if(sum==temp):
    print("Armstromg number")
else:
    print("Not a Armstrong")