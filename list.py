# Initial list of monthly expenses
expenses = [2200, 2350, 2600, 2130, 2190]

# 1. Extra dollars spent in February compared to January
extra_february = expenses[1] - expenses[0]
print(f"Extra dollars spent in February compared to January: {extra_february}")

# 2. Total expense in the first quarter (first three months)
total_first_quarter = sum(expenses[:3])
print(f"Total expense in the first quarter: {total_first_quarter}")

# 3. Check if you spent exactly 2000 dollars in any month
spent_2000 = 2000 in expenses
print(f"Spent exactly 2000 dollars in any month: {spent_2000}")

# 4. Add June expenses
expenses.append(1980)
print(f"Expenses after adding June: {expenses}")

# 5. Refund correction for April
expenses[3] -= 200
print(f"Expenses after refund correction for April: {expenses}")