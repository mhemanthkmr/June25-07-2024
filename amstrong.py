#amstrong using modulus
n=153
sum=0
temp=153
while(n!=0):
    last=n%10
    sum+=last **3
    n=n//10
if(sum==temp):
    print("amstrong")
else:
    print("not an amstrong")
#indexing
n=153
temp=153
sum=0
index=123
while(n!=0):
    last =n%10
    sum+=last **index
    n=n//10
if(sum==temp):
    print("amstrong")
else:
    print("not an amstrong")

