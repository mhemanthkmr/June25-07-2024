expense=[2200,2350,2600,2130,2190]

extra_spent=expense[1]-expense[0]
print(extra_spent)

extra_quarter=expense[0]+expense[1]+expense[2]
print(extra_quarter)


print(2000 in expense)

expense.append(1980)
print(expense)

expense[3] += 200
print(expense)


heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
heros[3]='black panther'
print(heros)
heros[1:3]="doctor strange"
print(heros)