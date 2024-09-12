from django.shortcuts import render
from django.conf import settings
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request
import urllib.parse

from urllib.error import HTTPError


# Create your views here.
def index(request): 

    data = {} # default data value 
    
    if request.method == 'POST': 
    
        city = request.POST['city'] 
        if city == "":
            return render(request, "main/index.html", data)
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
        
        # source contain JSON data from API 
        url_base = 'http://api.openweathermap.org/data/2.5/weather?'
        params = {
            'q': city,
            'appid': settings.OPENWEATHER_API_KEY,
        }
        url = url_base + urllib.parse.urlencode(params)
        
        # using try catch to avoid hhtp exception        
        try:
            source = urllib.request.urlopen(url=url).read()
        except HTTPError:
            return render(request, "main/index.html", data) 

        # print(source)
        # print(source.getcode())
        if source.getcode() == 404:
            return render(request, "main/index.html", data)

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

    return render(request, "main/index.html", data)
