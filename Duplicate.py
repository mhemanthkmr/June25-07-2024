# Demo_list =[12,22,12,34,45,34,56]
# duplicates = {x for x in Demo_list if Demo_list.count(x)>1}
# print('duplicates',duplicates)

list1 =[1,2,3,2,4,5,4,6,7]
list2 =[]
for i in list1:
 if i not in list2:
  list2.append(i)
 else:
  print(i)