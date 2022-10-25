from django.shortcuts import render
import urllib.request
import json
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=b4f590963057e97c3fdc903210b1b57e').read()
        list_data = json.loads(source)

        data = {
            "country_code": str(list_data['sys']['country']),
            "coordinate": str(list_data['coord']['lon']) + ', ' + str(list_data['coord']['lat']),
            "temp": str(list_data['main']['temp']),
            "pressure": str(list_data['main']['pressure']),
            "humidity": str(list_data['main']['humidity']),
            "main": str(list_data['weather'][0]['main']),
            "description": str(list_data['weather'][0]['description']),
            "icon": str(list_data['weather'][0]['icon']),
        }
        # print(data)
    else:
        data = {}
        
    return render(request, 'home.html', data)

