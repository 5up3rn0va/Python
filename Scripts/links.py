from bs4 import BeautifulSoup
import requests

html = requests.get('http://10.10.213.94:8000/static/index.html')
soup = BeautifulSoup(html.text, "lxml")
links = soup.find_all('a')

for link in links:
    if "href" in link.attrs:
        print(link["href"])