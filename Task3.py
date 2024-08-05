#Task 3
#expense for every month

list3=['January','February','March','April','May']
list4=[2200,2350,2600,2130,2190]
print(list3)
print(list4)
month=[(f"{list3[0]}= {list4[0]}"),(f"{list3[1]}= {list4[1]}"),(f"{list3[2]}= {list4[2]}"),
(f"{list3[3]}= {list4[3]}"),(f"{list3[4]}= {list4[4]}")]
print(month)
remaining=list4[0]-list4[1]
print(remaining)
remaining1=list4[0]+list4[1]+list4[2]
print(remaining1)
print(2000 in month)
list3.append ('june')
list4.append (1980)
print(list3)
print(list4)
month=[(f"{list3[0]}= {list4[0]}"),(f"{list3[1]}= {list4[1]}"),(f"{list3[2]}= {list4[2]}"),
(f"{list3[3]}= {list4[3]}"),(f"{list3[4]}= {list4[4]}"),f"{list3[5]}= {list4[5]}"]
print(month)
list4[3]+200
print(list4[3]+200)
list4 .remove(2130)
list4.insert(3,2330)

print(list4)
month=[(f"{list3[0]}= {list4[0]}"),(f"{list3[1]}= {list4[1]}"),(f"{list3[2]}= {list4[2]}"),
(f"{list3[3]}= {list4[3]}"),(f"{list3[4]}= {list4[4]}"),f"{list3[5]}= {list4[5]}"]
print(month)

#task 3
#favourite marvel super heros

list5=['spider man','thor','hulk','iron man','captain america']
print(list5)
print(len(list5))
list5.append('black panther')
print(list5)
list5.remove('black panther')
list5.insert(3,'black panther')
print(list5)
list5.remove('thor'),list5.remove('hulk'),list5.append('doctor strange')
print(list5)

#alternative solution:

heros=['spider man','thor','hulk','Iron man','captain america']
print(heros)
print(len(heros))
heros.insert(2,'black panther')
print(heros)
heros.remove('black panther')
print(heros)
heros.insert(2,'black panther')
print(heros)
heros.pop(1),heros.pop(2),heros.append('doctor strange')
print(heros)

