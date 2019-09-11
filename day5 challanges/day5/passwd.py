# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:50:53 2019

@author: Baith
"""

import csv
file_name=input("Enter File Name")
diction_update={}
try:
    file = open("{}".format(file_name), "rt")
    with open('{}'.format(file_name), mode='rt') as file:
        reader = csv.reader(file, delimiter=":")
        list_list=list(reader)
        for each in list_list:
            diction_update.__setitem__('{}'.format(each[0]), '{}'.format(each[2]))
        for key in sorted(diction_update.keys()):
            print("{} : {} ".format(key,diction_update[key]))
        
    
except IOError:
    print ( "File not Found or incorrect path")
except Exception:
    print ( "Programtic error")
    file.close()

    

    



