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

# Version 0.0.1

import argparse
import polib
import codecs

my_argument_parser = argparse.ArgumentParser()
my_argument_parser.add_argument("input_pot_file")
my_argument_parser.add_argument("input_translated_file")
my_arguments = my_argument_parser.parse_args()

my_input_pot_file = polib.pofile(my_arguments.input_pot_file)                                 # Taking Gettext template.
my_input_translated_file = codecs.open(my_arguments.input_translated_file, "r", "utf-8-sig")  # Taking translated base-language.txt.
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

#d = {key: value for key, value in iterable}

line_number = 1

dictionary = {}

# Putting translated file into key:value dictionary.

for line in my_input_translated_file:
    if line.strip() and line[0] != "#":  # Skip empty lines, comments.
        line = line.rstrip("\r\n").split(None, 1)
        if len(line) > 1:  # Do line have two values.
            key = line[0]
            value = line[1].replace("\"", "\\\"")
            dictionary[key] = value
        else:
            print "Only one value in line", line_number  # Printing number of line with only one value.
    line_number += 1

# Go over Gettext template file and append translated strings.

for entry in my_input_pot_file:
    my_input_translated_file.seek(0)
    for key, value in dictionary.iteritems():
        if entry.msgctxt == key:  # If Gettext context is equal to first part of string.
            translated_entry = polib.POEntry(
                msgctxt = entry.msgctxt,
                msgid = entry.msgid,
                msgstr = value,  # Second (translated) part of string.
                occurrences = entry.occurrences
            )
            my_output_file.append(translated_entry)
            break


my_input_translated_file.close()
my_output_file.save('prison_architect_generated.po')










