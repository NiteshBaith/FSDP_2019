# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:38:32 2019

@author: Baith
"""

def reversef(ip):
    print(ip[::-1])
    j=len(ip)
    for each in range(len(ip)):
        
        print(ip[j-1],end="")
        j=j-1
    
reversef(ip=input("Enter a string"))
        
        
        
    
    