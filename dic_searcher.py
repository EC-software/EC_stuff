from collections import OrderedDict  # the data appears to contain an OrderedDict.
import pprint


def recurse_object(obj_to_inspect, val_to_find, indexpath=""):
    if isinstance(obj_to_inspect, dict):
        for key, value in obj_to_inspect.items():
            recurse_object(value, val_to_find, indexpath + f"['{key}']")
    if isinstance(obj_to_inspect, list):
        for key, value in enumerate(obj_to_inspect):
            recurse_object(value, val_to_find, indexpath + f"[{key}]")
    if isinstance(obj_to_inspect, str):
        if obj_to_inspect == val_to_find:
            print(f"Value {val_to_find} found at {indexpath}")


dictionary = {'nestedA': OrderedDict(
    [('Name', 'TestCase'), ('VarA', 'Local'), ('VarB', None), ('VarC', None), ('VarD', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
     ('VarE', 'ABCD'), ('VarF', 10.0), ('VarG', False)]), 'nestedB': OrderedDict([('LocA', {'v1': 'ABCD', 'v2': None,
                                                                                            'v3': None, 'v4': [
        [[0, 1], [1, 1], [2, 2], [0, 4]], [[0, 2], [1, 2], [2, 3], [4, 4]], ['name', 'ABCD']]}), ('LocB', None),
                                                                                  ('LocC', None), ('LocD', True),
                                                                                  ('LocE', True), ('LocF', False),
                                                                                  ('LocG', False)])}
recurse_object(dictionary, 'ABCD')
pprint.pprint(dictionary)