# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:22:53 2019

@author: Baith
"""

"""
Code Challenge
  Name:
    SSA Analysis
  Filename:
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available
    data on the frequency of baby names from 1880 through the 2010.
    (Use Baby_Names.zip from Resources)  
   
    Read data from all the year files starting from 1880 to 2010,
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""

import pandas as pd
import os
import csv
col=['Name','Gender','Year']

"""li=[]
for each in os.listdir("."):
    if 'txt' in each:
        # Printing  a specific column    
        with open(each) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            df =pd.DataFrame(csv_reader,columns=col)
            li.append(df)
frame=pd.concat(li)
print(frame['Year']=frame[frame['Year']>2010])
"""
#the above code is for fast machine
n=pd.DataFrame()
new_dataf=pd.DataFrame()
for each in os.listdir("."):
    if 'txt' in each:
        # Printing  a specific column    
        with open(each) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            data=pd.DataFrame(csv_reader,columns=col)
            #Run loop 2 times ,first time 49 to 55 then 49to 56
            n['{}'.format(each[3:7])]=data['Name'] +" "+ data['Gender'] +" "+ data['Year']
#displaying first five male female rows
i=0
j=0
for item in n['2010'].values:
    if ' F ' in item:
        i=i+1
        print(item)
        if i==5:
            break
for item in n['2010'].values:
    if ' M ' in item:
        j=j+1
        print(item)
        if j==5:
            break
#fastermethod
print(n['2010'][0:5].head())
print(n['2010'][n['2010'].str.find(" M ")[:]>0].head())

h=data.head()
data['Year']=pd.to_numeric(data['Year'])

# Calculate sum of the births column by sex as the total number of births
#in that year(use pandas pivot_table method)
data.groupby('Gender')['Year'].sum()
#pivot table method
sex_data=data.pivot_table(index='Gender',values='Year',aggfunc='sum')

sex_data.plot.bar()
            
            

                