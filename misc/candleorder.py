import datetime

print "Solutions:"

tim_beg = datetime.datetime.now()

for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                lst_co = [a, b, c, d]
                if len(set(lst_co)) == 4:
                    if abs(b-a) == 1:
                        if abs(c-b) == 1:
                            if abs(d-c) == 1:
                                print lst_co

tim_end = datetime.datetime.now()
print "duration", tim_end-tim_beg