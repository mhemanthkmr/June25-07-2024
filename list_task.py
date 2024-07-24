monthly_exp={
    "Jan":2200,
    "Feb":2350,
    "March":2600,
    "April":2130,
    "May":2190}
extra_exp=monthly_exp["Feb"]-monthly_exp["Jan"]
print(f"Dollars spent extra compare to JAN is Rs: {extra_exp}")
print()

f_quarter_exp=2200+2350+2600
print(f"Total expense in first quarter is Rs: {f_quarter_exp} of the year")
print()
print("yes, Rs:2000 is spent for the month ")if monthly_exp==2000 else print("no, Rs.2000 is Not spent for any month")
print()
June_exp=1980
monthly_exp["June"]=June_exp
print(f"June month expense Rs.{June_exp}, is added in the monthly expense list" )
for month,amount in monthly_exp.items():
    print(f"{month}:{amount}")
print()
monthly_exp=monthly_exp["April"]-200
print(f"Updated  April month expense is {monthly_exp}")
print()
print()

#2 
heros=['spinder man','thor','hulk','iron man','captain america']
#len of the list
print(f"Length of the list: {len(heros)}")
# add BLACK PANTHER at the end of the list
heros.append("black panther")
print(heros)
print()
# Remove BLACK PANTHER and add after HULK
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)
print()
#Remove THOR and HULK, Replace DOCTOR STRANGE
del heros[1:3]
heros.insert(1,"doctor strange")
print(heros)
print()