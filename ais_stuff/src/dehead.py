

import os

""" Remove the first line from all .csv files in rootdir """

rootdir = r"C:\Users\22016\Martin\opg\19-03_AIS\AIS_dk_csv_may2018"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".csv"):
            print (filepath)
            bol_new = True
            with open(filepath, 'r') as fili:
                with open(filepath.replace(".csv", "dh.csv"), 'w') as filo:
                    for line in fili:
                        if bol_new:  # its the first line
                            bol_new = False
                            continue
                        else:
                            #if "some text" in line:
                            filo.write(line)