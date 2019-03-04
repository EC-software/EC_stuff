#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Walk root dir and find all types of .py headers
"""

import os
import sys
sys.path.append('../ec_base')
from ec_help import ec_cntdic as cntdic

str_root_dir = r"/home/martin/PycharmProjects"
str_extention = ".py"


def get_headers(str_ffn):
    lst_ret = list()
    bol_top = True
    with open(str_ffn, "r") as fil_j:
        for str_lin in fil_j:
            if bol_top and len(str_lin) > 0 and str_lin[0] == "#":
                lst_ret.append(str_lin)
            else:
                bol_top = False
    return lst_ret


cd = cntdic()
cnt_files = 0
for root, dirs, files in os.walk(str_root_dir):
    for fil_i in files:
        if fil_i.endswith(str_extention):
            str_ffn = os.path.join(root, fil_i)
            print("Looking in: {}".format(str_ffn))
            lst_hdrs = get_headers(str_ffn)
            print("          : {}".format(lst_hdrs))
            cd.add(str(lst_hdrs))
            cnt_files += 1
print("Looked in {} files".format(cnt_files))
#lst_hdrs = cd.by_cnt()
for lst_hdr in cd.by_cnt():
    print(lst_hdr)