

fn_in = r"C:\Users\22016\Martin\opg\19-03_AIS\AIS_dk_csv_may2018\aisdk_201805__dh_cln.csv"
fn_ou = r"C:\Users\22016\Martin\opg\19-03_AIS\AIS_dk_csv_may2018\aisdk_201805__dh_cln_fixlastline.csv"

dic_dip = dict()
cnt = 0
with open(fn_in, 'r') as fini:
    with open(fn_ou, 'w') as filo:
        for line in fini:
            try:
                aistype = line.split(',', 2)[1]
                filo.write(line)
            except:
                print("Can't handle line: |{}|".format(line))
    #         if not aistype in dic_dip.keys():
    #             dic_dip[aistype] = 1
    #         else:
    #             dic_dip[aistype] += 1
            cnt += 1
            if cnt%1000000 == 0:
                print(cnt)
#
# for keyi in sorted(dic_dip.keys()):
#     print("{} : {}".format(keyi, dic_dip[keyi]))