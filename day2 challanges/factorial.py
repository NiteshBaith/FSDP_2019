# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:15:19 2019

@author: Baith
"""


n = int(input("Enter the no"))
i=0
fact=n
while (i<n):
    n=n*(fact-1)
    fact=fact-1
    i=i+1    
    if (fact==1):
        break
print(n)
"""and"""

import math as m
fct=m.factorial(no)


    
