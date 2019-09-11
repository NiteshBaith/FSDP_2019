# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 21:50:35 2019

@author: Baith
"""
strs="""Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85"""
dict_input=list(tuple(x.split(",")) for x in strs.splitlines())
print(sorted(dict_input))
