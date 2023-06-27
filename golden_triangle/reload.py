
""" Reload the test data to initial situation,
    i.e. move all files from LAO and THA to MMR """

# after git filter-repo --force --strip-blobs-bigger-than 10M

import os
import shutil

KNOWN_METHODS = ["os.", "shutil.", "cmd"]


def movefile_byos(src, dst):
    print(f"Move: {src} --> {dst}, by os.")


def movefile_byshutil(src, dst):
    print(f"Move: {src} --> {dst}, by .shutil")
    shutil.copyfile(src, dst)


def movefile_bycmd(src, dst):
    print(f"Move: {src} --> {dst}, by cmd")


def moveall(str_fdn_from, str_fdn_to, method="none", ttt=3):
    """ move all files in dir_f to dir_t, No traveling sub-directories!
        using method (os., xxx. or cmd)
        ttt (time to try) default 3 """
    if method in KNOWN_METHODS:
        if method == "os.":
            for str_fn in os.listdir(str_fdn_from):
                movefile_byos(os.path.join(str_fdn_from, str_fn), os.path.join(str_fdn_to, str_fn))
        elif method == "shutil.":
            for str_fn in os.listdir(str_fdn_from):
                movefile_byshutil(os.path.join(str_fdn_from, str_fn), os.path.join(str_fdn_to, str_fn))
        elif method == "cmd":
            for str_fn in os.listdir(str_fdn_from):
                movefile_bycmd(os.path.join(str_fdn_from, str_fn), os.path.join(str_fdn_to, str_fn))
        else:
            raise ValueError(f"Error: something is out of wagg with method: {method} #2045")
    else:
        raise ValueError(f"Error: Unknown method: {method}")


def main():
    moveall("data/LAO", "data/MMR", "os.")
    moveall("data/THA", "data/MMR", "shutil.")
    moveall("data/XTR", "data/MMR", "cmd")


if __name__ == "__main__":
    main()