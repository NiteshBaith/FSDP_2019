# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:48:47 2019

@author: Baith
"""

# Data Preeprocessing modules
import pandas as pd
import numpy as np

# Loading the dataset
data = pd.read_csv("Salaries.csv")

"""

1. Which Male and Female (Professor) has the highest and the lowest salaries

"""

prof_male = data[(data['sex']=='Male') & (data['rank']=='Prof')]
print(prof_male[prof_male['salary'] == prof_male['salary'].min()])
print(prof_male[prof_male['salary'] == prof_male['salary'].max()])

prof_female = data[(data['sex']=='Female') & (data['rank']=='Prof')]
print(prof_female[prof_female['salary']==prof_female['salary'].min()])
print(prof_female[prof_female['salary']==prof_female['salary'].max()])

"""
2. Which Professor takes the highest and lowest salaries.
"""
professor = data[(data['rank']=='Prof')]
print(professor[professor['salary'] == professor['salary'].max()])
print(professor[professor['salary'] == professor['salary'].min()])


"""
3. Missing Salaries - should be mean of the matching salaries of those whose service is the same
"""
# Find those rows in which salary column has NaN
data[data['salary'].isnull()]

m = data.groupby("service")["salary"].mean()
   
m1=pd.Series(m)[18]
m2=pd.Series(m)[2]


# fill all the records with missing values, with mean of we wanted
data['salary'][data.index == 7]=data['salary'].fillna(m1)
data['salary'][data.index == 28]=data['salary'].fillna(m2)

    
"""
4. Missing phd - should be mean of the matching service 
"""
data[data['phd'].isnull()]
phd_grpby = data.groupby("phd")["service"].mean()
phd_n1=pd.Series(phd_grpby)[8]
phd_n2=pd.Series(phd_grpby)[33]
# fill all the records with missing values, with mean of the matching service 
data['phd'][data.index == 13]=data['phd'].fillna(phd_n1)
data['phd'][data.index == 33]=data['phd'].fillna(phd_n2)

"""
5. How many are Male Staff and How many are Female Staff. 
"""

gender_count = data['sex'].value_counts().reset_index()
#this is for setting new index using .reset_index()
gender_count_dataf = pd.DataFrame() 
# Empty data frame where male female datas to be filled
gender_count_dataf['Male'] = [gender_count['sex'][0]]
gender_count_dataf['female'] = [gender_count['sex'][1]]


"""
6. How many are Prof, AssocProf and AsstProf. 
"""
# same as upper male female case
data_rank = data['rank'].value_counts().reset_index()
data_rank_ref = pd.DataFrame()
data_rank_ref['Prof'] = [data_rank['rank'][0]]
data_rank_ref['AsstProf'] = [data_rank['rank'][1]]
data_rank_ref['AsscProf'] = [data_rank['rank'][2]]

"""
7. Who are the senior and junior most employees in the organization.
"""

print(data[data['service'] == data['service'].max()])
print(data[data['service'] == data['service'].min()])

# for checking right or wrong the upper execution
data.sort_values(['service'])





