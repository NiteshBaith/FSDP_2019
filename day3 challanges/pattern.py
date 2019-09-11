# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:01:14 2019

@author: Baith
"""
ip = int(input("Enter max star to be display "))
for i in range (0, ip):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\t")
for i in range (ip, 0, -1):
    
    for j in range(0, i -1):
        print("*", end=' ')
    print("\t")
