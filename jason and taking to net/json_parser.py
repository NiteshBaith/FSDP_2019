# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:03:58 2019

@author: Baith
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

# Printing temp using API

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2=input("Enter city name :")
url2 = "?q={}".format(url2)  # Putting city name at ? query string
 
# the app id is unique for a particular person so pasted munish's appid
url3 = "&appid=8573b478c87b6c6258bb3a4cefa99666"
url = url1 + url2 + url3

#taking Api From the site using url
response=requests.get(url)

#getting data of API
respo_cont=response.content

# Checkin Content wheter is in binary form
print (type(response.content))
print ("Status code: " + str(response.status_code))

#json() function to get the data converted to python data type (dict)
json_data = response.json()
#checking type (str(type(jsondata)))
#print (type(json_data))


import datetime #converting epoch unix to readabel date and time
sunrise=datetime.datetime.fromtimestamp(json_data["sys"]["sunrise"]).strftime('%c')
sunset=datetime.datetime.fromtimestamp(json_data["sys"]["sunset"]).strftime('%c')
F=json_data["main"]["temp"]
print("Temperatue in celcius is: ",round(F-273,2))
print("Latitude and longitude are:{},{}".format(json_data["coord"]["lon"],json_data["coord"]["lat"]))
print("Weather condition is :",json_data["weather"][0]["description"])
print("Wind speed is {}m/s".format(json_data["wind"]["speed"]))
print("sun rise tinme {} and sunset time {}".format(sunrise,sunset))









