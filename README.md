# pa-translate

## Introduction

This is python project with scripts, that will help translate applications, that use bitmap fonts (image with map of characters) and language strings in any simple text file (like base-language.txt in Prison Architect).

Why use this? Answer is simple: Gettext format allow you easy manage all language strings of application and collaborate with other translators on Zanata.org (and other collaborative translation websites/systems). When new version of Prison Architect arrives you need to manually manipulate with game language files, compare difference, transfer translations. With Gettext, Python and these scripts our task become trivial.

## How-to (if you want only to participate in translation)

Note: If you dont have account on Zanata.org, then you need [sign up][zanata-sign-up].

0. Log In on [Zanata website][zanata-website].
0. [Join a language][zanata-join-language].
0. Open [Prison Architect translation project page][zanata-prison].
0. Choose latest version.
0. Choose your language.
0. Choose prison_architect document.
0. Begin translating.

For more help contact [David Mason][github-davidmason] on Zanata team.

Note: if you have your own translation, you can help project and upload it on [Zanata website][zanata-website] by following steps:

0. Install Python, Python PIL library, Python Polib library (Python version 2.7.8 or near).
0. Download all scripts from this repository and put them in work folder.
0. Put in work folder original base-language.txt.
0. Run from command line: python prison2po.py base-language.txt prison_architect.pot
0. Put in work folder translated base-language.txt. Important: your translated base-language.txt must contain native language characters (german, french, spain etc.).
0. Run from command line: python prison2po.py prison_architect.pot base-language.txt
0. Log In on [Zanata website][zanata-website].
0. [Join a language][zanata-join-language].
0. Open [Prison Architect translation project page][zanata-prison].
0. Choose latest version.
0. Choose your language.
0. Choose prison_architect document.
0. Choose documents option in right upper corner.
0. Choose upload action of prison_architect document.
0. Upload prison_architect.po file.

## How-to (if you want to develop your own translation)

Note: If you dont have account on Zanata.org, then you need [sign up][zanata-sign-up].

0. Log In on [Zanata website][zanata-website].
0. Open [Prison Architect translation project page][zanata-prison].
0. Choose latest version.
0. Choose your language.
0. Choose prison_architect document.
0. Choose documents option in right upper corner.
0. Choose download action of prison_architect document.
0. Put downloaded prison_architect.po in work folder.
0. Install Python, Python PIL library, Python Polib library (Python version 2.7.8 or near).
0. Download all scripts from this repository and put them in work folder.
0. Open in text editor replace_pattern.txt.
0. Write in first line all characters from your alphabet in upper and lower case.
0. Save and close replace_pattern.txt.
0. Run from command line: python makefont.py
0. Run from command line: python po2prison.py prison_architect.po
0. Run from command line: python native2custom.py base-language.txt.native
0. Open verdana-bold-outline.png and save as verdana-bold-outline.bmp (BMP version 3 and type GrayscaleAlpha).
0. Replace original game fonts here "<game folder>/data/fonts/" with new one from work folder.
0. Replace original game translation here "<game folder>/data/language/" with new one from work folder (you also need to rename base-language.txt.custom to base-language.txt).

For more help contact [David Mason][github-davidmason] on Zanata team.

## How-to (if you want to develop your own translation without using Zanata)

0. Install Python, Python PIL library, Python Polib library (Python version 2.7.8 or near).
0. Download all scripts from this repository and put them in work folder.
0. Put base-language.txt from "<game folder>/data/language/" into work folder.
0. Run: python prison2pot.py base-language.txt
0. Open prison_architect.pot with good text editor (i highly recommend use [Poedit][poedit]).
0. Translate all entries and save as prison_architect.po.
0. Open in text editor replace_pattern.txt.
0. Write in first line all characters from your alphabet in upper and lower case.
0. Save and close replace_pattern.txt.
0. Run from command line: python makefont.py
0. Run from command line: python po2prison.py prison_architect.po
0. Run from command line: python native2custom.py base-language.txt.native
0. Open verdana-bold-outline.png and save as verdana-bold-outline.bmp (BMP version 3 and type GrayscaleAlpha).
0. Replace original game fonts here "<game folder>/data/fonts/" with new one from work folder.
0. Replace original game translation here "<game folder>/data/language/" with new one from work folder (you also need to rename base-language.txt.custom to base-language.txt).

## po2prison.py

Usage: python po2prison.py prison_architect.po

Dependencies: Python Polib library

Description: Generate translated file base-language.txt.native using provided file prison_architect.po with your own downloaded translation.

## native2custom.py

Usage: python native2custom.py base-language.txt.native

Dependencies: no

Description: Convert all characters with replace pattern from file replace_pattern.txt.

## makefont.py

Usage: python makefont.py

Dependencies: Python PIL library

Description: It generate custom fonts. Right now Python PIL library dont support transparency in BMP format.

## prison2pot.py

Usage: python prison2pot.py base-language.txt

Dependencies: Python Polib library

Description: It convert original file base-language.txt to Gettext template file.

## prison2po.py

Usage: python prison2po.py base-language.txt prison_architect.pot

Dependencies: Python Polib library

Description: It convert translated file base-language.txt to Gettext catalog file.

## Links

* [Prison Architect on Zanata website][zanata-prison]
* [Russian translation for Steam version of Prison Architect][russian-translation-steam]
* [Poedit translation editor][poedit]

## Additional information

.po file is Gettext format file for helping translators. It is actually .txt format, but it have structured information about translated strings. It may be easily edited. I recommend use Poedit editor (google it). But Gettext is not native format for Prison Architect and i use my own python scripts to convert translated prison_architect.po file to <game folder>/data/language/base-language.txt.

If your game files structure is:

* lib
* lib64
* main.dat
* PrisonArchitect.i686
* PrisonArchitect.x86_64
* sounds.dat

Then you need to unpack main.dat (it is actually a RAR archive) in game folder and rename main.dat to main1.dat (to make game not able to see this file).

Bitmap font parameters:

* catalogue.bmp - Grayscale
* verdana.bmp - Grayscale
* verdana-bold.bmp - Grayscale
* verdana-bold-outlined.bmp - GrayscaleAlpha, BMP3 (Microsoft Windows bitmap image (V3))

GIMP export options: do not save colors, not run-length encoded.

## Story (>ლ)

Following information about BMP3 with transparency from website of ImageMagick.

> I've installed Xnview and it does indicate that a BMP3 file that I created with nconvert has transparency. So, I looked at a hexdump of the file.
> The BMP3 file header indicates that the image has 32-bits per pixel. Nconvert has used the high byte of each DWORD to indicate the opacity of the pixel. If it is zero, the pixel is transparent and if it is 255 the pixel is fully opaque. I haven't tried to sort out whether Nconvert will produce a BMP3 with partially transparent pixels nor whether Xnview could display one properly.
> However, BMP is a Microsoft file format and the documentation that comes with my C compiler, and also what I have found on Microsoft's website, says that the high byte of each DWORD is unused. Therefore using this byte for opacity (or anything else) is a non-standard use.
> The specific problem that I can see right now is that because Microsoft says that the high byte is unused, programs are free to leave any random value in that byte. How do you then distinguish between a BMP generated by such a program and a BMP which is using that byte as opacity?
> I don't think that Magick (IM's developer) will expend any effort on the BMP coder to handle an apparently undefined/undocumented extension of the BMP format. If you can find documentation of this extension and how it fits in with the existing BMP3 spec maybe it will happen.

by el_supremo

[poedit]: http://poedit.net/
[zanata-website]: https://translate.zanata.org/zanata/
[zanata-prison]: https://translate.zanata.org/zanata/project/view/pa
[zanata-sign-up]: http://zanata.org/help/accounts/sign-up/
[zanata-join-language]: http://zanata.org/help/translation/translator-add/
[github-davidmason]: https://github.com/davidmason/
[russian-translation-steam]: http://steamcommunity.com/sharedfiles/filedetails/?id=390281765
