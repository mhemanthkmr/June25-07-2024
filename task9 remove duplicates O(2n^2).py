# task 9 remove duplicates from the list without using set

list2=[1,2,3,1,1,3,3,2,4,5,6,2,]
without_duplicates=[]
for i in range(len(list2)):
    if list2[i]==list2[i] in list2 and list2[i] not in without_duplicates:
        without_duplicates.append(list2[i])

print(without_duplicates)