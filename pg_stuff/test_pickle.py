import pickle
d = { "c1400067" : { "mahvi" : { "pw" : "secret"}},  "c1503681" : { "mahvi" : { "pw" : "secret"}}}
afile = open(r'data/connect_info.ecp', 'wb')
pickle.dump(d, afile)
afile.close()

#reload object from file
file2 = open(r'data/connect_info.ecp', 'rb')
new_d = pickle.load(file2)
file2.close()

#print dictionary object loaded from file
print new_d