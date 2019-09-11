# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:19:41 2019

@author: Baith
"""

Int_input = list(input("Enter the the number"))


for i in Int_input:
    if i == " ":
        Int_input.remove(' ')

p = 0      
for i in Int_input:
    p =p+1
    if(p==(len(Int_input) -1)):
       
        break
    if (Int_input[p-1] == Int_input[p+1]):
            print("true")
   
    
    
else: print("false")        

        
    
        
    
    
    



