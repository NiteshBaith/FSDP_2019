# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:12:12 2019

@author: Baith
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

import requests

url1 = "http://free.currencyconverterapi.com/api/v5/convert?q="
url2=input("Enter Formate like USD_INR,USD_EURO  :->")
f,l=url2.split("_")
url2="{}".format(url2)

 
# the app id is unique for a particular person so pasted munish's appid
url3 = "&apiKey=801b5f755c8c7d045de1"
url = url1 + url2 + url3

#taking Api From the site using url
response=requests.get(url)

#getting data of API
respo_cont=response.content

# Checkin Content wheter is in binary form
print ("Status code: " + str(response.status_code))

#json() function to get the data converted to python data type (dict)
json_data = response.json()
#checking type (str(type(jsondata)))
#print (type(json_data))
convtd=json_data["results"]["{}".format(url2)]["val"]
print("Value of {} is equal to 1{} :".format(f,l),convtd)