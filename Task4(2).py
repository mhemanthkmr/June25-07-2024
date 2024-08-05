#bmi
weight=int(input())
height=int(input())
a=weight/height
if a<35:
    print("underweight")
elif a>=40:
    print("average")
else :
    print("obesity")


