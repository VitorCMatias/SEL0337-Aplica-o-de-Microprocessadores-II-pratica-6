#!/usr/bin/env python3

from requests import get
from pprint import pprint


weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

weather = weather + str(966583)
my_weather = get(weather).json()['items']

pprint(my_weather)
print('Temperatura no solo é: {}'.format(my_weather[0]['ground_temp']))
    




    