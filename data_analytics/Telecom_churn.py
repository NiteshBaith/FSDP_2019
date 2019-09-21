# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:05:04 2019

@author: Baith
"""


"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    
To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght?
   Predict and print it
6. Predict a relation between the customer and customer care service that 
whether churned customer have shown their concern to inform the customer care 
service about their problem or not
7. In which area code the international plan is most availed?
"""
# Data Preeprocessing modules
import pandas as pd
import numpy as np

# Loading the dataset
# 2. Get the values from Price column into a numpy.ndarray
data = pd.read_csv("Telecom_churn.csv")

#1. Predict the count of Churned customer availing both voice mail plan and international plan schema
d=data[(data['international plan']=='yes') & (data['voice mail plan']=='yes')].index.tolist()
print("Predicted count of Churned customer availing both voice mail plan and international plan schema : ",len(d))

#2. Total charges for international calls made by churned and non-churned customer and visualize it
chrn_true=data[(data['total intl charge'] > 0) & (data['churn']== True )]['total intl charge'].sum()
chrn_false=data[(data['total intl charge'] > 0) & (data['churn']== False )]['total intl charge'].sum()

"""
Pie chart, where the slices will be ordered and plotted counter-clockwise:
"""

labels = 'Total charges of churned', 'Total charges of non-churned'
sizes = [chrn_true,chrn_false]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0)  # explode 1st slice

#plt.pie(sizes, labels=labels, autopct='%.0f%%')

# or
import matplotlib.pyplot as plt
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=90)


plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#3. Predict the state having highest night call minutes for churned customer
state_nigh_call=data[(data['churn']== True )][['total night calls','state']].max()

#4. Visualize -
   # a. the most popular call type among churned user
   # b. the minimum charges among all call type among churned user

column_names=data.columns.tolist()

j=0
list_i=[]
def main(df, column_name):
    return column_name,df[column_name][df["churn"]==True].value_counts().max()
    
for i in column_names:
    j=j+1
    if 8<=j<=18:
        a= main(data, i)
        list_i.append(a)

analytics =  data.iloc[:,7:19].sum()
plt.xlabel('types of calls', fontsize=10)
plt.ylabel('sum of call', fontsize=10)
analytics.plot.bar()

#5. Which category of customer having maximum account lenght? Predict and print it
churn_cat=data[(data['churn']== True)]['account length'].max()
non_churncat=data[(data['churn']== False )]['account length'].max()
print("max account lenght catagory: churn cat")

#7. In which area code the international plan is most availed?
print("Area code that is most availed: ",data['area code'].value_counts().index[0])

#6. Predict a relation between the customer and customer care service that 
#whether churned customer have shown their concern to inform the customer care 
#service about their problem or not

pred=data.iloc[:, 19:].groupby('churn')
daa=pred.sum()
label=['Problem reported','Having no problem']
plt.xlabel('sum of customer service calls', fontsize=10)
plt.ylabel('costmer behaviour', fontsize=10)
daa.plot.bar()





