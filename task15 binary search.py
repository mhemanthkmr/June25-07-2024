#task 15 binary search
binary_list=[2,5,8,12,16,23,38,56,72,91]
binary_list.sort()
print(binary_list)
High=len(binary_list)-1
low=0

#print(High)
search_element=int(input("Enter the number:"))

while(low<=High):
    mid=(low+High)//2
    if( binary_list[mid]==search_element):
        print("Value found")
        break
    elif binary_list[mid]>search_element:
        High=mid-1
    else:
        low=mid+1