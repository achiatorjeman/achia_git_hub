from flask import Flask, render_template, request
from datetime import datetime
import pytz
import json
import urllib.request
from requests import get
                                                                                                                                                                    
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def render_results1():
    api_key = 'd0a1e61ed2a7dcb5789a0595f3d62b53'
    city = request.form['city']

    list_api = 'http://api.openweathermap.org/' \
              'data/2.5/weather?q={}&appid={}'.format(city, api_key)

    source = get(list_api)


    list_of_data = source.json()
    if list_of_data['cod'] == '404':
        return render_template('error.html')

    country = pytz.country_names[list_of_data['sys']['country']]

    lat = str(list_of_data['coord']['lat'])
    lon = str(list_of_data['coord']['lon'])

    data7 = get_weather_results(lat, lon, api_key)

    date = []
    temp_day = []
    temp_night = []
    humidity = []
    temp = 0
    for i in data7['daily']:
        temp = datetime.fromtimestamp(i['dt'])
        date.append(str(temp.date()))
        temp_day.append(i['temp']['day'])
        temp_night.append(i['temp']['night'])
        humidity.append(i['humidity'])




    return render_template('results.html',
                           location=city, temp_day=temp_day, country=country,
                           temp_night=temp_night, date=date, humidity=humidity)

def get_weather_results(lat, lon, api_key):
    #source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api_key)).read()
    # listapi ='http://api.openweathermap.org/' \
    #          'data/2.5/weather?q={}&appid={}'.format(city, api_key)
    #
    # source = get(listapi)
    # if source.status_code == 500:
    #     return None, None


    #list_of_data = dict(json.loads(source))
    # list_of_data = source.json()
    # country = pytz.country_names[list_of_data['sys']['country']]
    #
    # lat = str(list_of_data['coord']['lat'])
    # lon = str(list_of_data['coord']['lon'])
    part = 'hourly,current,alerts,minutely'
    source2 = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/onecall?lat=' + lat + '&lon=' + lon + '&units=metric' + '&exclude=' + part + '&appid=' + api_key).read()
    list_of_data2 = dict(json.loads(source2))
    return list_of_data2




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

