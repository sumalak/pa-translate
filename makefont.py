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

#row11 = u" " * 176          # Offset (ASCII + 3 lines)

# Following string variables represent ISO 8859-1 Latin codepage with replaced characters in row12, row13, row14, row15, row16 (i didnt find all original characters in internets).

row1 =  u" ┌┐└┘│─    ♂♀ ♬☼"
row2 =  u"┼◀↕‼ ┴┬┤↑├→←    "
row3 =  u" !\"#$%&\'()*+,-./"
row4 =  u"0123456789:;<=>?"
row5 =  u"@ABCDEFGHIJKLMNO"
row6 =  u"PQRSTUVWXYZ[\\]^_"
row7 =  u"`abcdefghijklmno"
row8 =  u"pqrstuvwxyz{|}~ "
row9 =  u"€ ‚ƒ„…†‡ˆ‰Š‹Œ Ž "
row10 = u" ‘’“”•–—˜™š›œ žŸ"
row11 = u" ¡¢£¤¥¦§¨©ª«¬­®¯"
row12 = u"Ёё²³´µ¶·¸¹º»¼½¾¿"
row13 = u"АБВГДЕЖЗИЙКЛМНОП"
row14 = u"РСТУФХЦЧШЩЪЫЬЭЮЯ"
row15 = u"абвгдежзийклмноп"
row16 = u"рстуфхцчшщъыьэюя"

from PIL import Image, ImageDraw, ImageFont

def paint_font_grid(input_string, font_path, output_file):

    image_width = 1024
    image_height = 1024
    cell_width = image_width / 16       # 64
    cell_height = image_height / 16     # 64
    bg_color = (0, 0, 0)

    my_truetype_font = ImageFont.truetype(font_path, 52)
    my_image = Image.new('RGB', (image_width, image_height), bg_color)
    my_draw = ImageDraw.Draw(my_image)

    row = 1 # Starting coordinates of drawing
    col = 1

    # This draw each symbol in grid of cells and aligned center of cell. Each cell size is 64x64 pixels

    for symbol in string:
        symbol_width, symbol_height = my_draw.textsize(symbol, font=my_truetype_font)
        text_x = ((cell_width - symbol_width) / 2) + col * 64 - 64
        text_y = (row * 64) - 60
        my_draw.text((text_x, text_y), symbol, font=my_truetype_font)
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
        l_Draw.rectangle([rect_x1, rect_y1, rect_x2, rect_y2],
                         outline = (255,255,255))
        '''
        if col == 16:
            col = 1
            row = row + 1
        else:
            col = col + 1

    #l_Image.show()         # For testing purpose

    my_image.save(output_file)



string = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 + row9 + row10 + row11 + row12 + row13 + row14 + row15 + row16

paint_font_grid(string, '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', "catalogue.bmp")
paint_font_grid(string, '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', "verdana.bmp")
paint_font_grid(string, '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', "verdana-bold.bmp")




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
