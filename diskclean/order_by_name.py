import os
import pickle

str_order = "/home/output/.TMP/NAM" # """./"
str_chaos = "/home/output/.TMP/NEWS" # """./"
str_fn = 'dic_bab.ecp'

with open(str_fn, 'rb') as handle:
    dic_bab = = pickle.load(handle)

for dirpath, dnames, fnames in os.walk(str_chaos):
    for f in fnames:
        for hit in dic_bab:
