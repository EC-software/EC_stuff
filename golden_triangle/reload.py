
""" Reload the test data to initial situation,
    i.e. move all files from LAO and THA to MMR """

import os

KNOWN_METHODS = ["os.", "shutil.", "cmd"]


def movefile_byos(str_ffnfr, str_ffnto):
    print(f"Move: {str_ffnfr} --> {str_ffnto}, by os.")


def movefile_bycmd(str_ffnfr, str_ffnto):
    print(f"Move: {str_ffnfr} --> {str_ffnto}, by cmd")


def moveall(str_fdn_from, str_fdn_to, method="none", ttt=3):
    """ move all files in dir_f to dir_t, No traveling sub-directories!
        using method (os., xxx. or cmd)
        ttt (time to try) default 3 """
    if method in KNOWN_METHODS:
        if method == "os.":
            for str_fn in os.listdir(str_fdn_from):
                movefile_byos(os.path.join(str_fdn_from, str_fn), os.path.join(str_fdn_to, str_fn))
        elif method == "cmd":
            for str_fn in os.listdir(str_fdn_from):
                movefile_bycmd(os.path.join(str_fdn_from, str_fn), os.path.join(str_fdn_to, str_fn))
    else:
        raise ValueError(f"Error: Unknown method: {method}")


def main():
    moveall("data/LAO", "data/MMR", "os.")
    moveall("data/THA", "data/MMR", "cmd")


if __name__ == "__main__":
    main()