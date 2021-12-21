import pytz
from flask import Flask, render_template, request, url_for, flash, redirect
import configparser
import urllib.request
import pytz
import json
from datetime import datetime

def get_weather_results(city, api_key):
    city = 'london'
    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key).read()
    list_of_data = dict(json.loads(source))
    print(list_of_data)
    print(pytz.country_names[list_of_data['sys']['country']])


    lat = str(list_of_data['coord']['lat'])
    lon = str(list_of_data['coord']['lon'])
    part = 'hourly,current,alerts,minutely'
    source2 = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/onecall?lat=' + lat + '&lon=' + lon + '&exclude=' + part + '&appid=' + api_key).read()
    list_of_data2 = (json.loads(source2))
   # print(list_of_data2)
    # with open('json.json', 'w') as file:
    #     file.write(source2)



    # data = {
    #      "temp": str(list_of_data2['daily']['day']) + 'k',
    #    # "humidity": str(list_of_data2['']['humidity']),
    #     "cityname": str(city),
    # }
    j = 0
    date =[]
    temp_day = []
    temp_night = []
    humidity = []
    temp = 0
    for i in list_of_data2['daily']:
        temp = datetime.fromtimestamp(((i['dt']) - 32) * 5 / 9)
        date.append(str(temp.date()))
        temp_day.append(i['temp']['day'])
        temp_night.append(i['temp']['night'])
        humidity.append(i['humidity'])

    print("d", temp_day)







api_key = 'd0a1e61ed2a7dcb5789a0595f3d62b53'
get_weather_results('london', api_key)