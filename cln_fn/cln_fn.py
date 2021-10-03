#!/usr/bin/python

import os
import string

VALID = string.ascii_letters + string.digits + '_- .'
SUBST = {   "'": '',
            '!': '',
            '#': '_',
            '$': 'S',
            '%': '_',
            '&': '_',
            '(': '_',
            ')': '_',
            '+': '_',
            ',': ',',
            ':': '_',
            ';': '_',
            '=': '_',
            '@': '_',
            '[': '_',
            '\u2009': '',
            '\u200a': '',
            '\u200b': '',
            '\u200c': '',
            '\u200d': '',
            '\u202c': '',
            '\u65039': '',
            '\u9654': '',
            '\xa0': '',
            ']': '_',
            '`': '',
            'é': 'e',
            '{': '_',
            '}': '_',
            '~': '-',
            '¡': '_',
            '¤': '_',
            '«': '_',
            '±': '_',
            '´': '',
            '»': '_',
            'À': 'A',
            'Ä': 'AE',
            'Å': 'AA',
            'Æ': 'AE',
            'É': 'E',
            'Ö': 'OE',
            'Ø': 'OE',
            'ß': 'ss',
            'à': 'a',
            'á': 'a',
            'ã': 'a',
            'ä': 'ae',
            'å': 'aa',
            'æ': 'ae',
            'ç': 'c',
            'è': 'e',
            'é': 'e',
            'ê': 'e',
            'ë': 'e',
            'í': 'i',
            'ó': 'o',
            'ö': 'OE',
            'ø': 'oe',
            'ü': 'u',
            'ě': 'e',
            'š': 's',
            'ț': 't',
            'А': 'A',  # Russian?
            'Б': 'b',
            'В': 'B',  # Russian?
            'Г': 'R',  # Russian?
            'Д': 'D',  # Russian?
            'Е': 'E',  # Russian?
            'Ж': 'X',  # Russian?
            'И': 'N',  # Russian?
            'Й': 'N',  # Russian
            'К': 'K',  # Russian?
            'М': 'M',
            'Н': 'H',  # Russian?
            'О': 'O',  # Russian?
            'П': 'N',
            'Р': 'P',  # Russian?
            'С': 'C',  # Russian?
            'Т': 'T',
            'Ч': 'y',  # Russian?
            'Ш': 'W',
            'Ы': 'bl',  # Russian?
            'а': 'a',
            'б': 'd',
            'в': 'B',
            'г': 'r',
            'д': 'D',
            'е': 'e',  # apparently not a normal e ...
            'ж': 'X',
            'з': '3',
            'и': 'n',
            'й': 'n',
            'к': 'k',
            'л': 'r',
            'м': 'M',
            'н': 'H',
            'о': 'o',
            'п': 'n',
            'р': 'p',
            'с': 'c',
            'т': 'T',
            'у': 'y',
            'ф': 'O',
            'х': 'x',
            'ц': 'y',
            'ч': 'y',
            'ш': 'w',
            'ы': 'bl',
            'ь': 'b',
            'ю': 'h',
            'я': 'R',
            '–': '-',  # apparently not a normal hyphen ...
            '—': '-',  # apparently not a normal hyphen ...
            '’': '',
            '“': '',
            '”': '',
            '…': '_',
            '™': '',
            '▬': '',
            '▲': '',
            '▶': '',
            '►': '',
            '▼': '',
            '◄': '',
            '◈': '',
            '★': '_',
            '♥': '',
            '✅': '',
            '❤': '',
            '➤': '',
            '️': '',
            '🌶': '',
            '🎩': '',
            '🐇': ''}

ROOT = "/media/veracrypt1"  # "/home/output/.TMP/"  # "/run/media/martin/SAMSUNG"   # /.TMP/NEWS_1"
ZONEY = "/media/veracrypt1"

print(f"Valid: {VALID}")
print(f"NoVal: {''.join(SUBST.keys())}")

set_invalids = set()
num_invalids = 0

for root, dirs, files in os.walk(ROOT):
    path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        # print(len(path) * '---', file)
        if not all(c in VALID for c in file):  # If not a valid name
            lst_bad = sorted(list(set([c for c in file if c not in VALID])))
            lst_cnv = [ord(c) for c in lst_bad]
            set_invalids.update(lst_bad)
            num_invalids += 1
            if any(c not in SUBST.keys() for c in lst_bad):
                print(f" Bad char(s) {lst_bad}: {lst_cnv}: {root}{os.sep}{file}")
            else:  # Make a swap
                if root.startswith(ZONEY):
                    newf = file
                    for key_s in SUBST.keys():
                        newf = newf.replace(key_s, SUBST[key_s])
                    str_fno = root+os.sep+file
                    str_fnn = root+os.sep+newf
                    if str_fno !=str_fnn:
                        print(f"Renaming:\n< {str_fno}\n> {str_fnn}")
                        os.rename(str_fno, str_fnn)

print(f"num: {num_invalids}")
print(f"set: {sorted(list(set_invalids))}")
