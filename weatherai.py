import os
from langchain_community.utilities import openWeatherAPIWrapper
os.environ ["OPEN.WAETHERMAP-APIKEY"]="5b9c00e833344df2f06a2de4dfab2cdb"
Weather=openWeatherAPIWrapper()
result=Weather.run("uttrapradesh")
print(result)
