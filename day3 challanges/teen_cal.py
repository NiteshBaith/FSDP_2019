# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 13:32:39 2019

@author: Baith
"""


d= {"a" : 2, "b" : 15, "c" : 13}
def fix_teen(n):
        if n in {13, 14, 17, 18, 19}:
            return 0
        else:
            return n            
result=map(fix_teen, d.values())
print(sum(list(result)))



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  