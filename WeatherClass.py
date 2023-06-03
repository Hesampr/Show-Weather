# A library we need to receive weather data 
import requests


# An API KEY I received from weatherstack.com (it's a free website)
Api_Key = '4cd467403fcb8ed14a34dae13af4a37f'

Base_Url = f"http://api.weatherstack.com/current?access_key={Api_Key}"


# Weather receiver function 
def Weather(city):
    
    Url = f"{Base_Url}&query={city}"
    try : 
        Response = requests.get(Url).json()

        General_Weather = Response['current']['weather_descriptions']
        
        Today_feelslike = Response['current']['feelslike']

        return General_Weather[0],Today_feelslike
    except: 
        pass 

