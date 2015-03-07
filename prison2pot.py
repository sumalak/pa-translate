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

# Version 0.0.12

import argparse
import polib
import codecs
import re

my_argument_parser = argparse.ArgumentParser()
my_argument_parser.add_argument("txt", help="Original base-language.txt")
my_arguments = my_argument_parser.parse_args()

my_input_file = codecs.open(my_arguments.txt, "r", "utf-8-sig")
my_output_file = polib.POFile(check_for_duplicates=True)

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

line_number = 1

duplicates = [693]  # Example: duplicates = [1, 5, 6]

regexp = re.compile('([a-z_]+) +([\S ]+)')  # One or more a-z or underline, one or more space, one or more non-whitespace or space.

for line in my_input_file:
    if line_number not in duplicates:  # Skip duplicates.
        substring = regexp.match(line)
        if substring:
            line = substring.group(1, 2)
            if len(line) > 1:  # Do line have two values.
                entry = polib.POEntry(
                    msgctxt=line[0],                                    # Taking first part of string.
                    msgid=line[1].replace("\"", "\\\""),                # Taking second part of string.
                    occurrences=[(my_arguments.txt, str(line_number))]  # Taking number of string.
                )
                my_output_file.append(entry)
            else:
                print "Error! Only one value in line", line_number  # Printing number of line with only one value.
    line_number += 1

my_input_file.close()
my_output_file.save('prison_architect.pot')










