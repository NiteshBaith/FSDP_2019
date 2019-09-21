# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:42:48 2019

@author: Baith
"""
"""
Mini Project 1

Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts

"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw



#Relative Path 
#Image on which we want to paste 
img = Image.open("blank_certi.jpg")
draw = ImageDraw.Draw(img)
#Relative Path 
#Image which we want to paste 
img2=Image.open("Forsk_logo_bw.png")
img.paste(img2, (400, 100)) 
font3 = ImageFont.load_default().font
selectFont = ImageFont.truetype("georgia.ttf", 60 )
selectFont2 = ImageFont.truetype("arial.ttf",30)
font3 = ImageFont.truetype("verdana.ttf",60)
font4 = ImageFont.truetype("georgia.ttf",30)
draw.text( (250,250), "Certificate of Achievement", font=selectFont, fill=(79, 80, 76))
draw.text( (250,350), "For Superior Achievement in masters course of pyhton" ,font=selectFont2, fill=(79, 80, 76) )
draw.text( (300,400), "-MR. NITESH BAITH-" ,font=font3, fill=(93, 14, 39))
draw.text( (120,500), "For successful compliation of the carriculam of data Programming and analysing " ,font=font4, fill=(0, 0, 0))
draw.text( (200,600), "Date: _ _ _ _ _ _ _ " ,font=font4,fill=(93, 14, 39))
draw.text( (800,600), "Sign: _ _ _ _ _ _ _ " ,font=font4,fill=(93, 14, 39))
#draw.text((x,y),"text",font)
# (x,y) is the starting position for the draw object
# text is the text to be entered
# (r,g,b) represents the color eg (255,0,0) is Red
# font is used to specify the Font object
#Saved in the same relative location 
img.save("certimini.jpg")
img.show()
    
          




