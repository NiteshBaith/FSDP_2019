# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:24:23 2019

@author: Baith
"""

def transf(ip):
    
    ip2='aeiouAEIOU'
    csm=[""]
    
    for char in ip:
            if char not in ip2:
                if(char == ' '):
                    csm.append(char)
                else:
                    char = char + 'o' + char 
                    csm.append(char)
               
            else:
                csm.append(char)
    
    print("".join(csm))

transf(ip=input("Enter a string"))
                
        