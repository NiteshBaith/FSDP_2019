# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:58:27 2019

@author: Baith
"""

import re

diction={}
with open("post_codes_germany.txt") as p_c_g:
    for eachline in p_c_g:
        reg_exp=re.search(r"[\d ]+([^\d]+[a-z])\s(\d+)",eachline)
        if reg_exp:
             city, post_code = reg_exp.groups()
             if city in diction:
                 diction[city].add(post_code)
             else:
                diction[city]={post_code}
              
with open("largest_cities_germany.txt") as l_c_g:
    for eachline in l_c_g:
        reg_exp=re.search(r"^[0-9]{1,2}\.\s+([\w\s-]+\w)\s+[0-9]",eachline)
        city=reg_exp.group(1)
        print(city,diction[city])
