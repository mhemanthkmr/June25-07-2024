salary=['January','February','march','april','may']
print(salary)
amount=[2200,2350,2600,2130,2190]
print(amount)
expo=[(f"{salary[0]} ={amount[0]}"),(f"{salary[1]}= {amount[1]}"),(f"{salary[2]}= {amount[2]}"),
(f"{salary[3]} ={amount[3]}"),(f"{salary[4]}= {amount[4]}")]
print(expo)
print(expo[0])
print(expo[1])
all=amount[0]-amount[1]
print(all)
all2=amount[0]+amount[1]+amount[2]
print(all2)
print(2000 in expo)
add=salary.append('june')
print(salary)
add=amount .append(1980)
print(amount)
expo=[(f"{salary[0]} ={amount[0]}"),(f"{salary[1]}= {amount[1]}"),(f"{salary[2]}= {amount[2]}"),
(f"{salary[3]} ={amount[3]}"),(f"{salary[4]}= {amount[4]}"),(f"{salary[5]}= {amount[5]}")]
print(expo)
add=amount.remove(2600) 
add=amount.insert(2,2800) 
print(amount)
expo=[(f"{salary[0]} ={amount[0]}"),(f"{salary[1]}= {amount[1]}"),(f"{salary[2]}= {amount[2]}"),
(f"{salary[3]} ={amount[3]}"),(f"{salary[4]}= {amount[4]}"),(f"{salary[5]}= {amount[5]}")]
print(expo)

 #list your favourite marvel heroes:

hero=['spider man','thor','hulk','ironman','captain america']
print(hero)
print(len(hero))
hero.append('black panther')
print(hero[1:3])
hero[1:3]=['docter strange']
print(hero)