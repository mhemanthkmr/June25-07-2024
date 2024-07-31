import os
from langchain_community.utilities import OpenWeatherMapWrapper
os.environ["OPEN_WEATHERMAP _API_KEY"]="a7708f9d88d41e367c132b1b500c37f9"
weather = OpenWeatherMapWrapper(api_key=os.environ["OPEN_WEATHERMAP_API_KEY"])
result=weather.run('ooty')
print(result)

N73LVTNQYUSIHJW3