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

import argparse

# This is replace pattern below

iso8859_replacement =  u"ÀÁÂÃÄÅ°ÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäå±æçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
russian_alphabet =     u"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

my_argument_parser = argparse.ArgumentParser()
my_argument_parser.add_argument("input_file")
my_arguments = my_argument_parser.parse_args()

my_input_file = open(my_arguments.input_file)
my_output_file = open("base-language.txt.custom", "w")

my_output_file.write("\xef\xbb\xbf\r\n") # I dont know what is this array of non-printable characters, but it was important to be in begin of base-language.txt

for entry in my_input_file:
    entry_unicode = entry.decode("utf-8")
    for i, j in zip(russian_alphabet, iso8859_replacement):
        entry_unicode = entry_unicode.replace(i, j)
    my_output_file.write(entry_unicode.encode("utf-8"))

my_input_file.close()
my_output_file.close()













