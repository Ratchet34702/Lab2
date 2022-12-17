import requests
import matplotlib.pyplot as plt
import numpy as np
import json
import csv


response_doll = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20210101&end=20211231&valcode=usd&sort=exchangedate&order=asc&json");
response_euro = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20210101&end=20211231&valcode=eur&sort=exchangedate&order=asc&json")
json_doll = response_doll.json() 
json_euro = response_euro.json()

data_file = open('data_file.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(data_file)
 
# Counter variable used for writing
# headers to the CSV file
count = 0
 
for usd in json_doll:
    if count == 0:
 
        # Writing headers of CSV file
        header = usd.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    csv_writer.writerow(usd.values())
 
data_file.close()



date = np.array([])
doll = np.array([])
euro = np.array([])
for x in json_doll:
  date = np.append(date, x['exchangedate'])
  doll = np.append(doll, (x['rate']))
for x in json_euro:
  euro = np.append(euro, (x['rate']))

fig, ax = plt.subplots(1, 1, figsize=(12, 12))
ax.xaxis.set_ticks(np.arange(0, 365, 31))
ax.yaxis.set_ticks(np.arange(26, 36, 0.5))

labels = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
ax.set_xticklabels(labels)
plt.plot(date, doll, color = 'green')
plt.plot(date, euro, color = 'red')
plt.savefig('plot.png', bbox_inches='tight')
