# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:27:37 2019

@author: Baith
"""
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import requests
import urllib

#specify the url
url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(url).text
#or
source = urllib.request.urlopen(url)

soup = BeautifulSoup(source,"lxml")



all_tables=soup.find_all('table')



right_table=soup.find('table', class_='table')

print (right_table)

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]


for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        
from collections import OrderedDict

col_name = ["Position","Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))

import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("ODI.csv")