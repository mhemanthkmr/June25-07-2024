# task 1
# formatted string

 
student1={
       'Name' :"ramsaran",
        'Marks':90
}
student2={
        'Name' :'john',
        'Marks': 88
}
student3={
        'Name' :'antony',
        'Marks': 70
}
student4={
        'Name' :'Sarathy',
        'Marks': 100
}

Students=[student1,student2,student3,student4]

for i in Students:
 print(f"{i['Name']} scored {i['Marks']} marks ")
