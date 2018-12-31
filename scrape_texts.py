from bs4 import BeautifulSoup
import requests
import csv
import time

r = requests.get("http://www.typeracerdata.com/texts?texts=full&sort=id")
data = r.text

start = time.time()
# with open("data/texts.html" ,"r") as infile:
#     data = infile.read()
soup = BeautifulSoup(data, 'html.parser')

table = soup.find('table')

headers = [header.text for header in table.find_all('th')]
print(headers)

rows = list()
for row in table.find_all('tr'):
    rows.append([val.text for val in row.find_all('td')])

with open("data/texts.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    writer.writerows(row for row in rows if row)

print("Time taken: {}".format(time.time()-start))