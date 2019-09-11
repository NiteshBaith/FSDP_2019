# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 13:44:01 2019

@author: Baith
"""
#isdigit
#isalpha

d={}
d['Letters']=0
d['Digit']=0
input_str=input("Enter a string")
for item in input_str:
    if item.lower()>='a' and item.lower()<='z':
        d['Letters']=d['Letters']+1
    if item.isdigit():
        d['Digit']=d['Digit']+1
print("Letters are:",d['Letters'])
print("Digits are:",d['Digit'])