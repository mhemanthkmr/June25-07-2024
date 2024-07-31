# task  4
expenses=[2200,2350,2600,2130,2190]
feb_extra_expense=expenses[1]-expenses[0]
print(f"In february ${feb_extra_expense} spent extra than january")
total_expense_in_first_quarter=0
for i in range(0,3):
    total_expense_in_first_quarter+=expenses[i]


print(f"The amount of ${total_expense_in_first_quarter} is spend during first quarter")

if(2000 in expenses):
  print("yes i spent exactly $2000")
else:
 print("No i didn't spent exactly $2000")

expenses.append(1980)
print(expenses)

expenses[3]+=200

print(expenses)
