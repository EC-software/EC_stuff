import string

str_c = string.printable

print str(type(str_c)), len(str_c), str_c[:94]

for c in str_c:
    pass#print c, ord(c)

print str_c[93]