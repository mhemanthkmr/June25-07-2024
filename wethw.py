import os
from langchain_community.utilities import OpenWeatherMapAPIWrapper
os.environ["OPENWEATHERMAP_API_KEY"]="a7708f9d88d41e367c132b1b500c37f9"
weather = OpenWeatherMapAPIWrapper()
result=weather.run('ooty')
print(result)
