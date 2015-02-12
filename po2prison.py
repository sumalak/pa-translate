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

# Version 0.0.5

import argparse
import polib

my_argument_parser = argparse.ArgumentParser()
my_argument_parser.add_argument("input_file")
my_arguments = my_argument_parser.parse_args()

my_input_file = polib.pofile(my_arguments.input_file)
my_output_file = open("base-language.txt.native", "w")

my_output_file.write("\xef\xbb\xbf\r\n") # Line with byte order mark. Game crash without it

for entry in my_input_file:
    if entry.msgstr:
        my_output_file.write(entry.msgctxt.ljust(53).encode("utf-8") + entry.msgstr.encode("utf-8") + "\r\n")
    else:
        my_output_file.write(entry.msgctxt.ljust(53).encode("utf-8") + entry.msgid.encode("utf-8") + "\r\n")

my_output_file.close()









