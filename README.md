# pa-translate

With these tools you can make your own translation more easily without much handwork. 

## How it works

1. Install Python, Python PIL library, Python Polib library.
2. Download all scripts from this repository and put them in folder.
3. Open in editor makefont.py.
4. Replace existing russian characters with your native language characters and replace font paths.
5. Run: python makefont.py
6. Replace original game fonts.
7. Download ready to use translated prison_architect.po files from [Prison Architect translation project on Zanata.org][zanata]. You may be need to sign up and HELP translate game to your native language.
8. Run: python po2prison.py prison_architect.po
9. Open in editor native2custom.py.
10. Replace existing russian characters with your native language characters according to makefont.py.
11. Run: python native2custom.py base-language.txt.native
12. Replace original game translation.
13. Done.

For more detailed description read below.

## makefont.py

Usage: python makefont.py

Dependencies: Python PIL library

Description: It generates any custom fonts. Currectly contain russian characters, replacing western-european characters. Before making your own fonts you need replace characters with your own alphabet. Leave english characters untouched, so you may be sure to see english text in game (if its presented). Then replace original font file <game folder>/data/fonts/catalogue.bmp, verdana.bmp and verdana-bold.bmp. At the moment i didnt make verdana-bold-outlined.bmp fonts to work. In progress.

## po2prison.py

Usage: python po2prison.py prison_architect.po

Dependencies: Python Polib library

Description: Generate base-language.txt.native file with all strings translated according to provided prison_architect.po file with your translation. You can download ready prison_architect.po translations from [Prison Architect translation project on Zanata.org][zanata].

## native2custom.py

Usage: python native2custom.py base-language.txt.native

Dependencies: no

Description: Convert all characters  You need to rename "base-language.txt.custom" to "base-language.txt" and put it to <game folder>/data/language/ with overwrite. At the moment this script configured to convert russian characters to western-european.

## prison2pot.py

Usage: python prison2pot.py base-language.txt

Dependencies: Python Polib library

Description: It have no currently usage for translating participants. I used it to create Gettext template from <game folder>/data/language/base-language.txt and upload it on Zanata.org.

## Additional information

.po file is Gettext format file for helping translators. It is actually .txt format, but it have structured information about translated strings. It may be easily edited. I recommend use Poedit editor (google it). But Gettext is not native format for Prison Architect and i use my own python script to convert .po file to <game folder>/data/language/base-language.txt.

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

[zanata]: https://translate.zanata.org/zanata/project/view/pa
