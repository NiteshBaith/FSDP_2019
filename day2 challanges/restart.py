# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:12:34 2019

@author: Baith
"""


str2 = "RESTART"
count =0
for i in str2:
    if i=="R":
        print(count) 
        if count>0:
            str3=str2.replace("R","$")
    count=count+1
    

str4=str3.replace("$","R",1)
print(str4)


        
        
        
        