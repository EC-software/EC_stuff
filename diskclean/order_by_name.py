import os
import pickle
import re

import dic_bab_update

dic_bab_update.define()

str_order = "/home/output/.TMP/NAM" # "./" # "/media/veracrypt1/NAM" #
str_chaos = "/home/output/.TMP/NEWS" # """./" # "/media/veracrypt1/NEWS" #
str_fn = 'dic_bab.ecp'

def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None

with open(str_fn, 'rb') as handle:
    dic_bab = pickle.load(handle)

print("dic_bab_length:", len(dic_bab.keys()))

lst_suc = list()
for dirpath, dnames, fnames in os.walk(str_chaos):
    for f in fnames:
        for hit in dic_bab:
            for pat in dic_bab[hit]:
                if all([tag.lower() in f.lower() for tag in pat]):
                    print("Hit: [{}] {} > {}".format(hit, pat, f))
                    lst_suc.append((hit, pat, (os.path.join(dirpath, f)), f.replace(' ','_')))
lst_suc.sort()

# Move
for suc in lst_suc:
    print("\n",suc)
    str_old = suc[2]

    # Check dir exists, or make
    str_dir = str_order+os.sep+suc[0]
    if not os.path.exists(str_dir):
        os.makedirs(str_dir)

    # Check file not exists
    str_new = str_dir+os.sep+suc[3]
    print(str_new)
    if not os.path.isfile(str_new):

        # Rename / Move
        try:
            os.rename(str_old, str_new)
            print("moved: {}".format(suc[3]))
        except:
            pass

    else:
        print("File exists: {}".format(str_new))
        if '.' in str_new:
            done = False
            while not done:
                print ">",
                str_lft, str_rgt = str_new.rsplit('.', 1)
                num_tail = get_trailing_number(str_lft)
                if num_tail:
                    str_lft = str_lft[:-len(str(num_tail))] + str(num_tail+1)  # Up the number by 1
                else:
                    str_lft = str_lft[:-len(str(num_tail))] + str(1)  # just put a 1 in the ind
                str_new = str_lft + '.' + str_rgt
                try:
                    os.rename(str_old, str_new)
                    print "renamed: {}".format(str_new)
                    done = True
                except:  # More specific error handeling here <---------------------------------------
                    pass
