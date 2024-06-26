
""" Validate json and geojson """

import json

# import fiona
# import geojson

def valid_json(str_j):
    """ Validates on string, to test if it is valid JSON
    return False if any errors are found
    else return True """
    return json.loads(str_j)

def valid_geojson(xxx):
    """ Validates on string, to test if it is valid JSON
    return False if any errors are found
    else return True """
    return json.loads(xxx)

    # for feature in src:
    #     if not geojson.Feature(feature).is_valid or not src.validate_record_geometry(feature):
    #         raise RuntimeError("Feature is not valid")

filename = r"data/test50.geojson"

if filename.endswith('.json'):  # It's a .json file
    with open(filename, 'r') as fil_j:
        print(f"Valid: {valid_json(fil_j.read())}")
elif filename.endswith('.geojson'):  # It's a .geojson file
    with open(filename) as fil_g:
        print(f"Valid: {valid_json(fil_g.read())}")



