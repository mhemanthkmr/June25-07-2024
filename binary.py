arr=[2,3,5,7,9,4,22,45,67,89,12,34,54,27]
n=int(input("enter the target number to search:"))
low=0
high=len(arr)
while(low<=high):
    mid=(low+high)//2
    if(arr[mid]==n):
        print("value found")
        print(mid)
        break
    elif(arr[mid]>n):
        high=mid-1
    else:
        low=mid+1