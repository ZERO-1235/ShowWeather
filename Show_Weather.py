import sqlite3
import requests
from bs4 import BeautifulSoup

class City:
    def __init__(self):
        self.name = None
        self.url = None
        self.weather = None
        self.low_temp = None
        self.high_temp = None
        self.wind = None
        self.wind_speed = None

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

city = City()
city.name = input('请输入城市：')
while city.name not in city_list:
    city.name = input('没有该城市，请重新输入:')
    if city == '0':
        break
city.url = city_list[city.name]
#print(city_url)

city_bs = BeautifulSoup(requests.get(city.url, headers = headers).content, 'html.parser')
city_alphabet = city_bs.find(name = 'ul', attrs={"class":'days clearfix'})
#print(city_alphabet.text)
text = city_alphabet.text.split()
city.weather = text[1].strip()
city.low_temp = text[2].strip()
city.high_temp = text[4].strip()
city.wind = text[5].strip()
city.wind_speed = text[6].strip()

print('城市：', city.name)
print('天气：', city.weather)
print(f'温度：{city.low_temp} ~ {city.high_temp}')
print(f'风速：{city.wind} {city.wind_speed}')