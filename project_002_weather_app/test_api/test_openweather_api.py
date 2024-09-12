import os
import urllib
import urllib.parse
import urllib.request
import json

from dotenv import load_dotenv


load_dotenv("../weather/.env")


OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')


def test_api(city):
    url_base = 'http://api.openweathermap.org/data/2.5/weather?'
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
    }
    url = url_base + urllib.parse.urlencode(params)
    print(url)
    source = urllib.request.urlopen(url=url).read() 

    # converting JSON data to a dictionary 
    list_of_data = json.loads(source)

    # data for variable list_of_data 
    data = { 
        "country_code": str(list_of_data['sys']['country']), 
        "coordinate": str(list_of_data['coord']['lon']) + ' '
                    + str(list_of_data['coord']['lat']), 
        "temp": str(list_of_data['main']['temp']) + 'k', 
        "pressure": str(list_of_data['main']['pressure']), 
        "humidity": str(list_of_data['main']['humidity']), 
    } 
    print(data) 


test_api('524901')
