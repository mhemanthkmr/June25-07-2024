import os
from decouple import config
from langchain_community.utilities import OpenWeatherMapAPIWrapper
os.environ['OPENWEATHERMAP_API_KEY']=api_key=config("API_KEY")
weather=OpenWeatherMapAPIWrapper()
location=input("enter the location:")
result = weather.run(location)
print(result)