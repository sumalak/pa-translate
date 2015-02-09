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

import argparse

# This is replace pattern below

my_argument_parser = argparse.ArgumentParser()
my_argument_parser.add_argument("input_file")
my_arguments = my_argument_parser.parse_args()

my_input_file = open(my_arguments.input_file)
my_output_file = open("base-language.txt.custom", "w")

with open("replace_pattern.txt") as my_replace_pattern_file:
    iso8859_replacement, custom_alphabet = my_replace_pattern_file.readlines()

iso8859_replacement = iso8859_replacement.rstrip().decode("utf-8")
custom_alphabet = custom_alphabet.rstrip().decode("utf-8")

my_output_file.write("\xef\xbb\xbf\r\n") # \xef\xbb\xbf - zero width no-break space. Game crash without it

for entry in my_input_file:
    entry_unicode = entry.decode("utf-8")
    for i, j in zip(custom_alphabet, iso8859_replacement):
        entry_unicode = entry_unicode.replace(j, i)
    my_output_file.write(entry_unicode.encode("utf-8"))

my_input_file.close()
my_output_file.close()













