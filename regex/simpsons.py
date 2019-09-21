# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:54:24 2019

@author: Baith
"""
 
"""

Code Challenge
  Name: 
    Simpsons Phone Book
  Filename: 
    simpsons.py
  Problem Statement:
    There are some people with the surname Neu. 
    We are looking for a Neu, but we don't know the first name, 
    we just know that it starts with a J. 
    Let's write a Python script, which finds all the lines of the phone book, 
    which contain a person with the described surname and a first name starting with J. 
 Hint: 
     Use Regular Expressions 
"""
import re
import os
rx = re.compile('txt')

for filenames in os.listdir('.'):
    if re.search(rx,filenames):
        f_name=filenames
listdata = []             
with open(f_name,'r') as file:
    txt=file.readlines()
    for each in txt:
         dd=re.findall(r'^[J]+[a-zA-z]* [Neu]+', each)
         if dd!=None:   
             listdata.append(each)
            
    



