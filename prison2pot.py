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
import polib

# Pre-part l_ mean that variable is mine (for readability). Not at all.

l_Parser = argparse.ArgumentParser()
l_Parser.add_argument("input_file")
l_Args = l_Parser.parse_args()

l_File_In = open(l_Args.input_file)
l_File_Out = polib.POFile()

l_File_Out.metadata = {
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

next(l_File_In) # This skip because of some undefined data in begining of file...

line_number = 2 # ...and we skip it in here too.

# Lets parse each line, except empty one and comments.

for line in l_File_In:
    if not line.strip() or line[0] == "#":
        line_number +=  1
        continue
    else:
        entry = polib.POEntry(
            msgctxt = line.split(None, 1)[0].rstrip("\r\n"),
            msgid = line.split(None, 1)[-1].rstrip("\r\n").replace("\"", "\\\""),
            occurrences=[(l_Args.input_file, str(line_number))]
        )
        if line_number != 687: # This statement because of unaccepteable duplicate with 690 line.
            l_File_Out.append(entry)
        line_number += 1

l_File_In.close()
l_File_Out.save('prison_architect.pot')







