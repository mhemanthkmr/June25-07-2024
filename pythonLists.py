expenses = {
    'January': 2200,
    'February': 2350,
    'March': 2600,
    'April': 2130,
    'May': 2190
}

januaryExpense = expenses['January']
februaryExpense = expenses['February']
marchExpense = expenses['March']
aprilExpense = expenses['April']
mayExpense = expenses['May']
expenses['June'] = 1980

extraSpentInFebruary = (februaryExpense - januaryExpense)
firstQuarterMonthExpenses = (januaryExpense + februaryExpense + marchExpense)

print(f"The extra amount spent in February compared to January is: ${extraSpentInFebruary}")
print(f"The first quarter month expenses is ${firstQuarterMonthExpenses}")
print("Comparing 2000 dollars spent in any month is:", 2000 in expenses)
expenses['April'] += 200
print(expenses)