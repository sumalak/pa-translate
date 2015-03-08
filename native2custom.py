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

import argparse

# This is replace pattern below.

my_argument_parser = argparse.ArgumentParser()
my_argument_parser.add_argument("txt", help="Text file with non-english characters")
my_argument_parser.add_argument("-r", help="Reverse converting", action="store_true")
my_arguments = my_argument_parser.parse_args()

# Taking characters of native alphabet and not used game characters.

with open("replace_pattern.txt") as my_replace_pattern_file:
    custom_alphabet, iso8859_replacement = my_replace_pattern_file.readlines()
custom_alphabet = custom_alphabet.rstrip().decode("utf-8")
iso8859_replacement = iso8859_replacement.rstrip().decode("utf-8")[:len(custom_alphabet)]
if len(iso8859_replacement) < len(custom_alphabet):
    raise ValueError("Too small second line in replace_pattern.txt")

my_input_file = open(my_arguments.txt)
if my_arguments.r:
    my_output_file = open("base-language.txt.native", "w")
else:
    my_output_file = open("base-language.txt.custom", "w")

# Parsing characters of each string.

for entry in my_input_file:
    entry_unicode = entry.decode("utf-8")
    for i, j in zip(custom_alphabet, iso8859_replacement):
        if my_arguments.r:
            entry_unicode = entry_unicode.replace(j, i)
        else:
            entry_unicode = entry_unicode.replace(i, j)
    my_output_file.write(entry_unicode.encode("utf-8"))

my_input_file.close()
my_output_file.close()
