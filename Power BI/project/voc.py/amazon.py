# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:45:26 2019

@author: praveen.kumawat
"""
import urllib
from selenium import webdriver
import time as tm
import json
import pandas as pd
from datetime import date, timedelta


def live_data_fatch():
    l=0
    data = []
    for i in range(0,15):
        if not l:
            try:
                url = "https://www.amazon.com/sp/ajax/feedback?seller=ADZH7GRDFE99Y&marketplaceID=ATVPDKIKX0DER&pageNumber="+str(i)+""
                """    
                hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
                url = "https://www.amazon.com/sp/ajax/feedback?seller=ADZH7GRDFE99Y&marketplaceID=ATVPDKIKX0DER&pageNumber="+str(i)+""
                """
                print(i)
                tm.sleep(5)
                response = urllib.request.urlopen(url)
                data.append(json.loads(response.read()))
                for k in range(0,len(data)):
                    for j in range(0,len(data[k]['details'])):
                        if data[k]['details'][j]['ratingData']['date'] == 'March 25, 2019':  #Replace the Date upto where data is needed
                            l = 1
            except urllib.error.HTTPError:
                print('try again '+str(i)+"")
                tm.sleep(10)
                
                continue
        else:
            break
        
    rater_name = []
    rating = []
    feedback = []
    date = []
    for i in range(0,len(data)):
        for j in range(0,len(data[i]['details'])):
            if pd.to_datetime(data[i]['details'][j]['ratingData']['date']) >= pd.to_datetime('March 25, 2019'): 
                rater_name.append(data[i]['details'][j]['rater'])
                rating.append(data[i]['details'][j]['rating'])
                feedback.append(data[i]['details'][j]['ratingData']['text']['expandedText'])
                date.append(data[i]['details'][j]['ratingData']['date'])
    dataset = pd.DataFrame()
    dataset["rating"] = rating
    dataset["rater"] = rater_name
    dataset["date"] = date
    dataset["review"] = feedback
    
    dataset["date"]=pd.to_datetime(dataset['date'])
    return dataset


import pyodbc
data1=live_data_fatch()
yesterday = date.today() - timedelta(days=1)
dataset1=data1[data1['date']==yesterday.strftime('%Y-%m-%d 00:00:00')]
conn = pyodbc.connect(
                    )
cursor = conn.cursor()

for index,row in dataset1.iterrows():
    cursor.execute("INSERT INTO [dbo].[Amazon_Reviews]([rating],[rater],[date],[review]) values (?,?,?,?)", 
                   row['rating'],
                   row['rater'],
                   row['date'],
                   row['review']
                   )
    conn.commit()
cursor.close()
conn.close()
