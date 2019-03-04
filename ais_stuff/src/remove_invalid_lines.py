
import os

""" Remove invalid lines from all .csv files, assumed AIS files, in rootdir 

assume input where each line is a comma seperated list of:
    'Timestamp' string
    'Type of mobile' string
    'MMSI' bigint
    'Latitude' real
    'Longitude' real
    'Navigational status' string
    'ROT' real
    'SOG' real
    'COG' real
    'Heading' smallint
    'IMO' string
    'Callsign' string
    'Name' string
    'Ship type' string
    'Cargo type' string
    'Width' real
    'Length' real
    'Type of position fixing device' string
    'Draught' real
    'Destination' string
    'ETA' string
    'Data source type' string
"""


def tokenise_wm(str_in, chr_sep=',', chr_m='"'):

    def fetchnext(str_in_l, chr_sep, chr_m):
        if str_in_l[0] == chr_m:
            num_pos = str_in_l[1:].find(chr_m)
            str_n = str_in_l[:num_pos+2]
            str_i = str_in_l[num_pos+2:]
            if str_i[0] == ',':
                str_i = str_i[1:]
            return (str_n, str_i)
        elif chr_sep in str_in_l:
            return str_in_l.split(chr_sep, 1)
        else:
            return str_in_l, ""

    lst_ret = list()
    while len(str_in) > 0:
        str_next, str_in = fetchnext(str_in, chr_sep, chr_m)
        lst_ret.append(str_next)
    return lst_ret

rootdir = r"C:\Users\22016\Martin\opg\19-03_AIS\AIS_dk_csv_may2018b"
lst_int_values = [2,9]
lst_float_values = [3,4,6,7,8,15,16,18]
lst_ais_type = [1]

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".csv"):
            print (filepath)
            with open(filepath, 'r') as fili:
                with open(filepath.replace(".csv", "_cln.csv"), 'w') as filo:
                    with open(filepath.replace(".csv", "_bad.csv"), 'w') as filb:
                        cnt, cnt_dirty = 0, 0
                        for line in fili:
                            cnt += 1
                            bol_clean = True  # Assumed clean until proven dirty
                            line = line.strip()
                            lst_line = tokenise_wm(line, ',', '"')
                            if len(lst_line) != 22:  # Wrong number of columns
                                print("l: {} Wrong number of tokens in: {}".format(cnt, line))
                                bol_clean = False

                            for num_tok in lst_int_values:  # integers
                                if lst_line[num_tok] != '':
                                    try:
                                        int(lst_line[num_tok])
                                    except ValueError as e:
                                        print("{},{} cant make int({}): {}".format(cnt, num_tok, lst_line[num_tok], line))
                                        bol_clean = False

                            for num_tok in lst_float_values:  # floats
                                if lst_line[num_tok] != '':
                                    try:
                                        float(lst_line[num_tok])
                                    except ValueError as e:
                                        print("{},{} cant make float({}): {}".format(cnt, num_tok, lst_line[num_tok], line))
                                        bol_clean = False

                            for num_tok in lst_ais_type:  # AIS type
                                if lst_line[num_tok] != '':
                                    if not (isinstance(lst_line[num_tok], str)
                                        and len(lst_line[num_tok]) > 1
                                        and lst_line[num_tok] in ["AtoN","Base Station","Class A","Class B",
                                                                  "SAR Airborne", "Man Overboard Device",
                                                                  "Search and Rescue Transponder"]):
                                        print("{},{} cant recognise good AIS type({}): {}".format(cnt, num_tok, lst_line[num_tok], line))
                                        bol_clean = False

                            if bol_clean:
                                filo.write(line+"\n")  # No problems found, copy the line
                            else:
                                filb.write(line+"\n")  # Collect the bad lines here
                                cnt_dirty += 1
                print(" linecount: {} dirty: {} dirt%: {}".format(cnt, cnt_dirty, cnt_dirty*100/cnt))