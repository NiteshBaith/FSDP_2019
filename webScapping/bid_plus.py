# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:33:37 2019

@author: Baith
"""
"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          
          # Optional - Do not do this
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
from selenium import webdriver
from time import sleep
url = "https://bidplus.gem.gov.in/bidlists"



#For Windows System
#driver = webdriver.Chrome("C:/Users/rohit/Downloads/chromedriver_win32/chromedriver.exe")
#driver = webdriver.Firefox(executable_path="D:/Forsk Technologies/geckodriver")

# For Mac System
#driver = webdriver.Chrome(executable_path="/Users/sylvester/chromedriver")
#driver = webdriver.Firefox(executable_path="/Users/sylvester/geckodriver")
driver = webdriver.Chrome("C:/Users/Baith/Chrome_driver/chromedriver.exe")

# Opening the submission url
driver.get(url)


data=driver.find_element_by_id("pagi_content")
bidno=[]
Item=[]
Quantity_Required=[]
Dept_Name=[]
Start_Date=[]
End_Date=[]


#//*[@id="pagination"]/ul/li/ul/li[2]/a this is first page path address
#//*[@id="pagination"]/ul/li/ul/li[3]/a


n=2
while n < 10:
    for row in data.find_elements_by_xpath("//div[@class='block_header']"):
        para_bd=row.find_elements_by_tag_name('p')
       
        if len(para_bd)==2:
            bidno.append(para_bd[0].text.strip())
    i=0
    for item in data.find_elements_by_xpath("//div[@class='col-block']"):
        
            if i%3==0:
                para=item.find_elements_by_tag_name('p')
                if len(para)==2:
                    Item.append(para[0].text.strip())
                    Quantity_Required.append(para[1].text.strip())
                
            if i%3==1:
                para=item.find_elements_by_tag_name('p')
                if len(para)==2:
                    Dept_Name.append(para[1].text.strip())
                    
            if i%3==2:
                para=item.find_elements_by_tag_name('p')
                if len(para)==2:
                    Start_Date.append(para[0].text.strip())
                    End_Date.append(para[1].text.strip())
            i=i+1
    driver.find_element_by_xpath('//*[@id="pagination"]/ul/li/ul/li['+str(n)+']/a').click()
    sleep(3)
    n+=1
          
from collections import OrderedDict

col_name = ["bidnumber","Items","Quantity Required","Dept name and address","start date","Ending date"]
col_data = OrderedDict(zip(col_name,[bidno,Item,Quantity_Required,Dept_Name,Start_Date,End_Date]))

import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("bidcsv.csv")

                
            
                
            
            
            
    
   
        
        
