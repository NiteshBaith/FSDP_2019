# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:42:38 2019

@author: praveen.kumawat
"""

from  selenium import webdriver
from bs4 import BeautifulSoup as BS
import time as tm
import pandas as pd
from datetime import date, timedelta
import pyodbc
import time
"""
url = "https://www.google.com/shopping/customerreviews/merchantreviews?q=shoplc.com"
browser = webdriver.Chrome("C:/Users/admin-14/Downloads/chromedriver_win32/chromedriver.exe")
browser.get(url)
"""

def live_data_fatch():
    stars=[]  
    review=[]
    date_1=[]
    url = "https://www.google.com/shopping/customerreviews/merchantreviews?q=shoplc.com"
    browser = webdriver.Chrome(executable_path ="C:/Users/praveen.kumawat/Downloads/chromedriver_win32/chromedriver.exe")
    browser.get(url)

    for j in range(0,10):
        html_page = browser.page_source
        soup = BS(html_page)
        all_tables = soup.find_all(class_ = 'SzAWKe')
        tm.sleep(1)    
        for i in all_tables:        
            stars.append(int(i.find(class_ = 'ujLN8e').attrs['style'].split(':')[1].strip().split('%')[0])//20)
            try:
                review.append((i.find(attrs={'style': 'margin-top:6px'})).text.strip())
            except AttributeError:
                review.append(None)
            date_1.append((i.find(class_ = 'CfOeR')).contents[0].split('on')[1].strip())
            
        next_click = browser.find_element_by_class_name("VfPpkd-Jh9lGc")
        next_click.click()
    dataset = pd.DataFrame()
    dataset["Stars_Rating"] = stars
    dataset["Review"] = review
    dataset["Date"] = date_1
    dataset["Date"]=pd.to_datetime(dataset['Date'])
    browser.quit()
    return dataset
    
data1=live_data_fatch()
yesterday = date.today() - timedelta(days=1)
dataset1=data1[data1['Date']==yesterday.strftime('%Y-%m-%d 00:00:00')]

"""
yesterday.strftime('%Y-%m-%d 00:00:00')
"""

while True: 
    data1=live_data_fatch()
    yesterday = date.today() - timedelta(days=1)
    dataset1=data1[data1['Date']==yesterday.strftime('%Y-%m-%d 00:00:00')]
    
    conn = pyodbc.connect(
                        )
    
    cursor = conn.cursor()
    
    for index,row in dataset1.iterrows():
        cursor.execute("INSERT INTO [dbo].[Google_Trust_Reviews]([Stars_Rating],[Review],[Date]) values (?, ?,?)", 
                       row['Stars_Rating'],
                       row['Review'],
                       row['Date']
                       )
        conn.commit()
    cursor.close()
    conn.close()

    
