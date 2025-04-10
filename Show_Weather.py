import sqlite3
import requests
from bs4 import BeautifulSoup

url = 'https://tianqi.moji.com/weather/china'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/55.0.2883.87 Safari/537.36'}

bs = BeautifulSoup(requests.get(url).content)
alphabet = bs.find(name = 'dl', attrs={"class":'city_list clearfix'})
print(alphabet)
