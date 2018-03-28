#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Storing identity usernames, passwords and other info in a safe place, away from your repository and work-dir,
so it won't accedentially sync to bitbucket, github, dropbox or similar
Usage:
    1) ecpwb = ecpasswordbase.Base('/home/myuser/personalstuff/my_sectres.ecpwb')
    2) the_username = ecpwb.get('identity_id', 'user')
       the_password = ecpwb.get('identity_id', 'pw')
       the_moreinfo = ecpwb.get('identity_id', 'some_other_custom_parameter')
    3) you can go about your business...

Note: As we are using json all items must be string!!!

ToDo:
    Add logging
    Add encryption
"""

import os.path
import json

class Base(object):
    """ Storing identity user-names, passwords and other info in a safe place...
    Error codes:
        100-199: Internal code logic fail
        200-299: Errors associated with input data
    """

    def __init__(self, str_filename, crypt="None"):
        self._version = "0.1"
        self._filen = str_filename
        self._crypt = crypt  # No encryption supported, yet
        self._dicdb = dict()
        self._empty = True
        self._valid = True
        if not os.path.isfile(self._filen):
            self._new()
        else:
            self._load()

    def _new(self):
        """ Initializes a new .ecpwb file """
        dic_new = dict()
        dic_new['datatype'] = "ECPWB"
        dic_new['version'] = self._version
        dic_new['filen'] = self._filen
        dic_new['crypt'] = self._crypt
        dic_new['dicdb'] = self._dicdb
        dic_new['empty'] = self._empty
        dic_new['valid'] = self._valid
        json_load = json.dumps(dic_new, sort_keys=True, indent=4)
        with open(self._filen, "w") as fil:
            fil.write(json_load)
        with open(self._filen, "r") as fil:
            str_ret = fil.read()
        ret_load = json.loads(str_ret)
        if ret_load == dic_new:
            print "JSON is identical"
        else:
            print "!!! Error on reload: JSON"
            if json_load == str_ret:
                print "    but json == json, so it's likely just caused by non-string keys in input"
            return 210
        return 0

    def _load(self):
        """ Load an existing .ecpwb file """
        # try to load info from file
        try:
            fil_load = open(self._filen, 'rb')
            dic_load = json.load(fil_load)
            fil_load.close()
        except:
            print "{} Can't load data from file: {}".format(__file__, self._filen)
            return 201
        # Check some dic_load vitals...
        if isinstance(dic_load, dict):
            if 'datatype' in dic_load.keys():
                if dic_load['datatype'] == "ECPWB":
                    if 'version' in dic_load.keys():
                        if dic_load['version'] == "0.1":
                            # Load the data
                            self._version = dic_load['version']
                            self._filen = dic_load['filen']
                            self._crypt = dic_load['filen']  # No encryption supported, yet
                            self._dicdb = dic_load['filen']
                            self._empty = dic_load['filen']
                            self._valid = dic_load['filen']
                        else:
                            print "{} Can't load file: {} since it's version {}".format(__file__, self._filen, dic_load['version'])
                            return 206
                    else:
                        print "{} Can't load file: {} since it has no version".format(__file__, self._filen)
                        return 205
                else:
                    print "{} Can't load file: {} due to datatype ECPWB != {}".format(__file__, self._filen, dic_load['datatype'])
                    return 204
            else:
                print "{} Can't load file: {} since it has no datatype".format(__file__, self._filen)
                return 203
        else:
            print "{} Can't load file: {} since it dosn't seem to contain a dict()".format(__file__, self._filen)
            return 202
        return 0

    def _validate(self):
        """ Validate the self objects with some sanity checks """
        return 0

    def add(self):
        """ Add an identity to an existing .ecpwb file """
        return 0

    def get(self):
        """ Retrieve an identity from an existing .ecpwb file """
        return 0

    def rem(self):
        """ Remove an identity from an existing .ecpwb file """
        return 0

    def upd(self):
        """ Update an identity in an existing .ecpwb file """
        return 0

