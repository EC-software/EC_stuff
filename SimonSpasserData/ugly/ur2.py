
# mainly ChactGPT generated ... but considerably edited to purpose

str_ffn_in = r"in_file_name.txt"

def read_ugly(file_path):
    lst_ret = list()
    with open(file_path, 'r') as file:
        lst_line = file.readlines()
    i = 0
    while i < len(lst_line):
        str_header = lst_line[i].strip()
        str_note = lst_line[i].strip()
        i += 2
        lst_coord = []
        while i < len(lst_line):
            line = lst_line[i].strip()
            if not any(char.isdigit() for char in line):
                break  # This is a bold ChatGCP assumption - If a title contains a number, this will fail miserably!
            lst_coord.append(line)
            i += 1
        lst_ret.append((str_header, str_note, lst_coord))
    return lst_ret


def write_geojson(str_gj, str_ffn_ou):
    with open(str_ffn_ou, 'w') as fil_ou:
        fil_ou.write(f"{str_gj}\n")


def tup_ugly2geo_json(tup_u, dic_gj):

    def parse_coor(lst_coor):
        coord_string = "".join(coord_list)  # smash them all together before parsing!
        return [[float(itm) for itm in reversed(pair.split(' '))] for pair in coord_string.split('/') if ' ' in pair]

    title, note, coord_list = tup_u
    if "features" not in dic_gj:
        dic_gj = {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {"title": title, "note": note},
                "geometry": {"type": "LineString", "coordinates": parse_coor(coord_list)}}
            ]}
    else:
        dic_gj['features'].append({
            "type": "Feature",
            "properties": {"title": title, "note": note},
            "geometry": {"type": "LineString", "coordinates": parse_coor(coord_list)}}
        )
    return dic_gj


lst_ugly = read_ugly(str_ffn_in)
dic_geojson = dict()
for itm in lst_ugly:
    str_h, str_n, lst_c = itm
    print(f"------\n head: {str_h}\n note: {str_n}\n coor: {lst_c}\n  >> GeoJSON")
    dic_geojson = tup_ugly2geo_json(itm, dic_geojson)
str_ffn_ou = f"{str_ffn_in.rsplit('.', 1)[0]}.geojson"
write_geojson(str(dic_geojson).replace("'", '"'), str_ffn_ou)
