import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

print(page)

print("---------------")

print(page.content)

print("---------------")

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

with open("../Lab02-JavaScript.html") as fp:

    soup1 = BeautifulSoup(fp, 'html.parser')
print(soup1.prettify())