sugarLevelInput = float(input("Please Enter the sugar level: "))

if sugarLevelInput > 80 and sugarLevelInput < 100:
    print("Sugar level is Normal")
elif sugarLevelInput > 100:
    print("Sugar level is High")
elif sugarLevelInput < 80:
    print("Sugar level is Low")
else:
    print("Default")
