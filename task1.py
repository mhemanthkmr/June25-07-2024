#task 1
#formatted string 
#creating dictionaries:

dic1={'student':"eve",
      'score':98}
dic2={'student':"ini",
      'score':100}
dic3={'student':"mani",
      'score':76}
dic4={'student':"faiza",
      'score':65}

print(dic1)
join1=f"{dic1} scored{dic1}, {dic2} scored{dic2} ,{dic3} scored{dic3}" 
print(join1)
join2=((f"{dic1['student']} scored{dic1['score']} marks"),(f"{dic2['student']} scored{dic2['score']} marks"),
(f"{dic3['student']} scored{dic3['score']} marks"))
print(join2)
