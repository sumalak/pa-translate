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

my_input_file = open(my_arguments.input_file)
my_output_file = polib.POFile()

my_output_file.metadata = {
    'Project-Id-Version': '1.0',
    'Report-Msgid-Bugs-To': 'you@example.com',
    'POT-Creation-Date': '2007-10-18 14:00+0100',
    'PO-Revision-Date': '2007-10-18 14:00+0100',
    'Last-Translator': 'you <you@example.com>',
    'Language-Team': 'English <yourteam@example.com>',
    'MIME-Version': '1.0',
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Transfer-Encoding': '8bit',
}

next(my_input_file) # Skip line with byte order mark

line_number = 2

# Lets parse each line, except empty one and comments.

for line in my_input_file:
    if not line.strip() or line[0] == "#":
        line_number +=  1
        continue
    else:
        entry = polib.POEntry(
            msgctxt = line.split(None, 1)[0].rstrip("\r\n"),
            msgid = line.split(None, 1)[-1].rstrip("\r\n").replace("\"", "\\\""),
            occurrences = [(my_arguments.input_file, str(line_number))]
        )
        if line_number != 687: # This statement because of unaccepteable duplicate with 690 line.
            my_output_file.append(entry)
        line_number += 1

my_input_file.close()
my_output_file.save('prison_architect.pot')







