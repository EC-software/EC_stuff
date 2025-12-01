#!/usr/bin/env python
# -*- coding: ascii -*-

"""
EC-software
This small file demonstrates the typical everyday use of ecpw

Line 14: import the ecpw module
Line 15: create the ecpw object - this will automatically read your data from file
Line 18: get the 3 values, that we need for this program
Line 20: print the values, so we can verify that it worked. Almost too easy...
"""

import ecpw
ecs = ecpw.Store()

entry = 'demo_db'
db_ip, db_name, db_pw = ecs.gets(entry, ['ip', 'name', 'password'])

print(f"{entry} : {db_ip}, use credentials: {db_name} / {db_pw}")
