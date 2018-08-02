"""
This will create a new personal ecpw file in your home directory.
The file will contain a dummy identity, provided as a template for you.

"""

import os.path
import ecpw

str_fn = os.path.expanduser("~")+"/.ecpw"
if not os.path.isfile(str_fn):
    ecs = ecpw.Store()
    ecs.add("template", {"user": "my_user_name", "pw": "my_secret_password"})
    ecs.add('demo_db', {"ip": "212.58.241.131", "name": "editor_chief", "password": "very_secret"})  # Used by ecpw_demo.py
else:
    print "File all ready exist: {}\nTo initialise a new .ecpw please first delete, or rename, the old one...".format(str_fn)

