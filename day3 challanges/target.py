# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 10:32:22 2019

@author: Baith
"""
ip=input("Enter the small bricks , large bricks and target")
s,l,t=ip.split()
s=int(s)
l=int(l)
t=int(t)

if 2*s+5*l>=t:
    print("TRUE")
else: print("False")
    
    
    
