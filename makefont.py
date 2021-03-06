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

# Version 0.1.0

from PIL import Image, ImageDraw, ImageFont

# This is Prison Architect version of ISO 8859-1 Latin codepage.

'''
ur""" ┌┐└┘│─    ♂♀ ♬☼"""
ur"""┼◀↕‼ ┴┬┤↑├→←    """
'''

codepage = (
    ur"""           ♂♀ ♬☼"""
    ur""" ◀↕‼    ↑ →←    """
    ur""" !"#$%&'()*+,-./"""
    ur"""0123456789:;<=>?"""
    ur"""@ABCDEFGHIJKLMNO"""
    ur"""PQRSTUVWXYZ[\]^_"""
    ur"""`abcdefghijklmno"""
    ur"""pqrstuvwxyz{|}~ """
    ur"""€ ‚ƒ„…†‡ˆ‰Š‹Œ Ž """
    ur""" ‘’“”•–—˜™š›œ žŸ"""
    ur""" ¡¢£¤¥¦§¨©ª«¬ ®¯"""
    ur"""°±²³´µ¶·¸¹º»¼½¾¿"""
    ur"""ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏ"""
    ur"""ÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß"""
    ur"""àáâãäåæçèéêëìíîï"""
    ur"""ðñòóôõö÷øùúûüýþÿ""")


def paint_font_grid(input_string, font_path, output_file, image_mode):
    """
    Drawing characters in grid.
    """
    image_width = 1024
    image_height = 1024
    cell_width = image_width / 16    # 64.
    cell_height = image_height / 16  # 64.
    bg_color = 0
    text_color = 255

    my_truetype_font = ImageFont.truetype(font_path, 52)
    my_image = Image.new(image_mode, (image_width, image_height), bg_color)
    my_draw = ImageDraw.Draw(my_image)

    row = 1  # Starting coordinates of drawing.
    col = 1

    # This draw each symbol in grid.

    for position in xrange(256):

        # Aligned to center coordinates.

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
        my_draw.rectangle([rect_x1, rect_y1, rect_x2, rect_y2], outline = text_color)
        '''

        if col == 16:
            col = 1
            row = row + 1
        else:
            col = col + 1

    #my_image.show()  # For testing purpose.

    if output_file == "verdana-bold-outlined.png":
        my_image.save(output_file, transparency=0)
    else:
        my_image.save(output_file)

# Taking characters of native alphabet and not used game characters.

with open("replace_pattern.txt") as my_replace_pattern_file:
    custom_alphabet, iso8859_replacement = my_replace_pattern_file.readlines()
custom_alphabet = custom_alphabet.rstrip().decode("utf-8")
iso8859_replacement = iso8859_replacement.rstrip().decode("utf-8")[:len(custom_alphabet)]
if len(iso8859_replacement) < len(custom_alphabet):
    raise ValueError("Too small second line in replace_pattern.txt")

# Replacing characters in codepage.

for i, j in zip(custom_alphabet, iso8859_replacement):
    codepage = codepage.replace(j, i)

# Painting fonts.

paint_font_grid(codepage, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "catalogue.bmp", "L")
paint_font_grid(codepage, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "verdana.bmp", "L")
paint_font_grid(codepage, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "verdana-bold.bmp", "L")
paint_font_grid(codepage, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "verdana-bold-outlined.png", "L")  # Python PIL library dont support alpha channel for BMP format.

# Code remains.

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
