# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:37:28 2019

@author: Baith
"""
"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""
# Data Preeprocessing modules
import pandas as pd
#import numpy as np

# Loading the dataset
data = pd.read_csv("training_titanic.csv")

#1.
datas = data['Survived'].value_counts()
print("survived: ",datas['Survived'][0])
print("Did not survive: ",datas['Survived'][1])

"""2.Calculate and print the survival rates as proportions (percentage)
by setting the normalize argument to True.
Males that survived vs males that passed away
Females that survived vs Females that passed away
"""
print("Survived rate in percentage : ",data['Survived'].value_counts(normalize = True)[0]*100)
df=data[(data['Sex']=='male')]
print("Male Survied Rate(%) : ",df['Survived'].value_counts(normalize = True)[1]*100)
df2=data[(data['Sex']=='female')]
print("Male Survied Rate(%) : ",df2['Survived'].value_counts(normalize = True)[1]*100)


data["child"] = data["Age"].map(lambda x: 0 if (x >=18 or x =='nan' ) else 1 )

def gender_code(gender_value):  
    if (gender_value >= 18) :
        return 0
    elif (gender_value <= 18) :
        return 1   
    
data["Child"] = data["Age"].apply(gender_code)

#df["bool_sex"] = df["sex"].map(lambda x: 0 if x == 'Male' else 1 ) 
#the above labmda fn can't be used bcz nan values replaces by 0

"""
Compare the normalized survival rates for those who are <18 and 
those who are older. 

"""
print("survive rate(%) those are 18+ : ",data['Child'].value_counts(normalize = True)[0]*100)



