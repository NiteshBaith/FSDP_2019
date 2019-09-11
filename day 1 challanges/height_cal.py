# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:38:23 2019

@author: Baith
"""

Height = input("enter height in foot and inches")
foot,inch = Height.split()
foot= float(foot)
inch = float(inch)
print("height in meters",foot*0.3048 + inch*0.025)
print("height in centimeters",(foot*0.3048 + inch*0.025)*100)


