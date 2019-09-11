# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:34:32 2019

@author: Baith
"""
import functools
import operator

def Add(x):
    print("Sum is :",sum(x))
def Multiply(x):
    print(functools.reduce(operator.__imul__ ,x))    
def Largest(x):
    print("maximum is:",max(x))
def Smallest(x):
    print("minimum is:",min(x))
def Sorting(x):
    print("Sorted",sorted(x))
def Remove_Duplicates(x):
    mylist =list(dict.fromkeys(x))
    print("list without duplicates",mylist)
x=input("Enter inputs ")
x=x.split()
x=list(map(int,x))
def printf(x):
    Add(x)
    Multiply(x)
    Largest(x)
    Smallest(x)
    Sorting(x)
    Remove_Duplicates(x)
printf(x)
    
    


