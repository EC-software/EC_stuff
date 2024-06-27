import csv

target = '220434000'


with open('C:/Users/22016/Desktop/aisdk-2023-08-09.csv') as fil_in:
    reader = csv.reader(fil_in)
    with open(f'C:/Users/22016/Desktop/{target}-2023-08-09.csv', 'w') as fil_ou:
        n = 0
        for row in reader:
            #lst_in = row.split(',')
            if row[2] == target:
                print(row)
                fil_ou.write(f"{row} \n")
            n += 1
            # if n > 999999:
            #     break
print(f"Found: {n} records ...")