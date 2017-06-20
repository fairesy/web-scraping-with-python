from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
beautifulSoupObject = BeautifulSoup(html, "html.parser")

nameList = beautifulSoupObject.findAll("span", {"class" : "green"})
for name in nameList:
    print(name.get_text())
