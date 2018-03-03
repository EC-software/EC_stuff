import os
import pickle

import dic_bab_update

dic_bab_update.define()

str_ossep = "/"
str_order = "/home/output/.TMP/NAM" # """./"
str_chaos = "/home/output/.TMP/NEWS" # """./"
str_fn = 'dic_bab.ecp'

with open(str_fn, 'rb') as handle:
    dic_bab = pickle.load(handle)

print "dic_bab_length:", len(dic_bab.keys())

lst_suc = list()
for dirpath, dnames, fnames in os.walk(str_chaos):
    for f in fnames:
        for hit in dic_bab:
            for pat in dic_bab[hit]:
                if all([tag.lower() in f.lower() for tag in pat]):
                    print "Hit: [{}] {} > {}".format(hit, pat, f)
                    lst_suc.append((hit, pat, (os.path.join(dirpath, f)), f.replace(' ','_')))
lst_suc.sort()

# Move
for suc in lst_suc:
    print "\n",suc
    str_old = suc[2]

    # Check dir exists, or make
    str_dir = str_order+str_ossep+suc[0]
    if not os.path.exists(str_dir):
        os.makedirs(str_dir)

    # Check file not exists
    str_new = str_dir+str_ossep+suc[3]
    print str_new
    if not os.path.isfile(str_new):

        # Rename
        try:
            os.rename(str_old, str_new)
            print "moved: {}".format(suc[3])
        except:
            pass

    else:
        print "File exists: {}".format(str_new)

