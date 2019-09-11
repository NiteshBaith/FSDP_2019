# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:13:02 2019

@author: Baith
"""

gas_milage = input("enter kelometer travelled and fuel consumed")
kl,ltr = gas_milage.split()
kl= float(kl)
ltr = float(ltr)
print("Average of bike",kl/ltr)