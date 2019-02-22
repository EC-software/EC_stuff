import os
import sys

rootdir = sys.argv[1]
target = "Scandinavia"

print(rootdir)
with open("filter_lines_out", "w") as filo:
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".csv"):
                print(filepath)
                with open(filepath, "r") as fili:
                    for line in fili:
                        if target.lower() in line.lower():
                            filo.write(str(filepath)+"<<"+line)