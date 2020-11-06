#!/usr/bin/python

import os
import string

VALID = string.ascii_letters + string.digits + '_- .'
SUBST = {'$': 'S',
         '!': '_',
         '%': '_',
         '&': '_',
         '#': '_',
         "'": '_',
         '`': '',
         '(': '_',
         ')': '_',
         '+': '_',
         '=': '_',
         ',': '_',
         ':': '_',
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
         'á': 'a',
         'ä': 'ae',
         'é': 'e',
         'è': 'e',
         'ê': 'e',
         'ü': 'u',
         'æ': 'ae',
         'Æ': 'AE',
         'ø': 'oe',
         'Ø': 'OE',
         'å': 'aa',
         'Å': 'AA',
         'ö': 'OE'
         }
ZONEY = "/home/output/.TMP/NEWS_1"

print(f"Valid: {VALID}")
print(f"Subst: {''.join(SUBST.keys())}")

set_invalids = set()
num_invalids = 0

for root, dirs, files in os.walk("/home/output"):  # /.TMP/NEWS_1"):
    path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        # print(len(path) * '---', file)
        if not all(c in VALID for c in file):  # If not a valid name
            lst_bad = sorted(list(set([c for c in file if c not in VALID])))
            set_invalids.update(lst_bad)
            num_invalids += 1
            if any(c not in SUBST.keys() for c in lst_bad):
                print(f" ! {lst_bad}: {root}{os.sep}{file}")
            else:  # Make a swap
                if root.startswith(ZONEY):
                    print(f" swapping: {'x'}")
print(f"num: {num_invalids}")
print(f"set: {sorted(list(set_invalids))}")
