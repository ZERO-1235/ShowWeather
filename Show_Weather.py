import sqlite3
import requests
from bs4 import BeautifulSoup

class city:
    def __init__(self, name):
        self.name = name
        self.weather = None
        self.temp = None
        self.wind = None

url = 'https://tianqi.moji.com/weather/china'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/55.0.2883.87 Safari/537.36'}

bs = BeautifulSoup(requests.get(url, headers = headers).content, 'html.parser')
alphabet = bs.find(name = 'div', attrs={"class":'city clearfix'})
#print(alphabet)

prov = dict()
for item in alphabet.find_all('a'):
    prov_url = str(item['href'])
    zh_name = item.text
    prov[zh_name] = prov_url
#print(prov)

province = input('请输入省份：')
while province not in prov:
    province = input('没有该省份，请重新输入:')
    if province == '0':
        break
province_url = 'https://tianqi.moji.com' + prov[province]
#print(province_url)

prov_bs = BeautifulSoup(requests.get(province_url, headers = headers).content, 'html.parser')
prov_alphabet = prov_bs.find(name = 'div', attrs={"class":'city_hot'})
city_list = dict()
for item in prov_alphabet.find_all('a'):
    city_url = str(item['href'])
    zh_name = item.text
    city_list[zh_name] = city_url
#print(city_list)

city = input('请输入城市：')
while city not in city_list:
    city = input('没有该城市，请重新输入:')
    if city == '0':
        break
city_url =city_list[city]
#print(city_url)

