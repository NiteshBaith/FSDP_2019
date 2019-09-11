# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 13:37:59 2019

@author: Baith
"""
x=input("Enter inputs ")
x=x.split()
x=list(map(int,x))

def Remove_Duplicates(x):
    mylist =list(dict.fromkeys(x))
    print("list without duplicates",mylist)
    
Remove_Duplicates(x)