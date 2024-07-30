#openweathermap.org/api, langchain,-->api-->key
import os
from langchain_community.utilities import openWeatherMapAPIWrapper
os.environ["OPENWEATHERMAP_API_KEY"]= "718c3755bfb63c110e57e14e90a24636"
weather = openWeatherMapAPIWrapper()
result = weather.run("chennai")
print(result)