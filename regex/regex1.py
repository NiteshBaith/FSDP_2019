# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:11:50 2019

@author: Baith
"""

"""
Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""
import re
Input="""
    4  
    4.000
    -1.00
    +4.54
    """
ff= lambda x: True if re.match(r'[-+]?[\d]+[.][\d]*',x)!=None else False
for i in range(0,4):
    print(ff(Input.split()[i]))
    
    