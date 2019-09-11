# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:44:41 2019

@author: Baith
"""

input_int=input("Enter inputs ")
input_int=input_int.split()
input_int=list(map(int,input_int))
newlist=[]
for index,item in enumerate(input_int):
    if item==13:
        newlist.append(index)
        if index != len(input_int)-1:
            newlist.append(index+1)
        
        
        
newlist
sum1=0
for index,item in enumerate(input_int):
    if index not in newlist:
        sum1=sum1+item
print(sum1)

        
    

