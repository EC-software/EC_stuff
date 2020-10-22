
import os

ROOT = r'C:\Users\22016\Martin\mega\Private'
EXT = '.csv'
WORDS = ['Hvidberg', 'Grøndahl']

def checkfor_words(lst_words, str_fn, mode='all'):
        lst_lines_found = list()
        datafile = open(str_fn, 'r')
        num_ln = 0
        for line in datafile:
            num_ln += 1
            # for word in lst_words:
            #     if word in line:
            #         lst_lines_found.append((num_ln, line))
            #         print(f"{word}: {num_ln} < {str_fn}")
            if mode == 'all':
                if all([w in line for w in lst_words]):
                    print(f"all: {lst_words}: {num_ln} < {line.strip()}")
        return lst_lines_found

def main(str_root):
    for root, dirs, files in os.walk(str_root):
        for file in files:
            if file.endswith(EXT):
                ffn = os.path.join(root, file)
                print((ffn))
                checkfor_words(WORDS, ffn)

if __name__ == '__main__':
    main(ROOT)