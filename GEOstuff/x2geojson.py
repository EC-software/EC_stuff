
import re

str_fn = r"data/NEP_PLA_coordinates_s1.txt"

with open(str_fn, 'r') as fil_in:
    lst_data = fil_in.readlines()

geomodes = ["Points", "Lines", "Areas"]
geomode = ""  # Expected values are geomodes
for lin in [itm.strip() for itm in lst_data]:
    # print(f"|{lin}|")
    str_data = lin.split('#', 1)[0].strip()
    if len(str_data) > 0:
        print(f"+{str_data}")
        if '*' in str_data:
            geomode = str_data.strip('*').strip()
            if geomode in geomodes:
                print(f"% GeoMode = {geomode}")
            else:
                print(f"GeoModeError :: Unknown GeoMode: {geomode}")
                raise ValueError
        else:
            if bol_header_next:
                lst_header = str_data.split(':', 1)
                str_name = lst_header[0]
                lst_coords = []  # Clear the list
                if len(lst_header) > 1:
                    str_note = lst_header[1]
                else:
                    str_note = ""
                print(f"header:: {str_name}; str")
            else:  # Non-header line
                numbers = re.findall('\d+', str_data)  # finds all the numbers in the string
                result = list(map(int, numbers))  # converts the numbers to integers and puts them in a list

    else:
        bol_header_next = True