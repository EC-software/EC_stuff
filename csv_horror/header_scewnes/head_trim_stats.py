import os
import pprint

DATA_DIR = "./data"
EXTENSION = ".csv"


def coll_headers(str_dir, str_ext):
    """ read a bunch of csv files and generate a header to catch all headers """
    lst_heads = list()
    for dirpath, dnames, fnames in os.walk(str_dir):
        for f in fnames:
            if f.endswith(str_ext):
                with open(os.path.join(str_dir, f), 'r') as fil_in:
                    lst_heads.append(fil_in.readline().strip())
    return lst_heads


def one_union_header(lst_heads):
    set_fields = set()
    for head in lst_heads:
        set_fields.update([tok.strip() for tok in head.split(',')])
    return ", ".join(sorted(list(set_fields)))


def union_all_csv(str_dir, str_ext, str_uhead, str_fnou):
    """ """
    print("------ Union ----")
    with open(os.path.join(str_dir, str_fnou), 'w') as fil_ou:
        fil_ou.writelines(str_uhead + '\n')
        lst_uhead = [itm.strip() for itm in str_uhead.split(',')]
        for dirpath, dnames, fnames in os.walk(str_dir):
            for f in fnames:
                if f.endswith(str_ext):
                    n = 0
                    print(f" file: {f}")
                    with open(os.path.join(str_dir, f), 'r') as fil_in:
                        for line_in in fil_in:
                            if n == 0:  # Header
                                lst_head = [itm.strip() for itm in line_in.split(',')]
                                print(f"    {lst_head}")
                            else:
                                lst_in = [itm.strip() for itm in line_in.split(',')]
                                lst_ou = ["" for itm in lst_uhead]  # list of empties, same length as out header
                                for n in range(len(lst_uhead)):  # replacing the empties with data from input line
                                    fld_uni = lst_uhead[n]
                                    if fld_uni in lst_head:  # we have that field in this in file
                                        val = lst_in[lst_head.index(fld_uni)]
                                        lst_ou[lst_uhead.index(fld_uni)] = val
                                line_ou = ", ".join(lst_ou)
                                fil_ou.write(line_ou + '\n')
                                print(f"    {line_ou}")
                            n += 1


lst_headers = coll_headers(DATA_DIR, EXTENSION)
pprint.pprint(lst_headers)
str_uheader = one_union_header(lst_headers)
print(str_uheader)

union_all_csv(DATA_DIR, EXTENSION, str_uheader, "_union_.ucsv")