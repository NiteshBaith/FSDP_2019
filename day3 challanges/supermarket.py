# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 14:05:42 2019

@author: Baith
"""        
d = {}
for item in range(int(input("Enter the record(no of rows) you wanna store"))):
    keys, space, values = input("Enter item name and quantity").rpartition(' ')
   
    d[keys] = d.get(keys, 0) + int(values)
d
for keys, values in d.items():
    print(keys, values)
    


