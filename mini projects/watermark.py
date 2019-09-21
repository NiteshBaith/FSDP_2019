# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:43:37 2019

@author: Baith
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
photo = Image.open('blank_certi.jpg')
watermark = Image.open('Forsk_logo_bw.png')
photo.paste( (25, 25),watermark)
photo.show()

 
def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)
 
    # make the image editable
    drawing = ImageDraw.Draw(photo)
 
    black = (3, 8, 12)
    font = ImageFont.truetype("arial.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)
 
 
if __name__ == '__main__':
    img = 'certimini.jpg'
    watermark_text(img, 'cerimini.jpg',
                   text='www.Baith.com',
                   pos=(0, 0))