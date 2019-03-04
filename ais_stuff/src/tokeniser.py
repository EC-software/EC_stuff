
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
            return (str_in_l, "")

    print("twm: 0: {},{},{}".format(str_in, chr_sep, chr_m))
    lst_ret = list()
    while len(str_in) > 0:
        str_next, str_in = fetchnext(str_in, chr_sep, chr_m)
        print("twm: 1: {} <> {} : {}".format(str_next, str_in, len(str_in)))
        lst_ret.append(str_next)
    return lst_ret

if __name__ == '__main__':
    lst_in = [
        '01/05/2018 00:52:42,AtoN,992191529,55.834082,4.561650,Unknown value,,,,,Unknown,,"VALDEMAR AA, AB",Undefined,,,,Undefined,,,,AIS',
        '01/05/2018 00:52:51,Class A,211330370,54.508568,13.635972,Moored,0.0,0.0,24.1,115,9210995,DIFE,"FAIRPLAY,25",Tug,,12,36,GPS,5.4,SASSNITZ,01/12/2018 00:00:00,AIS',
        '01/05/2018 00:54:01,AtoN,992191515,56.344700,4.271982,Unknown value,,,,,Unknown,,"HARALD A, B",Undefined,,,,Undefined,,,,AIS',
        '01/05/2018 00:54:06,AtoN,992191524,55.720382,4.799932,Unknown value,,,,,Unknown,,"TYRA EAST E, B",Undefined,,,,Undefined,,,,AIS',
        '01/05/2018 00:54:08,AtoN,992191511,55.530350,5.005782,Unknown value,,,,,Unknown,,"HALFDAN DA, DB, DC",Undefined,,,,Undefined,,,,AIS',
        '01/05/2018 00:54:17,AtoN,992191520,55.530932,4.908132,Unknown value,,,,,Unknown,,"SKJOLD A, B, C",Undefined,,,,Undefined,,,,AIS',
        '01/05/2018 00:54:22,AtoN,992191529,55.834082,4.561650,Unknown value,,,,,Unknown,,"VALDEMAR AA, AB",Undefined,,,,Undefined,,,,AIS',
        '01/05/2018 00:55:35,AtoN,992191524,55.720382,4.799932,Unknown value,,,,,Unknown,,"TYRA EAST E, B",Undefined,,,,Undefined,,,,AIS',
        '01/05/2018 00:55:37,AtoN,992191515,56.344700,4.271982,Unknown value,,,,,Unknown,,"HARALD A, B",Undefined,,,,Undefined,,,,AIS',
        '101/05/2018 00:55:42,AtoN,992191529,55.834082,4.561650,Unknown value,,,,,Unknown,,"VALDEMAR AA, AB",Undefined,,,,Undefined,,,,AIS',
        '01/05/2018 00:55:50,Class A,211330370,54.508568,13.635937,Moored,0.0,0.0,24.1,115,9210995,DIFE,"FAIRPLAY,25",Tug,,12,36,GPS,5.4,SASSNITZ,01/12/2018 00:00:00,AIS',
        '01/05/2018 00:57:01,AtoN,992191515,56.344700,4.271982,Unknown value,,,,,Unknown,,"HARALD A, B",Undefined,,,,Undefined,,,,AIS',
        '01/05/2018 00:57:06,AtoN,992191524,55.720382,4.799932,Unknown value,,,,,Unknown,,"TYRA EAST E, B",Undefined,,,,Undefined,,,,AIS',
    ]

    str_test = lst_in[0]
    lst_res = tokenise_wm(str_test, ',', '"')
    print(str_test, '\n', lst_res)