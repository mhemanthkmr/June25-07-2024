india = ['mumbai','bangalore','chennai','delhi']
pakistan =['lahore','karachi','islamabad']
bangledesh =['delhi','khulna','rangpur']
city =input('enter your city name:')
if (city in india):
  print('city belongs to india:')
elif(city in pakistan):
 print('city belongs to pakistan:')
elif (city in bangledesh):
  print('city belongs to bangledesh:')
else:
 print('no country found')