# binary search
arr=[2,5,8,12,16,23,38,56,72,91]
n=int(input("Enter the target to seach:"))
low=0
high=len(arr)

while(low <=high):
    mid=(low+high)//2
    if(arr[mid]== n):
        print("value found")
        break
    elif(arr[mid]>n):
        high=mid-1;
    else:
        low=mid+1;
