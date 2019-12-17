
import requests
from bs4 import BeautifulSoup

with open("../Lab02-JavaScript.html") as fp:

    soup = BeautifulSoup(fp, 'html.parser')

rows = soup.findAll("tr")
for row in rows:
    cols = row.findAll("td")
    datalist = []
    for col in cols:
         datalist.append(col.text)
    print(datalist)

