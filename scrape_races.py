from bs4 import BeautifulSoup
import requests
import csv
import time
import re
r = requests.get("http://www.typeracerdata.com/profile?username=nirajp&last=99999999")
data = r.text

start = time.time()
# with open("data/races.html" ,"r") as infile:
#     data = infile.read()
soup = BeautifulSoup(data, 'html.parser')

tables = soup.findAll('table')

# There are 3 tables on the page. We want the third one only.
table = tables[2]
headers = [header.text for header in table.find_all('th')]
print(headers)

rows = list()

for row in table.find_all('tr'):
    content = list()
    for i, col in enumerate(row.find_all('td')):
        if col.a and i==4:
            content.append(re.findall(r'id=([0-9]+)\&', col.a.get('href'))[0])
        else:
            content.append(col.text)
    rows.append(content)

with open("data/races.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    writer.writerows(row for row in rows if row)

print("Time taken: {}".format(time.time()-start))