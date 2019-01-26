# -*- coding: utf-8 -*-

import os
import pickle
import re

STR_ORDER = "/home/output/.TMP/NAM" # "./" # "/media/veracrypt1/NAM" #
STR_CHAOS = "/home/output/.TMP/NEWS" # """./" # "/media/veracrypt1/NEWS" #
STR_CONFL = "/home/output/.TMP/NAME_CONFUSING"
STR_FN = 'dic_bab.ecp'

def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None

def move_soft(str_full_path_fn, str_full_path_dn):
    """ Move a file to a directory. Autp-rename if exists """
    ##print("*moving({}, {})".format(str_full_path_fn, str_full_path_dn))

    str_path_to = str_full_path_dn
    str_fn = str_full_path_fn.rsplit(os.sep, 1)[1]
    ##print(" str_path_to: {}".format(str_path_to))
    ##print(" str_fn: {}".format(str_fn))

    # remove spaces from filename
    str_fn = str_fn.replace(' ', '_')

    # Avoid existing files
    str_new = str_path_to+os.sep+str_fn
    while os.path.isfile(str_new):
        str_fn_lft, str_fn_rgt = str_fn.rsplit('.', 1)
        num_tail = get_trailing_number(str_fn_lft)
        if num_tail:
            str_fn_lft = str_fn_lft[:-len(str(num_tail))] + str(num_tail + 1)  # Up the number by 1
        else:
            str_fn_lft = str_fn_lft[:-len(str(num_tail))] + str(1)  # just put a 1 in the ind
        str_new = str_path_to + os.sep + str_fn_lft + '.' + str_fn_rgt

    # Move
    #try:
    print(" moving: {} > {}".format(str_full_path_fn, str_new))
    os.rename(str_full_path_fn, str_new)
    # except:
    #     print("XXX: {}".format(str_new))
    #     pass


# Open the pickle
with open(STR_FN, 'rb') as handle:
    dic_bab = pickle.load(handle)
print("dic_bab_length:", len(dic_bab.keys()))

# Prepare lists (unique and claim-conflict)
lst_hit = list()
for dirpath, dnames, fnames in os.walk(STR_CHAOS):
    for f in fnames:
        for hit in dic_bab:
            for pat in dic_bab[hit]:
                if all([tag.lower() in f.lower() for tag in pat]):
                    lst_hit.append({'hit': hit, 'fil': (os.path.join(dirpath, f)), 'pat': pat})
del dic_bab

dic_clm = dict()
for hit in lst_hit:
    if not hit['fil'] in dic_clm.keys():
        dic_clm[hit['fil']] = {'hit': [hit['hit']], 'pat': [hit['pat']]}
    else:
        dic_clm[hit['fil']]['hit'].append(hit['hit'])
        dic_clm[hit['fil']]['pat'].append(hit['pat'])
    dic_clm[hit['fil']]['cnt'] = len(set(dic_clm[hit['fil']]['hit']))
lst_unq = list()
lst_cnf = list()
for fil in dic_clm.keys():
    if dic_clm[fil]['cnt'] > 1:
        print("{} \n\t{} \n\t{} \n\t{}".format(fil, dic_clm[fil]['cnt'], list(set(dic_clm[fil]['hit'])), dic_clm[fil]['pat']))
        lst_cnf.append(fil)
    else:
        lst_unq.append((fil, dic_clm[fil]['hit']))

del dic_clm

# Move Unique
if not os.path.exists(STR_ORDER):
    os.makedirs(STR_ORDER)
for unq in lst_unq:
    ##print("#{}".format(unq))
    if not os.path.exists(STR_ORDER+os.sep+unq[1][0]):
        os.makedirs(STR_ORDER+os.sep+unq[1][0])
    move_soft(unq[0], STR_ORDER+os.sep+unq[1][0])

# Move Conflict
if not os.path.exists(STR_CONFL):
    os.makedirs(STR_CONFL)
for cnf in lst_cnf:
    print(cnf)
    move_soft(cnf, STR_CONFL)
