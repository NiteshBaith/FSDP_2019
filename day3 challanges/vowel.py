# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:53:38 2019

@author: Baith
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
for each in state_name:
   each=list(each.lower())
   for a in each :
       
       if 'a'== a :           
           each.remove('a')
       elif 'e'== a:
           each.remove('e')
       elif 'i'==a:
           each.remove('i')
       elif 'o'==a:
           each.remove('o')
       elif 'u'==a:
           each.remove('u')
   else:
        
        print("".join(each),end=" ")
    

           
     
    
               
          
              
           
           

           
           
           
      
       
       
       
       
    
    
        
        
           
            
            
            
        