from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

all_divs = soup.find_all('span',attrs={'id':'KOSPI_now'})
all_divs += soup.find_all('h3',attrs={'class':'blind'})
all_divs += soup.find_all('span',attrs={'id':'time3'})

res = [span.string for span in all_divs]

for i in res:
    print(i)