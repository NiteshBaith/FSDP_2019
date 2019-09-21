# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:11:23 2019

@author: Baith
"""





from bs4 import BeautifulSoup
import urllib
url='https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area'
source = urllib.request.urlopen(url)

soup = BeautifulSoup(source,"lxml")

right_table=soup.find('table', class_='wikitable sortable')
print (right_table)

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 6:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        
for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==7:
        A.append(cells[1].text.strip())
        B.append(cells[2].text.strip())
        C.append(cells[3].text.strip())
        D.append(cells[4].text.strip())
        E.append(cells[5].text.strip())
A.pop()
B.pop()
C.pop()
D.pop()
E.pop()

import pandas as pd
from collections import OrderedDict

column=[ "State / Territory","Area (km2)",	'Region',	'National Share (%)',	'Country of comparable size (land mass)']
col_data=OrderedDict(zip(column,[A,B,C,D,E]))

df=pd.DataFrame(col_data)
df.to_csv("dataset of Inida")

ind=df['State / Territory'].tolist()
values=df['National Share (%)'].tolist()
newdatafram=pd.DataFrame({'Nation Share':values},index=ind)

import matplotlib.pyplot as plt
newdatafram.plot.pie(subplots=True)

df['National Share (%)'] = pd.to_numeric(df['National Share (%)'])
new_df=df.iloc[0:6]

# Create a pie chart
plt.pie(
    
    new_df['National Share (%)'],
  
    labels=new_df['State / Territory'],
    # with no shadows
    shadow=False,

    # with one slide exploded out
    explode=(0.1, 0, 0, 0, 0,0),
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction
    autopct='%1.1f%%',
    )

