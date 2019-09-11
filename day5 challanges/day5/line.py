# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:26:50 2019

@author: Baith
"""
file_name=input("Enter File Name")
try:
    file = open("{}".format(file_name), "rt")
    with open('{}'.format(file_name), mode='rt') as file :
    
        for last_line in file:
            pass
        print(last_line)
except IOError:
    print ( "File not Found or incorrect path")
except Exception:
    print ( "This is a general exception")
    file.close()
    

       
   
    
    
