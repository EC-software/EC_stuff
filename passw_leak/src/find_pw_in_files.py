
import os

lst_suspects = list()
# lst_suspects.extend(['password', 'passw', 'pword', 'pw '])
lst_suspects.extend(['Cinfadel', 'Zyra', 'Marianne'])
lst_suspects.extend(['myrica', 'fiveb', 'ovod.', 'Flipper', 'flipper', 'bbbbb', 'bix_user', 'b004218', 'mahvi'])
# lst_suspects.extend(['psycopg2.connect'])
str_root = r"/home/martin/repos"
# str_root = r"C:\Users"
lst_skip_ext = ['exe', 'zip', '7z', 'html', 'jpg', 'pack', 'las', 'shp', 'shx']

def checkfor_words(lst_words, str_fn):
        lst_lines_found = list()
        try:
            datafile = open(str_fn, 'r')
        except OSError:
            return lst_lines_found
        except PermissionError:
            return lst_lines_found
        except FileNotFoundError as e:
            print(f"Strange ERR. Can't find: {os.path.join(root, file)}: {e}")
            return lst_lines_found
        num_ln = 0
        try:
            for line in datafile:
                num_ln += 1
                for word in lst_words:
                    if word in line:
                        lst_lines_found.append((num_ln, line))
                        print(f"Arrest: {word}: {num_ln} < {str_fn}")
        except UnicodeDecodeError:
            pass
        except PermissionError:
            pass
        return lst_lines_found

dic_cnt_ext = dict()
lst_arrests = list()

for root, dirs, files in os.walk(str_root):
    for file in files:
        if file.endswith(".pack"):
             pass  # print((os.path.join(root, file)))
        # Count files by extention
        try:
            ext = file.rsplit('.', 1)[1]
        except:
            ext = "?"
        if not ext in lst_skip_ext:
            try:
                siz = os.path.getsize(os.path.join(root, file))
            except FileNotFoundError as e:
                print(f"Strange ERR. Can't find: {os.path.join(root, file)}: {e}")
                siz = 0  # just to be safer ...
            if ext not in list(dic_cnt_ext.keys()):
                dic_cnt_ext[ext] = [1, siz]
            else:
                dic_cnt_ext[ext][0] += 1
                dic_cnt_ext[ext][1] += siz
            # Actually check for words
            ##print("> Checking: {} size: {}".format(os.path.join(root, file), siz))
            lst_hits = checkfor_words(lst_suspects, os.path.join(root, file))
            if len(lst_suspects) > 0:
                for hit in lst_hits:
                    lst_arrests.append([os.path.join(root, file), hit])

# # List filecount by extension
# lst_trio = list()
# for keye in sorted(dic_cnt_ext.keys()):
#     print("{} : {}".format(keye, dic_cnt_ext[keye]))
#     lst_trio.append((keye, dic_cnt_ext[keye][0], dic_cnt_ext[keye][1]))
# def getKey(item):
#     return item[2]
# lst_trio.sort(key=getKey, reverse=True)
# print(lst_trio)

# print("Hits: {}".format(len(lst_arrests)))
# for arr in lst_arrests:
#     print(arr)