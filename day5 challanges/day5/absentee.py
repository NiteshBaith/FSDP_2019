# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:21:40 2019

@author: Baith
"""
"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
file = open('data/new.txt', mode='wt')   
for i in range(25):
        str_input=input("Enter student name")
        
        if str_input=="":
            break
        file.write(str_input)
        file.write("\n")
file.close()

with open('data/new.txt', mode='rt') as file :
   file_contents = file.readlines()
   print (file_contents)