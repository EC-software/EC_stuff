import os

str_root = "/home/output/.TMP/30" # """./"
num_min_size = 1048576 # 1Mb

for dirpath, dnames, fnames in os.walk(str_root):
    for f in fnames:
        if f.endswith(".mp4") or True:
            statinfo = os.stat(os.path.join(dirpath, f))
            if statinfo.st_size < num_min_size:
                print statinfo.st_size, (os.path.join(dirpath, f))