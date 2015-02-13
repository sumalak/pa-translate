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

# Version 0.0.6

import argparse
import polib
import codecs

my_argument_parser = argparse.ArgumentParser()
my_argument_parser.add_argument("input_file")
my_arguments = my_argument_parser.parse_args()

my_input_file = polib.pofile(my_arguments.input_file)
my_output_file = codecs.open("base-language.txt.native", "w", "utf-8-sig")

for entry in my_input_file:
    if entry.msgstr:
        my_output_file.write(entry.msgctxt.ljust(53) + entry.msgstr + "\r\n")
    else:
        my_output_file.write(entry.msgctxt.ljust(53) + entry.msgid + "\r\n")

my_output_file.close()









