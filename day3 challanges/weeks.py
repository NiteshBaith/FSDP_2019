# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:15:50 2019

@author: Baith
"""

tuple_1=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
tuple_2=()
tuple_3=("")
for day in tuple_1 :
    if day not in tuple_2:
        
        tuple_2=tuple_2 +(day,)
print(tuple_2)
        
        