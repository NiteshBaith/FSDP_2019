# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:43:28 2019

@author: Baith
"""
from collections import Counter
from functools import reduce
import csv
  
with open("data/romeo.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=" ")
    list_list=list(csv_reader)
    
    dict_item=reduce(lambda x,y:x+y,list_list)
    print (Counter(dict_item))
    
    
   
    
    
    
    
    