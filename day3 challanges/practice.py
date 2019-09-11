# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:29:54 2019

@author: Baith
"""
import random as rd
#using random
for i in range(10):
    print(rd.random())
    
for i in range(10):
    print(4*rd.random()+3)
    
# using uniform 
for i in range(10):
    print(rd.uniform(3,7))
# using randint
for i in range(10):
    print(rd.randint(1,10))
