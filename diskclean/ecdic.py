#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Maintain .ecdir file of a dir
    Modes:
        init: Create new .ecdic file. Overwrites an existing .ecdic file
        status: compare present state with .ecdir file. Newer changes .ecdir
        update: Change the .ecdir to reflect current state of dir
    Usage
        ecdir status|update (dir_name)
"""

import os
import argparse
import pickle
import datetime
import ec_hash

NUM_MIN_SIZE = 1048576 # 1Mb
VERBOSE_SILENT = 0
VERBOSE_ERROR = 2
VERBOSE_WARNING = 4
VERBOSE_INFO = 6
VERBOSE_CHATTY = 8
VERBOSE_DEBUG = 10

def dir_2_dic(str_root, verbose, exeptions=('.7z', '.csmsp')):
    dic_ret = dict()
    for dirpath, dnames, fnames in os.walk(str_root):
        for f in fnames:
            if any([f.endswith(ext) for ext in exeptions]):
                continue
            else:
                str_fullpath = os.path.join(dirpath, f)
                statinfo = os.stat(str_fullpath)
                if statinfo.st_size < NUM_MIN_SIZE:  # True: #
                    hash = ec_hash.file_hash(str_fullpath, 'md5')
                    dic_ret[str_fullpath] = dict()
                    dic_ret[str_fullpath]['stat'] = statinfo
                    dic_ret[str_fullpath]['hash'] = hash
                if verbose >= VERBOSE_CHATTY:
                    print str_fullpath, hash
    return dic_ret


def ecdic_save(dic_dir, str_fn, verbose):
    """ Save a ecdic to a file """
    if verbose >= VERBOSE_INFO:
        print "Saving to file: {}".format(str_fn)
    pickle.dump(dic_dir, open(str_fn, "wb"))
    return


def ecdic_load(str_fn, verbose):
    """ Load a ecdic from a file """
    return pickle.load(open(str_fn, "rb"))


def init(dir, verbose):
    """ Initializes a new .ecdic"""
    if verbose >= VERBOSE_INFO:
        print "Initializing a new .ecdir file"
    dic_dir = dir_2_dic(dir, verbose)
    ecdic_save(dic_dir, dir+r'/.ecdir', verbose)
    # Chec the file by reading it back in...
    ret_load = ecdic_load(dir+r'/.ecdir', verbose)
    if ret_load == dic_dir:
        if verbose >= VERBOSE_INFO:
            print "Pickle is identical"
    else:
        if verbose > VERBOSE_SILENT:
            print "!!! Error on reload: Pickle"
    return

def status(dir, verbose):

    return

def update(dir, verbose):
    """ Updates the .ecdic, but only for new and changed files """

    return

if __name__ == "__main__":

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--init", action="store_true")
    group.add_argument("-s", "--status", action="store_true")
    group.add_argument("-u", "--update", action="store_true")
    ap.add_argument("-d", "--directory", required=False, default="./", help="the stat directory")
    ap.add_argument("-v", "--verbose", required=False, default=0, help="verbosity [0..9], where 0 is silent and 9 is chatty")
    args = vars(ap.parse_args())
    print args

    if args['init']: # Initialize the .ecdir
        init(args['directory'], args['verbose'])
    elif args['status']: # Show state of a dir compared to it's .ecdir
        status(args['directory'], args['verbose'])
    elif args['update']:# Update the .ecdir to reflect the current state of the dir
        update(args['directory'], args['verbose'])
    else:
        if args['verbose'] > VERBOSE_SILENT:
            print "Unknown node... You should never see this!"
