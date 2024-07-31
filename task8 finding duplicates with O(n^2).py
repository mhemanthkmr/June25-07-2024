# task 8 find duplicate elemnts in a list and store it in another list  "O(n^2)"

list1=[1,2,3,1,1,3,3,2,4,5,6,2,]
duplicates = []

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] == list1[j] and list1[i] not in duplicates:
            duplicates.append(list1[i])

print("Duplicates:", duplicates)