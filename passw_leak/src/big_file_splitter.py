import datetime

bol_small_files = False
bol_cnt_hex_3 = False
bol_print_one = True

# Prep. the dic
dic_temp = dict()
lst_chrs = "0123456789abcdef"
lst_lbls = [a+b+c for c in lst_chrs for b in lst_chrs for a in lst_chrs]
ecc = dict()
for labl in lst_lbls:
    dic_temp[labl] = 0

with open('/home/martin/Downloads/pwned/pwned-passwords-2.0.txt', 'r') as fin:
    num_cnt = 0
    for line in fin:
        line = line.lower()
        num_cnt += 1
        if num_cnt % 100000 == 0:
            print "{} dumping at: {}".format(datetime.datetime.now(),num_cnt)
        if bol_small_files:  # Split in small files
            str_key = line[:3]
            if not str_key in dic_temp.keys():
                dic_temp[str_key] = list()
            dic_temp[str_key].append(line.strip())
            for str_tmp in dic_temp:
                with open("/home/martin/Downloads/pwned/split4096/pwnd_{}.txt".format(str_tmp), 'a') as the_file:
                    for lint in dic_temp[str_tmp]:
                        the_file.write(lint+'\n')
            dic_temp = dict()
        if bol_cnt_hex_3:  # Count the keys
            dic_temp[line[:3]] += 1
        if bol_print_one:  # Simply print any line with this key...
            str_key = line[:3]
            if str_key.lower() == 'fff':
                print line.strip()

if bol_cnt_hex_3:
    print [(k, dic_temp[k]) for k in sorted(dic_temp)]

