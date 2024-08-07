while True :
    print(""" Hi Welcome to Weather App
          please choose a options in a given below :
            1. Weather App
            2. Exit 
          """)

    choice = int(input("Enter a option no : "))

    if choice == 1 :
        import os
        from langchain_community.utilities import OpenWeatherMapAPIWrapper
        os.environ['OPENWEATHERMAP_API_KEY'] = "c2aef44761586b94368ca465ae9c6f98"
        weather = OpenWeatherMapAPIWrapper()
        location = input("Enter a location : ")
        result = weather.run(location)
        print(result)

    elif choice == 2 :
        print("Your progress executed successfully. Thank You")
        break

    else :
        print("Invalid Option Number")