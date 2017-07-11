from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#https 페이지를 불러오기 위해 인증이 필요하다.
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen("https://www.ted.com/")
beautifulSoupObject = BeautifulSoup(html, "html.parser")
for link in beautifulSoupObject.findAll("a"):
    if "href" in link.attrs:
        print(link.attrs["href"])
