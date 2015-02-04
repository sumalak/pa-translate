# pa-translate

Currently no ready to use translations. All these information for participants in traslation project.

## How it works

You make fonts, then translate any russian (or any other language) word and put result in <game folder>/data/language/base-language.txt. In result game shows you english and your native characters right.

## font.py

Usage: python font.py

Dependencies: Python PIL library

Description: It generates any custom fonts. Currectly contain russian characters, replacing western-european characters. Before making your own fonts you may replace characters, presented in the script. Leave english characters untouched, so you may be sure to see english text in game (if its presented). Then replace original font file <game folder>/data/fonts/catalogue.bmp, verdana.bmp and verdana-bold.bmp. At the moment i didnt make verdana-bold-outlined.bmp fonts to work. In progress.

## translator.py

Usage: python translator.py <your non-english word>

Dependencies: no

Description: At the moment this script only able to translate russian characters to western-european characters according to current script font.py.

## po2prison.py

Usage: python po2prison.py prison_architect.po

Dependencies: Python Polib library

Description: .po file is Gettext format file for helping translators. It is actually .txt format, but it have structured information about translated strings. It may be easily edited. I recommend use Poedit editor (google it). But Gettext is not native format for Prison Architect and i use my own python script to convert .po file to <game folder>/data/language/base-language.txt.

## prison2pot.py

Usage: python prison2pot.py base-language.txt

Dependencies: Python Polib library

Description: It have no currently usage for translating participants. I used it to create Gettext template from <game folder>/data/language/base-language.txt and upload it on Zanata.org.

## Additional information

Possible game files structure is:

* lib
* lib64
* main.dat
* PrisonArchitect.i686
* PrisonArchitect.x86_64
* sounds.dat

Then you need to unpack main.dat (it is actually a RAR archive) in game folder and rename main.dat to main1.dat (game will load unpacked data).

Bitmap font parameters:

* catalogue.bmp - grayscale, 24 bits, do not save colors, RL-coding
* verdana.bmp - grayscale, 24 bits, do not save colors, RL-coding
* verdana-bold.bmp - grayscale, 24 bits, do not save colors, RL-coding
* verdana-bold-outlined.bmp - ???

facepalm (>ლ)
