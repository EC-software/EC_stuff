
import math
import random

data = r"data/samp1.txt"

HEDRS = ["White-route", "Green-route", "Red-route", "Purple-route", "Orange-route"]
NOTES = ["Good for Horses", "Good for Simon", "Good for hiking", "Good for Running", "Good for Children"]

def fill_list(leapl=24, boxsize=1000, nmin=64, nmax=255):

    def leap(pnt_i, head, wobl, lp):
        hd = random.randrange(head-wobl, head+wobl)
        pnt_ox = round(pnt_i[0] + (lp * math.cos(hd)), 1)
        pnt_oy = round(pnt_i[1] + (lp * math.sin(hd)), 1)
        return (pnt_ox, pnt_oy)

    heading = random.randint(0, 359)
    wobling = random.randint(23, 135)
    pnt_nxt = (random.randint(0, boxsize), random.randint(0, boxsize))
    lst_pnt = list()
    for n in range(random.randint(nmin, nmax)):
        lst_pnt.append(pnt_nxt)
        pnt_nxt = leap(pnt_nxt, heading, wobling, leapl)
    return lst_pnt


with open(data, 'w') as fil_ou:
    for n in range(min(len(HEDRS), len(NOTES))):
        fil_ou.write(f"{HEDRS[n]}\n")
        fil_ou.write(f"{NOTES[n]}\n")
        lst_wps = fill_list()
        str_wps = "/".join([f"{itm[0]} {itm[1]}" for itm in lst_wps])

        chunks, chunk_size = len(str_wps), 64  # len(str_wps) // 24
        for cnk in [str_wps[i:i + chunk_size] for i in range(0, chunks, chunk_size)]:
            fil_ou.write(f"{cnk}\n")

        print(str_wps)
    print("Done...")
