#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Storing identity user-names, passwords and other info in a safe place, away from your repository and work-dir,
so it won't accidentally sync to bitbucket, github, dropbox or similar
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
            print "JSON Init is identical"
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
            return 221
        # Check some dic_load vitals...
        if isinstance(dic_load, dict):
            if 'datatype' in dic_load.keys():
                if dic_load['datatype'] == "ECPWB":
                    if 'version' in dic_load.keys():
                        if dic_load['version'] == "0.1":
                            # Load the data
                            self._version = dic_load['version']
                            self._filen = dic_load['filen']
                            self._crypt = dic_load['crypt']  # No encryption supported, yet
                            self._dicdb = dic_load['dicdb']
                            self._empty = dic_load['empty']
                            self._valid = dic_load['valid']
                        else:
                            print "{} Can't load file: {} since it's version {}".format(__file__, self._filen, dic_load['version'])
                            return 226
                    else:
                        print "{} Can't load file: {} since it has no version".format(__file__, self._filen)
                        return 225
                else:
                    print "{} Can't load file: {} due to datatype ECPWB != {}".format(__file__, self._filen, dic_load['datatype'])
                    return 224
            else:
                print "{} Can't load file: {} since it has no datatype".format(__file__, self._filen)
                return 223
        else:
            print "{} Can't load file: {} since it dosn't seem to contain a dict()".format(__file__, self._filen)
            return 222
        return 0

    def _validate(self):
        """ Validate the self objects with some sanity checks """
        return 0

    def _upd(self):
        """ Update an existing .ecpwb file, with current self._dicdb """
        self._validate()
        if self._valid:
            dic_upd = dict()
            dic_upd['datatype'] = "ECPWB"
            dic_upd['version'] = self._version
            dic_upd['filen'] = self._filen
            dic_upd['crypt'] = self._crypt
            dic_upd['dicdb'] = self._dicdb
            dic_upd['empty'] = self._empty
            dic_upd['valid'] = self._valid
            json_load = json.dumps(dic_upd, sort_keys=True, indent=4)
            with open(self._filen, "w") as fil:
                fil.write(json_load)
            with open(self._filen, "r") as fil:
                str_ret = fil.read()
            ret_load = json.loads(str_ret)
            if ret_load == dic_upd:
                print "JSON Update is identical"
                return 0
            else:
                print "!!! Error on reload: JSON"
                if json_load == str_ret:
                    print "    but json == json, so it's likely just caused by non-string keys in input"
                return 230

    def add(self, str_key, dic_add):
        """ Add an identity to an existing .ecpwb file
        the identity must be in form of a dictionary, with all string keys.
        and the identity-key cant be on all ready used in self."""
        if isinstance(str_key, str):
            if isinstance(dic_add, dict):
                if not str_key in self._dicdb.keys():
                    if all([isinstance(key_i, str) for key_i in dic_add.keys()]):
                        self._dicdb[str_key] = dic_add
                    else:
                        print "Can't add identity because it contains key(s) that are not string"
                        return 244
                else:
                    print "Can't add identity because key all readay exists: {}".format(str_key)
                    return 243
            else:
                print "Can't add identity because it's not a dictionary, its: {}".format(str(type(dic_add)))
                return 242
        else:
            print "Can't add identity because the key in not string, its: {}".format(str(type(str_key)))
            return 241
        self._upd()
        return 0

    def get(self, str_key, str_inner_key):
        """ Retrieve a value by key from an identity from an existing .ecpwb file """
        if isinstance(str_key, str):
            if isinstance(str_inner_key, str):
                if str_key in self._dicdb.keys():
                    if str_inner_key in self._dicdb[str_key].keys():
                        return self._dicdb[str_key][str_inner_key]
                    else:
                        print "Can't find key: {} in {}".format(str_inner_key, str_key)
                        return None
                else:
                    print "Can't find key: {}".format(str_key)
                    return None
            else:
                print "None-string type in key: {} in {}".format(str_inner_key, str_key)
                return None
        else:
            print "None-string type in key: {}".format(str_key)
            return None


    def set(self, str_key, str_inner_key, inner_val):
        """ Write (overwrite if exists) a value by key, to an identity to an existing .ecpwb file """
        dic_set = self.get(str_key, str_inner_key)
        if isinstance(str_inner_key, str):
            dic_set[str_inner_key] = inner_val
            self._upd()
            return 0
        else:
            print "None-string type in key: {} in {}".format(str_inner_key, str_key)
            return 260

    def rem(self, str_key):
        """ Remove an identity from an existing .ecpwb file """
        if str_key in self._dicdb.keys():
            del self._dicdb[str_key]
            self._upd()
            return 0
        else:
            print "Can't remove key: {}, because it's not there...".format(str_key)
            return 270
