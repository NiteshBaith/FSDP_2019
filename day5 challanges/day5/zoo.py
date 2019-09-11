# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:34:07 2019

@author: Baith
"""

from collections import defaultdict
defaultdict={}
diction={}
import csv
with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    for row in csv_reader:  
        if row[2]=="water_need":
            pass
        else:
            defaultdict["{}".format(row[0])]=0
            diction=defaultdict               
with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        if row[0] in diction.keys():
            diction["{}".format(row[0])]=diction["{}".format(row[0])]+int(row[2])
t=sum(diction.values())
print(diction)
print("sum of all animal water Need:",t)          





    
        