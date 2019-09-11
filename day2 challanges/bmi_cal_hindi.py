# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:43:09 2019

@author: Baith
"""
mashi= input("Enter your weight in kg and height in meter (\u0939\u093F\u093A\u0926\u0940) ")
mass,height = mashi.split()
mass=float(mass)
height=float(height)
print( "your BMI value is",mass/(height*height) )
