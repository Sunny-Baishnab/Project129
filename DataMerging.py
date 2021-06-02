import csv
data1 = []
data2 = []

with open('stars.csv','r') as f:
    reader = csv.reader(f)
    for data in reader:
        data1.append(data)

headers1 = data1[0]
headers1[0] = 'row_num'
stars_data1 = data1[1:]

with open('simplified.csv','r') as f:
    reader = csv.reader(f)
    for data in reader:
        data2.append(data)

headers2 = data2[0]
headers2[0] = 'row_num'
stars_data2 = data2[1:]

finalheaders = headers1+headers2
final_stars_data = []

for index,data in enumerate(stars_data1):
    final_stars_data.append(stars_data1[index]+stars_data2[index])

with open('final_star_data.csv','a+') as f:
    writer = csv.writer(f)
    writer.writerow(finalheaders)
    writer.writerows(final_stars_data)