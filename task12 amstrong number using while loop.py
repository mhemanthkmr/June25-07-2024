#task 12 amstrong number using while loop

B=int(input("Enter the number:"))
temp1=B
print(B)
digit=0

while(temp1!=0):
    temp1=temp1//10
    digit+=1
print(f"{B} is a {digit} digit number")

temp2=B
sum=0
while(temp2!=0):
    last=temp2%10
    sum+=last**digit
    temp2//=10
if(sum==B):
    print(f"{B} is a amstrong number")
else:
    print(f"{B} is not a amstrong number")

