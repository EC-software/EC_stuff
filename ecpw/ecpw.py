#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Storing identity user-names, passwords and other info in a safe place, away from your repository and work-dir,
so it won't accidentally sync to bitbucket, github, dropbox or similar

The store is two level, top-level called 'identities', lower level called 'keys'

Store:
    itentity_1:
        key1 = value1
        key2 = value2
    identity_2:
        key1 = value3
        key2 = value4
        key3 = value5

identity-name must be unique in store
key-name must be unique within 'identity', but not in store

lst() - List all 'identity' names in store
add(i,j) - Adds an identity (i) to the store, and fill it with (j)
rem(i) - Removes an identity from the store
set(i,k,v) - Sets a value (v) to a key (k), in the identity (i)
get(i,k) - Returns the value for key (k) in identity (i)
clr(i,k) - Clears key and value of key (k) in identity (i)

Usage:
    1) ecpwb = ecpasswordbase.Base('/home/myuser/personalstuff/my_sectres.ecpwb')
    2) the_username = ecpwb.get('identity_id', 'user')
       the_password = ecpwb.get('identity_id', 'pw')
       the_moreinfo = ecpwb.get('identity_id', 'some_other_custom_parameter')
    3) you can go about your business...

Note: As we are using json all items must be string!!!

ToDo:
    Consider placing this file in: /usr/lib/python2.7/site-packages/
    Consider placing the .ecpwb in ~/.ecpwb
    Add logging
    Add encryption
    Consider using shelve (or marshal), rather than JSON?
"""

import os.path
import json

class Store(object):
    """ Storing identity user-names, passwords and other info in a safe place...
    Error codes:
        100-199: Internal code logic fail
        200-299: Errors associated with input data
    """

    ECPW_DATATYPE = "ECPW"
    ECPW_VERSION = "0.1"

    def __init__(self, str_filename=None, crypt=None):
        if not str_filename:
            str_filename = os.path.expanduser("~")+"/.ecpw"
        #self._datatype = self.ECPW_DATATYPE # For compatibility check
        #self._version = self.ECPW_VERSION # For compatibility check
        self._filen = str_filename  # So it knows where to dump itself...
        self._crypt = crypt  # No encryption supported, yet
        self._base = dict()  # The actual contents
        if not os.path.isfile(self._filen):
            self._new_file()
        else:
            self._load_file()

    # internal/private commands
    def _new_file(self):
        """ Initializes a new .ecpwb file """
        dic_out = dict()
        dic_out['ecpw_datatype'] = self.ECPW_DATATYPE # For compatibility check
        dic_out['ecpw_version'] = self.ECPW_VERSION # For compatibility check
        #dic_out['filen'] = self._filen
        dic_out['crypt'] = self._crypt
        dic_out['base'] = self._base
        json_load = json.dumps(dic_out, sort_keys=True, indent=4)
        with open(self._filen, "w") as fil:
            fil.write(json_load)
        with open(self._filen, "r") as fil:
            str_ret = fil.read()
        ret_load = json.loads(str_ret)
        if ret_load == dic_out:
            print "New file created successfully"
        else:
            print "!!! Error on reload new file 1:1 {}".format(self._filen)
            if json_load == str_ret:
                print "    but json == json, so it's likely just caused by non-string keys in input"
            return 210

    def _load_file(self):
        """ Load an existing .ecpwb file """
        # try to load info from file
        try:
            fil_load = open(self._filen, 'rb')
            dic_load = json.load(fil_load)
            fil_load.close()
        except:
            print "Can't load data from file: {} \nPlease check if file is empty...".format(self._filen)
            return 221
        # Check some dic_load vitals...
        if isinstance(dic_load, dict):
            if 'ecpw_datatype' in dic_load.keys():
                if dic_load['ecpw_datatype'] == self.ECPW_DATATYPE:
                    if 'ecpw_version' in dic_load.keys():
                        if dic_load['ecpw_version'] == self.ECPW_VERSION:
                            # Load the data
                            self._crypt = dic_load['crypt']  # No encryption supported, yet
                            self._base = dic_load['base']
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

    def _validate_key(self, keyi):
        """
        Validates a single key, val pair in an identity, in the store
        :param key:
        :return: True if valid, otherwise returns False
        """
        if isinstance(keyi, str):
            return True
        else:
            return False

    def _validate_identity(self, ident):
        """
        Validates a single identity...
        :param ident:
        :return:
        """
        if isinstance(ident, str) and isinstance(self._base[ident], dict):
            if all([self._validate_key(keyi) for keyi in self._base[ident].keys()]):
                return True
            else:
                print "identity Failed validation (2), it has invalid key"
                return False
        else:
            print "identity Falied validation (1), it's not a dictionary"
            return False

    def _validate_store(self):
        """ Validate the self 'store' objects with some sanity checks """
        if isinstance(self._base, dict):
            if all([self._validate_identity(ident) for ident in self._base]):
                return True
            else:
                print "store Failed validaton, it has invalid itentity"
                return False
        else:
            print "store Failed validatain, it's not a dictionary"
            return False

    def _upd_file(self):
        """ Update an existing .ecpwb file, with current self. """
        if self._validate_store():
            dic_upd = dict()
            dic_upd['ecpw_datatype'] = self.ECPW_DATATYPE
            dic_upd['ecpw_version'] = self.ECPW_VERSION
            dic_upd['crypt'] = self._crypt
            dic_upd['base'] = self._base
            json_load = json.dumps(dic_upd, sort_keys=True, indent=4)
            with open(self._filen, "w") as fil:
                fil.write(json_load)
            with open(self._filen, "r") as fil:
                str_ret = fil.read()
            ret_load = json.loads(str_ret)
            if ret_load == dic_upd:
                print "(upd_file) Update is successfully"
                return 0
            else:
                print "!!! Error on reload: JSON"
                if json_load == str_ret:
                    print "    but json == json, so it's likely just caused by non-string keys in input"
                return 230
        else:
            print "Can't update file, because store is not valid."

    # store level commands
    def print_raw(self):
        store = self._base
        print "< store:", str(type(store))
        if isinstance(store, dict):
            for keyi in store.keys():
                iden = store[keyi]
                print "<  iden:", str(type(iden)), keyi
                for keyj in iden.keys():
                    print "<  k-v: ({}, {}) =  {}, {}".format(str(type(keyj)),str(type(iden[keyj])),iden.keyi[keyj])

    # identity level commands
    def lst(self):
        """ List all 'identities' in the store """
        pass

    def add(self, str_key, dic_add):
        """ Add an identity to an existing .ecpwb file
        the identity must be in form of a dictionary, with all string keys.
        and the identity-key cant be on all ready used in self."""
        if isinstance(str_key, str):
            if isinstance(dic_add, dict):
                if not str_key in self._base.keys():
                    if all([isinstance(key_i, str) for key_i in dic_add.keys()]):
                        self._base[str_key] = dic_add
                    else:
                        print "Can't add identity because it contains key(s) that are not string"
                        return 244
                else:
                    print "Can't add identity because key all readay exists: {}".format(str_key)
                    return 243
            else:
                print "Can't add identity because it's not a dictionary, it is a: {}".format(str(type(dic_add)))
                return 242
        else:
            print "Can't add identity because the key in not string, it is: {}".format(str(type(str_key)))
            return 241
        self._upd_file()

    def rem(self, str_key):
        """ Remove an identity from an existing .ecpwb file """
        if str_key in self._base.keys():
            del self._base[str_key]
            self._upd_file()
            return 0
        else:
            print "Can't remove key: {}, because it's not there...".format(str_key)
            return 270

    # key level commands
    def get(self, str_key, str_inner_key):
        """ Retrieve a value by key from an identity from an existing .ecpwb file """
        if isinstance(str_key, str):
            if isinstance(str_inner_key, str):
                if str_key in self._base.keys():
                    if str_inner_key in self._base[str_key].keys():
                        return self._base[str_key][str_inner_key]
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

    def gets(self, str_key, lst_inner_keys):
        lst_ret = list()
        for keyi in lst_inner_keys:
            lst_ret.append(self.get(str_key, keyi))
        return lst_ret

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

    def clr(self, str_key, str_inner_key):
        pass
