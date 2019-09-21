# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 16:10:24 2019

@author: Baith
"""

"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""

# Data Preeprocessing modules
import pandas as pd
import numpy as np

# Loading the dataset
# 2. Get the values from Price column into a numpy.ndarray
data = pd.read_csv("Automobile.csv")
d=data['price']
da = np.array(d)
print (type(da ))

# 3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
data['price'].max()
data['price'].mean()
data['price'].std()

#1. Handle the missing values for Price column
data[data['price'].isnull()]
data['price']=data['price'].fillna(data['price'].mean())