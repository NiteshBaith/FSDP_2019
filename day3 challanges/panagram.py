# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:32:27 2019

@author: Baith
"""
list1=list(input("Enter a string").lower())
list2=list("abcdefghijklmnopqrstuvwxyz")
i=0
for each in list2:
    if each not in list1:
            print("Not Panagram")
            break
    else:
        if(i==25):
            print("Panagaram")







    
 
