#find armstrong number:

n=153
temp=153
sum=0
while (n!=0):
    last=n%10
    sum+=last**3
    n=n//10
if sum==temp:
    print('Armstrong')
else:
    print('not')
