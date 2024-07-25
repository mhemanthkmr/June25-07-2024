# n=153
# temp=153
# sum=0

# while(n!=0):
#   last_name = n%10
#   sum += last_name ** 3
#   n = n//10
 # if (sum == temp):
#   print('Armstrong Number')
# else:
#   print('Not an Armstrong Number')

n=7777
temp=n
sum=0
index =0
while(n!=0):
  last_name = n%10
  sum += last_name ** 4
  n = n//10
 
 
if (sum == temp):
  print('Armstrong Number')
  
else:
  print('Not an Armstrong Number')

