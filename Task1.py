""" 1. Let us say your expense for every month are listed below,
      1. January - 2200
      2. February - 2350
      3. March - 2600
      4. April - 2130
      5. May - 2190

    Create a list to store these monthly expenses and using that find out, """

monthlyexp = [{"January" : 2200}, {"February" : 2350}, {"March" : 2600}, {"April" : 2130}, {"May" : 2190}]

# 1. In Feb, how many dollars you spent extra compare to January?
january_exp = monthlyexp[0]["January"]
february_exp = monthlyexp[1]["February"]

extra_dollars = february_exp - january_exp

print("In February, you spent", extra_dollars,"extra dollars compared to January.")

# 2. Find out your total expense in first quarter (first three months) of the year.
january_exp = monthlyexp[0]["January"]
february_exp = monthlyexp[1]["February"]
march_exp = monthlyexp[2]["March"]

total_first_quarter = january_exp + february_exp + march_exp

print("The total expense in first quarter is",total_first_quarter,"dollars.")

# 3. Find out if you spent exactly 2000 dollars in any month.
spent_2000 = False
for month in monthlyexp:
    for expense in month.values():
        if expense == 2000:
            spent_2000 = True
            break

    if spent_2000:
        break

if spent_2000:
    print("Yes, you spent exactly 2000 dollars in a month.")

else:
    print("No, you did not spend exactly 2000 dollars in any month.")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list.
monthlyexp.append({"June" : 1980})
print(monthlyexp)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this.
for month in monthlyexp:
    if "April" in month:
        month["April"] -= 200
        break

print(monthlyexp)