
""" Iterable filter aka Leave only Gold
    loop through nested iterables and copy all to output,
    if the leaf passes the filter function.
    return a filtered copy of the iterable """


import pprint

import init_data

pprint.pprint(init_data.data)

def itarfilt_r(itar, filtfunc):
    """ Filter, recursively, an iterable
        valid is defined by filtfunc(leaf) == True """
    try:
        iter(itar)
        bol_isiterable = True
    except TypeError:
        bol_isiterable = False
    if bol_isiterable:
        for itm in itar:
            return


def itarfilt_l(itar, filtfunc):
    """ Filter, while looping, an iterable
        valid is defined by filtfunc(leaf) == True """
    return



