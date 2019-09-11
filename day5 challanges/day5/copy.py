
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:53:43 2019

@author: Baith
"""
"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""
# Copying a file
with open ("data/words.txt", "rt") as rf :
  with open ("data/word2.txt", "wt") as wf :
    for line in rf :
      wf.write ( line)

