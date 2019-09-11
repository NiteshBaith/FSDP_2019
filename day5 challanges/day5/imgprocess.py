# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:19:31 2019

@author: Baith
"""
from PIL import Image
file_name=input("Enter File Name")
try:
    img = Image.open("{}".format(file_name))
except IOError:
        print ( "File not Found or incorrect path")
except Exception:
        print ( "This is a general exception")
    
inp=int(input("Enter 1 for grayscale \n 2 for rotating,\n 3 for Crop,\n 4 for tumpnail\n "))
def Imgfun(x):
    
        
        if x==1:
            img_grayscale=img.convert(mode="L")
            img_grayscale.show()
        if x==2:
            img_rotate = img.transpose(Image.ROTATE_90)
            img_rotate.save("data/rorate_sample1.jpg")
            img_rotate.show()
            
        if x==3:
        # left, upper,right,lower
            width, height = img.size   # Get dimensions
            new_width,new_height=input("Enter width and height to crop from centre ").split()
            new_height=int(new_height)
            new_width=int(new_width)
            left = (width - new_width)/2
            top = (height - new_height)/2
            right = (width + new_width)/2
            bottom = (height + new_height)/2
            box=(left,top,right,bottom)
            crop_im = img.crop(box)
            
            crop_im.save('data/crop_sample1.jpg')
            crop_im.show()
        if x==3:
            img.thumbnail((75, 75))
            print(img.width, img.height)
            img.save('data/thumb_sample1.jpg')
    

Imgfun(inp)





