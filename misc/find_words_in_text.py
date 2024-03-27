
import os

ROOT = r'/home/martin/'  # r'D:\\'  # r'/home/martin/MEGA/Private'  #
EXT = '.py'  #'.csv'  #
SKIP = ['.mp3', '.mp4', '.pdf',
        '.js', '.css', '.ashx',
        '.jpg', '.png', '.gif',
        '.ods', '.odt', '.xls', '.doc', '.docx',
        '.7z', '.exe', '.dll']  # SKIP only used if EXT == '*'
MAXSIZE = 10000
WORDS = ['debug', 'INFO', 'WARNING', 'ERROR', 'FATAL']
CASE = False

def checkfor_words(lst_words, str_fn, mode='all'):
        num_ln = 0
        lst_lines_found = list()
        try:
            datafile = open(str_fn, 'r')
        except PermissionError:
            # pass
            print(f" - PermissionError: {str_fn}")
            return []
        except OSError:
            # pass
            print(f" - OSError: {str_fn}")
            return []
        try:
            for line in datafile:
                num_ln += 1
                if mode == 'all':
                    if CASE:
                        if all([w in line for w in lst_words]):
                            print(f"all: {lst_words}: {num_ln} < {line.strip()} in {str_fn}")
                            lst_lines_found.append(line.strip())
                    else:  # Not case sensitive
                        if all([w.lower() in line.lower() for w in lst_words]):
                            print(f"all: {lst_words}: {num_ln} < {line.strip()} in {str_fn}")
                            lst_lines_found.append(line.strip())
        except UnicodeDecodeError:
            pass
            # print(f" - UnicodeDecodeError: {str_fn}")
        except PermissionError:
            # pass
            print(f" - PermissionError: {str_fn}")
        return lst_lines_found

def main(str_root):
    num_cnt = 0
    num_hit = 0
    for root, dirs, files in os.walk(str_root):
        for file in files:
            num_cnt += 1
            if '.' in file:
                str_ext = '.' + file.rsplit('.', 1)[1]
            else:
                str_ext = ''
            if file.endswith(EXT) or (EXT == '*' and str_ext not in SKIP):
                str_ffn = os.path.join(root, file)
                # print(f"ffn: {str_ffn}")
                try:
                    if os.path.getsize(str_ffn) <= MAXSIZE:
                        # print(str_ext)
                        ffn = os.path.join(root, file)
                        # print(f"ffn: {str_ffn}")
                        num_hit += len(checkfor_words(WORDS, ffn))
                    else:
                        pass
                        # print(f"MAX: {str_ffn}")
                except FileNotFoundError:
                    # pass
                    print(f" - FileNotFoundError: {str_ffn}")

            if num_cnt == 1 or num_cnt % 100000 == 0:
                print(f"\tcnt: {num_cnt} - latest file: {os.path.join(root, file)}")
    print(f"\n {num_cnt} files scanned\n {num_hit} lines found")

if __name__ == '__main__':

    print(f"Start at: {ROOT} looking for {WORDS}")
    main(ROOT)