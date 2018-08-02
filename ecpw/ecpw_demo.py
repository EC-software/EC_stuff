"""
This small file demonstrates the typical everyday use of ecpw

Line 10: import the ecpw module
Line 11: create the ecpw object - this will automatically read your data from file
Line 13: get the 3 values, that we need for this program
Line 15: print the values, so we can verify that it worked. Almost too easy...
"""

import ecpw
ecs = ecpw.Store()

db_ip, db_name, db_pw = ecs.gets('demo_db', ['ip', 'name', 'password'])

print("For my work database: {}, use credentials: {} / {}".format(db_ip, db_name, db_pw))