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

#iso8859_replacement = u"ÀÁÂÃÄÅ°ÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß"
#russian_alphabet = u"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#reps = {'А':'À', 'Б':'Á', 'В':'Â', 'Г':'Ã', 'Д':'Ä', 'Е':'Å', 'Ё':'°', 'Ж':'Æ', 'З':'Ç', 'И':'È', 'Й':'É', 'К':'Ê', 'Л':'Ë', 'М':'Ì', 'Н':'Í', 'О':'Î', 'П':'Ï', 'Р':'Ð', 'С':'Ñ', 'Т':'Ò', 'У':'Ó', 'Ф':'Ô', 'Х':'Õ', 'Ц':'Ö', 'Ч':'×', 'Ш':'Ø', 'Щ':'Ù', 'Ъ':'Ú', 'Ы':'Û', 'Ь':'Ü', 'Э':'Ý', 'Ю':'Þ', 'Я':'ß'}

dictionary = {u'А':u'À', u'Б':u'Á', u'В':u'Â', u'Г':u'Ã', u'Д':u'Ä', u'Е':u'Å',
              u'Ё':u'°', u'Ж':u'Æ', u'З':u'Ç', u'И':u'È', u'Й':u'É', u'К':u'Ê',
              u'Л':u'Ë', u'М':u'Ì', u'Н':u'Í', u'О':u'Î', u'П':u'Ï', u'Р':u'Ð',
              u'С':u'Ñ', u'Т':u'Ò', u'У':u'Ó', u'Ф':u'Ô', u'Х':u'Õ', u'Ц':u'Ö',
              u'Ч':u'×', u'Ш':u'Ø', u'Щ':u'Ù', u'Ъ':u'Ú', u'Ы':u'Û', u'Ь':u'Ü',
              u'Э':u'Ý', u'Ю':u'Þ', u'Я':u'ß',
              u'а':u'à', u'б':u'á', u'в':u'â', u'г':u'ã', u'д':u'ä', u'е':u'å',
              u'ё':u'±', u'ж':u'æ', u'з':u'ç', u'и':u'è', u'й':u'é', u'к':u'ê',
              u'л':u'ë', u'м':u'ì', u'н':u'í', u'о':u'î', u'п':u'ï', u'р':u'ð',
              u'с':u'ñ', u'т':u'ò', u'у':u'ó', u'ф':u'ô', u'х':u'õ', u'ц':u'ö',
              u'ч':u'÷', u'ш':u'ø', u'щ':u'ù', u'ъ':u'ú', u'ы':u'û', u'ь':u'ü',
              u'э':u'ý', u'ю':u'þ', u'я':u'ÿ'}

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

# Pre-part l_ mean that variable is mine

l_Parser = argparse.ArgumentParser()
l_Parser.add_argument("input_file")
l_Args = l_Parser.parse_args()

l_File_In = open(l_Args.input_file)
l_File_Out = open("base-language.txt.custom", "w")

l_File_Out.write("\xef\xbb\xbf\r\n")

for entry in l_File_In:
    #for i, j in dictionary.iteritems():
    #    entry = entry.decode("utf-8").replace(i, j)
    l_File_Out.write(replace_all(entry.decode("utf-8"), dictionary).encode("utf-8"))

l_File_In.close()
l_File_Out.close()













