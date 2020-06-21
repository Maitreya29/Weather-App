import configparser
import requests
import sys
 
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']
 
def get_weather(api_key, location, country):
    url = "http://api.openweathermap.org/data/2.5/weather?zip={},{}&units=metric&appid={}".format(location, country, api_key)
    r = requests.get(url)
    return r.json()
 
def main():
    
    location = str(input("Enter Zip:"))
    country = str(input("Enter Country Code:"))
    api_key = get_api_key()
    weather = get_weather(api_key, location, country)
    temp_min=str(weather['main']['temp_min'])
    temp_max=str(weather['main']['temp_max'])
    print("min:"+temp_min+" max"+temp_max)
 
 
if __name__ == '__main__':
    main()