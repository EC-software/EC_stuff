import os
import sys

rootdir = r"C:\Users\22016\Martin\repos"  # sys.argv[1]
target = "Music"

print(rootdir)
with open("filter_lines_out", "w") as filo:
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".py") and not any([filepath.find(tok) > 0 for tok in ['venv']]):
                print(filepath)
                with open(filepath, "r") as fili:
                    try:
                        for line in fili:
                            if target.lower() in line.lower():
                                filo.write(str(filepath)+"<<"+line)
                    except UnicodeDecodeError:
                        pass