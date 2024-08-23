#find duplicates:

row=[1,2,3,4,4,4,5,5,52,35,23,35,52]
print(row)
print(len(row))
myset=set(row)
print(myset)
print(len(myset))
if len(row)!=len(myset):
    print("Duplicates present ")
else:
    print("No duplicates")
