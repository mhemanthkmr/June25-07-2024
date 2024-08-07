import os
from langchain_community.utilities import OpenWeatherMapAPIWrapper
os.environ['OPENWEATHERMAP_API_KEY'] = "c2aef44761586b94368ca465ae9c6f98"
weather=OpenWeatherMapAPIWrapper()
Location = input("Enter the Location:")
result = weather.run(Location)
print(result)