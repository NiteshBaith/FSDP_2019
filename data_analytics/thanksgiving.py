# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:40:21 2019

@author: Baith
"""

"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
  Hint:

"""
# Data Preeprocessing modules
import pandas as pd

# Loading the dataset
df = pd.read_csv("thanksgiving.csv",encoding = "ISO-8859-1")
newdata=df.rename(columns={"RespondentID":"RespoId","Do you celebrate Thanksgiving?"
                  :"thx celebration","What is typically the main dish at your Thanksgiving dinner?":"main dis thx_dinner"
                  ,"What is typically the main dish at your Thanksgiving dinner? - Other (please specify)":"typically main dis"
                  ,"How is the main dish typically cooked?":"tppically cooked"
                  ,"How is the main dish typically cooked? - Other (please specify)":"tpycally cooked other"
                ,"What kind of stuffing/dressing do you typically have?":"stuffing"
                ,"What kind of stuffing/dressing do you typically have? - Other (please specify)":"stuffing other"
                ,"What type of cranberry saucedo you typically have?":"saudcedo_type"
                ,"What type of cranberry saucedo you typically have? - Other (please specify)":"saudcedo_other"
                ,"Do you typically have gravy?":"Gravy?"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Brussel sprouts":"Brussel sprouts side"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Carrots":"Carrots side"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cauliflower":"Cauliflower side"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Corn":"Corn sid"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cornbread":"Cornbread side"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Fruit salad":"Fruit Salad side"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Green beans/green bean casserole":"Green beans/green bean casserole side"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Macaroni and cheese":"Macaroni and cheese side"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Mashed potatoes":"Mashed potatoes"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Rolls/biscuits":"Rolls/biscuits side"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Squash":"Squash side"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Vegetable salad":"Vegetable salad"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Yams/sweet potato casserole":"Yams/sweet potato casserole"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)":"Other side"
                ,"Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)":"Other side"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple":"pie apple"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Buttermilk":"Pie Buttermilk"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Cherry":"pie Cherry"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Chocolate":" pie Chocolate"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Coconut cream":"pie Coconut cream"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Key lime":"pie kay lime"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Peach":"pie Peach" 
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan":"pie Peacan"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin":"pie Pumpkin"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Sweet Potato":"pie sweet patato"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - None":"None"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)":"pie other"
                ,"Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)":"pie other"
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Apple cobbler":"Desert Type -Apple Cobbler"
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Blondies":"desert Type -Blondies"
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Brownies":"Desert Type- Bwonies"
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Carrot cake":"Desert Type-carrotcake "
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cheesecake":"Desert Type -cheesecake"
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cookies":"Desert Type -cookies"
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Fudge":"Desert Type-Fudge "
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Ice cream":"Desert Type -Ice cream"
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Peach cobbler":"Desert Type- Peach"
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - None":"None"
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Other (please specify)":"Desert Type -other"
                ,"Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.  - Other (please specify)":"Desert Type -other "
                ,"Do you typically pray before or after the Thanksgiving meal?":"Typically pray"
                ,"How far will you travel for Thanksgiving?":"how far travel"
                ,"Will you watch any of the following programs on Thanksgiving? Please select all that apply. - Macy's Parade": "programm Macy's Parade"

                ,"Have you ever tried to meet up with hometown friends on Thanksgiving night?":"Try to meet on thanksgiving?"
                ,"Have you ever attended a ""Friendsgiving?""":"attended Friendgive?"
                ,"Will you shop any Black Friday sales on Thanksgiving Day?":"will you tx giving black friday"

                ,"Will you employer make you work on Black Friday?":"empoyee make blackfriday?"
                ,"How would you describe where you live?":"live?"
                ,"What is your gender?":"Gender"
                ,"How much total combined money did all members of your HOUSEHOLD earn last year?":"Total earn"
        
        
        
        })

def gender(gender_value):  
    if (gender_value =="Male") :
        return 'Male'
    else :
        return 'nan'  
    
newdata["Gender_male"] = newdata["Gender"].apply(gender)
def genderfe(gender_value):  
    if (gender_value =="Female") :
        return 'female'
    else :
        return 'nan'
newdata["Gender_female"] = newdata["Gender"].apply(genderfe)




newdata['Total earn'] = newdata['Total earn'].str.replace('$','').str.replace(',','').str.replace(' and up','')
newdata['Total earn'] = newdata['Total earn'].str.replace('Prefer not to answer','nan')



for each in newdata['Total earn'].values:
    print(type(each))
    if type(each)==str:
        newdata["Total earn"]=newdata['Total earn'].replace(to_replace = each , value =int(each)) 
        
    elif 'to' in each:
        print(each)
        dd,ddd=each.split(' to ')
        avg_income=(int(dd)+int(ddd))/2
        newdata["Total earn"]=newdata['Total earn'].replace(to_replace = each , value =avg_income) 

newdata["Total earn"]=newdata['Total earn'].replace(to_replace = 'nan' , value =0) 
newdata['Total earn']=newdata['Total earn'].fillna(0)
newdata['saudcedo_type']=newdata['saudcedo_type'].fillna('missing')
df_new=newdata.groupby('saudcedo_type')['Total earn'].mean()

import matplotlib.pyplot as plt
plt.xlabel('types of sauce', fontsize=10)
plt.ylabel('mean', fontsize=10)
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
#autopct show percetage
df_new.plot.pie(explode=explode, colors=colors, autopct='%1.2f%%', shadow=True, startangle=90)

dis_comparison=newdata.groupby('live?')['main dis thx_dinner'].value_counts()
a=dis_comparison.loc[('Rural','Tofurkey')]
b=dis_comparison.loc[('Suburban','Tofurkey')]
print("no of Rural Tofurkey and Suburban Tofurkey are: ",a,b)
dis_comparison.plot.bar()



# Where do people go to Black Friday sales most often?
where=newdata['US Region'][newdata['will you tx giving black friday'] == 'Yes'].value_counts()
where[0:1].index

#  What income groups are most likely to have homemade cranberry sauce?
inc_grp=newdata['Total earn'][newdata['saudcedo_type']=='Homemade'].value_counts()
print(inc_grp.iloc[0:2])


#  Find the number of people who live in each area type (Rural, Suburban, etc)
#who eat different kinds of main dishes for Thanksgiving:
print(newdata['live?'].value_counts())
print(newdata['main dis thx_dinner'].value_counts())
        