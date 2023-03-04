""" Generate sample data, csv files with random garbagedata, but taylored headers to test head_trim procedures """

import random
import string

lst_headers = [
    ["ID", "Name", "Year", "BIX"],
    ["ID", "Name", "Year", "BIX", "Colour"],
    ["ID", "Name", "Year", "BIX", "NAT", "NEP"],
    ["ID", "BIX", "Name", "Year"],
    ["Name", "Year", "ID", "BIX", "B", "W", "H"],
    ["Length", "Width"],
]

N = 2  # number of data in each file

for head in lst_headers:
    str_fn = ''.join(random.choices(string.ascii_lowercase, k=6)) + ".csv"
    print(f"file: {str_fn}")
    with open(str_fn, "w") as fil_ou:
        fil_ou.write(", ".join(head) + "\n")
        for n in range(N):
            lst_val = ["".join(random.choices(string.ascii_lowercase, k=4)) for m in head]
            line = ", ".join(lst_val)
            # print(line)
            fil_ou.write(line + "\n")