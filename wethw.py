import os
from langchain_community.utilities import OpenWeatherMapAPIWrapper
os.environ["OPENWEATHERMAP_API_KEY"]= api_key=("AI2_key")
weather = OpenWeatherMapAPIWrapper()
location = input("enter the location : ")
result=weather.run(location)
print(result)
