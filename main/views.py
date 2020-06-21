from django.shortcuts import render
import requests
import configparser
import sys
import datetime
def get_weather(api_key, zipcode, country):
    url = "http://api.openweathermap.org/data/2.5/weather?zip={},{}&units=metric&appid={}".format(zipcode, country, api_key)
    r = requests.get(url)
    return r.json()
 
def home(request):
    return render(request, 'home.html')
def new(request):
    print(request.method)
    if request.method == "POST":
        api_key = 'yourkeyhere'
        zipcode = request.POST['zip']
        country = request.POST['country']
        weather = get_weather(api_key, zipcode, country)
        context={}
        context['temp_min']=str(weather['main']['temp_min'])
        context['temp_max']=str(weather['main']['temp_max'])
        context['name']=str(weather['name'])
        sunriseint = datetime.datetime.fromtimestamp(int(weather['sys']['sunrise'])).strftime('%Y-%m-%d %H:%M:%S')
        sunsetint = datetime.datetime.fromtimestamp(int(weather['sys']['sunset'])).strftime('%Y-%m-%d %H:%M:%S')
        context['sunrise']=str(sunriseint)
        context['sunset']=str(sunsetint)
        return render(request, 'weather.html', context)
    else:
        return redirect("/")