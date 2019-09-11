# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 11:49:47 2019

@author: Baith
"""
import os
from PIL import Image
for filename in os.listdir("."):
    try:
        name,ext=filename.split(".")
        im = Image.open('{}'.format(filename))
        im.save('{}.png'.format(name))
    except Exception:
        print ( "cannot Convert -> {}".format(filename))


        

    
    

    