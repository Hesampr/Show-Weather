
import requests
from datetime import datetime


Api_Key = '4cd467403fcb8ed14a34dae13af4a37f'
Base_Url = f"http://api.weatherstack.com/current?access_key={Api_Key}"

def to_celsius(temperature):
    return temperature - 273

City = "ramsar"
# City = input()

Url = f"{Base_Url}&query={City}"

Response = requests.get(Url).json()

General_Weather = Response['current']['weather_descriptions']
Today_temperature = to_celsius(Response['current']['temperature'])
Today_feelslike = Response['current']['feelslike']

print(General_Weather)
print(Today_temperature)
print(Today_feelslike)
