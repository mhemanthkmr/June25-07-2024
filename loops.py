india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter a city name: ")

if city in india or city in pakistan or city in bangladesh:
    if(city in india):
        print(f'{city}, belongs to india')
    else:
        if(city in pakistan):
            print(f'{city},belongs to pakistan')
        else:
            if(city in bangladesh):
                print(f'{city},belongs to bangaladesh')
else:
    print(f'{city},not belongs to india,pakistan,and bangladesh')
