#!/usr/bin/python

import os
import string

VALID = string.ascii_letters + string.digits + '_- .'
SUBST = {'$': 'S',
         '!': '_',
         '¡': '_',
         '…': '_',
         '%': '_',
         '&': '_',
         '#': '_',
         "'": '_',
         '`': '',
         '´': '',
         '’': '',
         '(': '_',
         ')': '_',
         '+': '_',
         '★': '_',
         '¤': '_',
         '±': '_',
         '=': '_',
         ',': '_',
         ',': '_',
         ':': '_',
         ';': '_',
         '@': '_',
         '[': '_',
         ']': '_',
         '{': '_',
         '}': '_',
         '«': '_',
         '»': '_',
         '~': '-',
         '–': '-',  # apparently not a normal hyphen ...
         '—': '-',  # apparently not a normal hyphen ...
         'À': 'A',
         'á': 'a',
         'à': 'a',
         'ã': 'a',
         'ç': 'c',
         'е': 'e',  # apparently not a normal e ...
         'é': 'e',
         'ë': 'e',
         'É': 'E',
         'è': 'e',
         'é': 'e',
         'ß': 'ss',
         'ê': 'e',
         'í': 'i',
         'к': 'k',
         'ó': 'o',
         'ü': 'u',
         'у': 'y',
         'æ': 'ae',
         'Æ': 'AE',
         'Ä': 'AE',
         'ä': 'ae',
         'ø': 'oe',
         'Ø': 'OE',
         'Ö': 'OE',
         'å': 'aa',
         'Å': 'AA',
         'ö': 'OE',
         'А': 'A',  # Russian?
         'В': 'B',  # Russian?
         'Д': 'D',  # Russian?
         'Е': 'E',  # Russian?
         'Ж': 'X',  # Russian?
         'И': 'N',  # Russian?
         'Й': 'N',  # Russian?
         'К': 'K',  # Russian?
         'Н': 'H',  # Russian?
         'О': 'O',  # Russian?
         'Р': 'P',  # Russian?
         'С': 'C',  # Russian?
         'Г': 'R',  # Russian?
         'Ч': 'y',  # Russian?
         'Ы': 'bl',  # Russian?
         ',': ',',
        'а': 'a',
        'б': 'd',
        'в': 'B',
        'е': 'e',
        'ж': 'X',
        'и': 'n',
        'й': 'n',
        'к': 'k',
        'л': 'r',
        'н': 'H',
        'о': 'o',
        'п': 'n',
        'р': 'p',
        'с': 'c',
        'т': 'T',
        'у': 'y',
        'х': 'x',
        'ц': 'y',
        'ю': 'h',
        'я': 'R',
         '™': '',
         '🎩': '',
         '🐇': '',
         '▶': '️',
         '▶': '',
         '❤': '',
         '♥': '',
         '✅': '',
         '\u9654': '',
         '\u65039': '',
         '\u2009': '',
         '\u200a': '',
         '\u200b': '',
         '\u200c': '',
         '\u200d': '',
         '\u202c': '',
         '\xa0': ''
         }
ROOT = "/home/output/.TMP/"  # "/run/media/martin/SAMSUNG"   # /.TMP/NEWS_1"
ZONEY = "/home/output/.TMP/"

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
                    print(f"\n< {str_fno}\n> {str_fnn}")
                    os.rename(str_fno, str_fnn)

print(f"num: {num_invalids}")
print(f"set: {sorted(list(set_invalids))}")
