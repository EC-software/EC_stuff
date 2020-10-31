#!/usr/bin/python

import os
import string

VALID = string.ascii_letters + string.digits + '_- .'
SUBST = {'$': 'S',
         '%': '_',
         '&': '_',
         "'": '_',
         '(': '_',
         ')': '_',
         '+': '_',
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
         'ä': 'ae',
         'é': 'e',
         'ü': 'u',
         'æ': 'ae',
         'Æ': 'AE',
         'ø': 'oe',
         'Ø': 'OE',
         'å': 'aa',
         'Å': 'AA',
         'ö': 'OE'
         }
print(f"Valid: {VALID}")
set_invalids = set()
num_invalids = 0

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("/home"):
    path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        # print(len(path) * '---', file)
        if not all(c in VALID for c in file):
            lst_bad = sorted(list(set([c for c in file if c not in VALID])))
            set_invalids.update(lst_bad)
            num_invalids += 1
            if any(c not in SUBST.keys() for c in lst_bad):
                print(f" % {lst_bad}: {file}")
print(f"num: {num_invalids}")
print(f"set: {sorted(list(set_invalids))}")
