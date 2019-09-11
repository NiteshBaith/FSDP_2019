# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:38:08 2019

@author: Baith
"""

lists=['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
s=""
final_list = list(map(lambda x: s.join(sorted(x)) , lists)) 
t=len(set(final_list))
if t==1:    
    print("anagram")
else:
    print("Not anagram")
