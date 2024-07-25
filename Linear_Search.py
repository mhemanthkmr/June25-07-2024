# linear search
# arr=[9,1,2,3,4,5,6,7,8]
# n=int(input("enter the value to search"))
# for i in arr:
#     if i==n:
#         print("record found")
#         break
#     else:
#         print("record not found")

#bineray search

arr=[2,5,8,12,16,23,38,56,72,91]
n=int(input(Enter the target number))
low=0
high=len(arr)
while(low<=high)//2:
 if(arr[mid]==n):
  print("value found")
  break
 elif(arr[mid]>n):
  high =mid-1;
print("high")
else:
low = mid+1;
print("low")