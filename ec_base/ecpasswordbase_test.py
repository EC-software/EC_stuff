
import ecpasswordbase

ecp = ecpasswordbase.Base(r"/home/martin/Private/Secrets.ecpwb")
ecp.add('homeDB', {'name': 'myuser', 'pasw': 'verysecret', 'port': 1234})
my_pw_back = ecp.get('homeDB', 'pasw')
print my_pw_back
ecp.rem('workDB')
ecp.rem('homeDB')

print "\n"
for tok in dir(ecp):
    print tok

