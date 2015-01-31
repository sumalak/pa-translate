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

l_File_Out = open("base-language.txt.new", "w")
l_File_In = polib.pofile(l_Args.input_file)

for entry in l_File_In:
    if entry.msgstr:
        print type(entry.msgctxt.ljust(53)), type(entry.msgstr)
    else:
        print type(entry.msgctxt.ljust(53)), type(entry.msgid)

l_File_Out.close()
