from citipy import citipy
import requests as r
import numpy as np
import json
import time
import matplotlib.pyplot as plt
from random import random, randint
import openweathermapy as ow
import pandas as pd

api_key = 'fd006e30478a34e544f081897dd4111c'
url = "http://api.openweathermap.org/data/2.5/weather?"
units = 'metrics'

query_url = url + 'appid=' + api_key + '&units=' + units + '&q='

random_cities = 500
lat_base = [((np.random.randint(-90, 90))) for _ in range (random_cities)]
long_base = [((np.random.randint(-180, 180))) for _ in range (random_cities)]
lat_long = tuple(zip(lat_base, long_base))

weather_data = []
cities = []
country = []

for lat,lon in lat_long:
    city = citipy.nearest_city(lat,lon)
    city_N = city.city_name
    cities.append(city_N)
    country.append(city.country_code)
    response = r.get(query_url + city_N).json()
    weather_data.append(response)

weather_df = pd.DataFrame({'Cities': cities,
              'Country': country, 'Latitude': lat_base, 'Longitude': long_base })
weather_df.tail()

tempature = []
humidity = []
cloudiness = []
wind_speed = []
for city in cities:
    weather_response = r.get(query_url + city_N).json()
    try:
        tempature.append(weather_response['main']['temp'])
        humidity.append(weather_response['main']['humidity'])
        cloudiness.append(weather_response['clouds']['all'])
        wind_speed.append(weather_response['wind']['speed'])
    except:
        print("Skipping")

plotting_data = pd.DataFrame({"Temp": tempature, "Humidity": humidity, "Cdiness": cloudiness, "Speed of Wind": wind_speed})

plt.scatter(weather_data["lon"], weather_data["pressure"], marker="o")

plt.title("Temperature in World Cities")
plt.ylabel("TemperaturE")
plt.xlabel("Latitude")
plt.show()