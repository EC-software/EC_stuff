
import os

""" Call Graph
    For a given .py file. Find the start, and map all function calls, statically
    Just analyse the source, don't run it ... """

str_in_ffn = r"/home/martin/repos/oship/oship_kiss/ship_maintain/ship_luoti.py"  # start file
str_root_dir = os.sep.join(str_in_ffn.split(os.sep)[:-1])

print(f"root file: {str_in_ffn}")
print(f"root dir : {str_root_dir}")


def init_dot():
    """ Make list of strings, that will be the final .dot file """
    str_dot = """graph {
                   rankdir=LR; // Left to Right, instead of Top to Bottom
                }"""
    return [tok.strip() for tok in str_dot.split('\n')]


def main(str_start_ffn):
    lst_dot = init_dot()
    print(f"init dot: {lst_dot}")
    with open(str_start_ffn, 'r') as fil_s:
        print(f"reading file: {str_start_ffn}")
        lst_lines = [line.rstrip() for line in fil_s.readlines() if line != '\n']
    return lst_lines


if __name__ == "__main__":
    lst_lines = main(str_in_ffn)
    print(lst_lines)