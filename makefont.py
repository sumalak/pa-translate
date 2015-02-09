#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.

'''

# Version 0.0.3

# This is Prison Architect version of ISO 8859-1 Latin codepage

'''
# Those temporarily removed by reason of overriding nearby character spaces by some characters
row1 =  ur""" ┌┐└┘│─    ♂♀ ♬☼""" 
row2 =  ur"""┼◀↕‼ ┴┬┤↑├→←    """
'''

row1 =  ur"""           ♂♀ ♬☼"""
row2 =  ur""" ◀↕‼    ↑ →←    """
row3 =  ur""" !"#$%&'()*+,-./"""
row4 =  ur"""0123456789:;<=>?"""
row5 =  ur"""@ABCDEFGHIJKLMNO"""
row6 =  ur"""PQRSTUVWXYZ[\]^_"""
row7 =  ur"""`abcdefghijklmno"""
row8 =  ur"""pqrstuvwxyz{|}~ """
row9 =  ur"""€ ‚ƒ„…†‡ˆ‰Š‹Œ Ž """
row10 = ur""" ‘’“”•–—˜™š›œ žŸ"""
row11 = ur""" ¡¢£¤¥¦§¨©ª«¬ ®¯"""
row12 = ur"""°±²³´µ¶·¸¹º»¼½¾¿"""
row13 = ur"""ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏ"""
row14 = ur"""ÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß"""
row15 = ur"""àáâãäåæçèéêëìíîï"""
row16 = ur"""ðñòóôõö÷øùúûüýþÿ"""

codepage = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 + row9 + row10 + row11 + row12 + row13 + row14 + row15 + row16

from PIL import Image, ImageDraw, ImageFont

# Function for drawing fonts

def paint_font_grid(input_string, font_path, output_file, image_mode):

    image_width = 1024
    image_height = 1024
    cell_width = image_width / 16   # 64
    cell_height = image_height / 16 # 64
    bg_color = 0
    text_color = 255

    my_truetype_font = ImageFont.truetype(font_path, 52)
    my_image = Image.new(image_mode, (image_width, image_height), bg_color)
    my_draw = ImageDraw.Draw(my_image)

    row = 1 # Starting coordinates of drawing
    col = 1

    # This draw each symbol in grid

    for position in xrange(256):

        # Aligned to center coordinates

        symbol_width, symbol_height = my_draw.textsize(input_string[position], my_truetype_font)
        text_x = ((cell_width - symbol_width) / 2) + col * 64 - 64
        text_y = (row * 64) - 60

        my_draw.text((text_x, text_y), input_string[position], text_color, my_truetype_font)

        '''
        # For testing purpose
        
        print '{} {} {} {}'.format(symbol_width,
                                   symbol_height,
                                   cell_width,
                                   cell_height)
        
        # This part draw borders to test aligments
        
        rect_x1 = 64 * col - 64
        rect_y1 = 64 * row - 64
        rect_x2 = 64 * col - 1
        rect_y2 = 64 * row - 1
        my_draw.rectangle([rect_x1, rect_y1, rect_x2, rect_y2],
                         outline = 255)
        '''

        if col == 16:
            col = 1
            row = row + 1
        else:
            col = col + 1

    #my_image.show() # For testing purpose

    if output_file == "verdana-bold-outlined.png":
        my_image.save(output_file, transparency=0)
    else:
        my_image.save(output_file)

# Taking replace pattern strings

with open("replace_pattern.txt") as my_replace_pattern_file:
    iso8859_replacement, custom_alphabet = my_replace_pattern_file.readlines()

iso8859_replacement = iso8859_replacement.rstrip().decode("utf-8")
custom_alphabet = custom_alphabet.rstrip().decode("utf-8")

# Replacing characters in codepage

for i, j in zip(custom_alphabet, iso8859_replacement):
    codepage = codepage.replace(i, j)

# Painting fonts

paint_font_grid(codepage, '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', "catalogue.bmp", "L")
paint_font_grid(codepage, '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', "verdana.bmp", "L")
paint_font_grid(codepage, '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', "verdana-bold.bmp", "L")
paint_font_grid(codepage, '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', "verdana-bold-outlined.png", "L") # Python PIL library dont support alpha channel for BMP format

# Code remains

'''

from PIL import Image, ImageDraw

W, H = (300,200)
msg = "hello"

im = Image.new("RGBA",(W,H),"yellow")
draw = ImageDraw.Draw(im)
w, h = draw.textsize(msg)
draw.text(((W-w)/2,(H-h)/2), msg, fill="black")

im.show()

'''

'''

from PIL import Image

img = Image.new( 'RGB', (255,255), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (i, j, 100) # set the colour accordingly

img.show()

'''
