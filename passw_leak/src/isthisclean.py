#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
7C4A8D09CA3762AF61E59520943DC26494F8941B:20760336 = 123456
F7C3BC1D808E04732ADF679965CCC34CA7AE3441:7016669
B1B3773A05C0ED0176787A4F1574FF0075F7521E:3599486 = qwerty
5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8:3303003 = password
3D4F2BF07DC1BE38B20CD6E46949A1071F9D0E3D:2900049
7C222FB2927D828AF22F592134E8932480637C0D:2680521 = 12345678
6367C48DD193D56EA7B0BAAD25B19455E529F5EE:2670319 = abc123
E38AD214943DAAD1D64C102FAEC29DE4AFE9DA3D:2310111
20EABE5D64B0E216796E834F52D61FD0B70332FC:2298084
8CB2237D0679CA88DB6464EAC60DA96345513964:2088998 = 12345
"""

import hashlib

#print hashlib.sha1('password').hexdigest().upper()

def check1(word=""):
    itc = word
    has = hashlib.sha1(itc).hexdigest().upper()
    #print "Looking for:", has
    key = has[:3]
    fnm = r"/home/martin/Downloads/pwned/split4096/pwnd_{}.txt".format(key)
    #print fnm
    with open(fnm, 'r') as fin:
        hit = False
        cnt = 0
        for lin in fin:
            val = lin.split(':', 1)[0]
            if has == val:
                hit = lin
                break
            cnt += 1
    if hit:
        print "You are hit: {} on  \t|{}|".format(lin.strip(), itc)
    else:
        print "Checked {} lines with no hit for                        :-)\t|{}|".format(cnt, itc)

def check_file():
    list_my_words = []
    with open(r"/home/martin/Private/pawn.txt", 'r') as fin:
        for line in fin:
            list_my_words.append(line.split('#', 1)[0].strip())
    for wor in list_my_words:
        check1(wor)

#check_file()

check1('1234')

print "Done..."