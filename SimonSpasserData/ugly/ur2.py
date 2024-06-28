
# mainly ChactGPT generated ... but considerably edited to purpose

import pprint

str_ffn_in = r"data/samp1.txt"

def read_ugly(file_path):
    lst_ret = list()
    with open(file_path, 'r') as file:
        lst_line = file.readlines()
    i = 0
    while i < len(lst_line):
        str_header = lst_line[i].strip()
        if any(char.isdigit() for char in str_header):
            print(f"Unexpected format: Line {i} should be text without numbers.")
            break
        i += 1
        str_note = lst_line[i].strip()
        if any(char.isdigit() for char in str_note):
            print(f"Unexpected format: Line {i} should be text without numbers.")
            break
        i += 1
        lst_coord = []
        while i < len(lst_line):
            line = lst_line[i].strip()
            if not any(char.isdigit() for char in line):
                break
            lst_coord.append(line)
            i += 1
        lst_ret.append((str_header, str_note, lst_coord))
    return lst_ret


def write_geojson(str_gj, str_ffn_ou):
    with open(str_ffn_ou, 'w') as fil_ou:
        fil_ou.write(f"{str_gj}\n")


def parse_coordinates(coord_list):
    coordinates = []
    coord_string = "".join(coord_list)  # smash them all together before parsing!
    coord_pairs = coord_string.split('/')
    for pair in coord_pairs:
        if ' ' in pair:
            x, y = pair.split(' ')
            try:
                coordinates.append([float(x), float(y)])
            except ValueError:
                # Handle potential parsing errors, such as trailing periods.
                pass
    return coordinates

def tup_ugly2geo_json(tup_u, dic_gj):


    title, note, coord_list = tup_u

    # Parse the coordinates
    coordinates = parse_coordinates(coord_list)

    if "features" not in dic_gj:
        dic_gj = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "title": title,
                        "note": note
                    },
                    "geometry": {
                        "type": "LineString",
                        "coordinates": coordinates
                    }
                }
            ]
        }
    else:
        dic_gj['features'].append({
                    "type": "Feature",
                    "properties": {
                        "title": title,
                        "note": note
                    },
                    "geometry": {
                        "type": "LineString",
                        "coordinates": coordinates
                    }
                })
    return dic_gj


lst_ugly = read_ugly(str_ffn_in)
dic_geojson = dict()
for itm in lst_ugly:
    # print(itm)
    str_h, str_n, lst_c = itm
    print("------")
    print(f"head: {str_h}")
    print(f"note: {str_n}")
    print(f"coor: {lst_c}")
    print("  >> GeoJSON")
    dic_geojson = tup_ugly2geo_json(itm, dic_geojson)
str_ffn_ou = f"{str_ffn_in.rsplit('.', 1)[0]}.geojson"
write_geojson(str(dic_geojson).replace("'", '"'), str_ffn_ou)
