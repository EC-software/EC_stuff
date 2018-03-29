import datetime

dic_temp = dict()

with open('/home/martin/Downloads/pwned/pwned-passwords-2.0.txt', 'r') as fin:
    num_cnt = 0
    for line in fin:
        str_key = line[:3]
        if not str_key in dic_temp.keys():
            dic_temp[str_key] = list()
        dic_temp[str_key].append(line.strip())
        num_cnt += 1
        if num_cnt % 100000 == 0:
            print "{} dumping at: {}".format(datetime.datetime.now(),num_cnt)
            #for keyt in dic_temp:
                #print keyt, dic_temp[keyt]
                #filt = open(r"../data/pwn_{}.txt".format(keyt), 'w+')
                #filt.write()
            for str_tmp in dic_temp:
                with open("/home/martin/Downloads/pwned/split4096/pwnd_{}.txt".format(str_tmp), 'a') as the_file:
                    for lint in dic_temp[str_tmp]:
                        the_file.write(lint+'\n')
            dic_temp = dict()


