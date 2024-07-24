# find the max using conditions
# lst=[1,2,3,4,5]
# maxi=lst[0]
# for i in lst:
#     if maxi<i:
#         maxi=i
# print(maxi)
# find the duplicate in the list element
# lst=[1,2,3,4,5,2,5,0,1,0]
# fdup= {i for i in lst if lst.count(i)>1}
# print(fdup)

# remove the duplicate without using set
# lst=[1,2,3,4,5,2,5,0,1,0]
# rdup=[] 
# [rdup.append(x) for x in lst if x not in rdup]
# print(rdup)

# linear search the element
# lst=[1,2,3,4,5,2,5,0,1,0]
# svalue=int(input("Enter the value to search: "))
# for i in lst:
#     if i==svalue:
#         print("Value Found")
#         break
#     else:
#         print("Value not found")


# Bineary search
bsearch=[2,4,6,2,8,6,9,23,54,76,12]
target_search=int(input("Enter the value to search: "))
low=0
high=len(bsearch)
while (low<high):
    

# amstrong number
# n=999
# temp=n
# sum=0
# while (n!=0):
#     lastvalue=n%10
#     sum+=lastvalue**3
#     n=n//10
# if sum==temp:
#     print(f"{sum} is an Amstrong number")
# else:
#     print(f"{sum} is not an Amstrong number")
