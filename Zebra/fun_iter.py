import itertools

lst_base = ['a', 'b', 'c', 'd', 'e']

n = 0
for cmb in itertools.permutations('abcde'):
    print(cmb)
    n += 1
print(n)


# def add1(lst_base, lst_cmb):
#     pass
#
# lst_ret = []
# lst_cmb = []
# for i in lst_base:
#     lst_cmb.append(i)
#     for j in [c for c in lst_base if c not in lst_cmb]:
#         lst_cmb.append(j)
#         for k in [c for c in lst_base if c not in lst_cmb]:
#             lst_cmb.append(k)
#             for l in [c for c in lst_base if c not in lst_cmb]:
#                 lst_cmb.append(l)
#                 for m in [c for c in lst_base if c not in lst_cmb]:
#                     lst_cmb.append(m)
#                     if len(set(lst_cmb)) == 5:
#                         lst_ret.append(lst_cmb)
#                         print(lst_cmb)
#                         # lst_cmb = []
# print(len(lst_ret))
# print(len(set(str(lst_ret))))
#
#
