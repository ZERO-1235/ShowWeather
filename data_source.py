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

class WeatherData:
    
    def __init__(self):
        self.prov = None
        self.city_list = None
        self.city = City()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/55.0.2883.87 Safari/537.36'}
    
    def get_provinces(self):
        url = 'https://tianqi.moji.com/weather/china'
        headers = self.headers

        bs = BeautifulSoup(requests.get(url, headers = headers).content, 'html.parser')
        alphabet = bs.find(name = 'div', attrs={"class":'city clearfix'})

        prov = dict()
        for item in alphabet.find_all('a'):
            prov_url = str(item['href'])
            zh_name = item.text
            prov[zh_name] = prov_url
        
        self.prov = prov
        return prov
    
    def get_cities(self, province):
        prov = self.prov
        province_url = 'https://tianqi.moji.com' + prov[province]
        headers = self.headers
        prov_bs = BeautifulSoup(requests.get(province_url, headers = headers).content, 'html.parser')
        prov_alphabet = prov_bs.find(name = 'div', attrs={"class":'city_hot'})
        city_list = dict()
        for item in prov_alphabet.find_all('a'):
            city_url = str(item['href'])
            zh_name = item.text
            city_list[zh_name] = city_url

        self.city_list = city_list
        return city_list
    
    def get_weather(self, city_name):
        city_list = self.city_list
        city = City()
        city.name = city_name
        city.url = city_list[city.name]
        headers = self.headers
        city_bs = BeautifulSoup(requests.get(city.url, headers = headers).content, 'html.parser')
        city_alphabet = city_bs.find(name = 'ul', attrs={"class":'days clearfix'})
        text = city_alphabet.text.split()
        city.weather = text[1].strip()
        city.low_temp = text[2].strip()
        city.high_temp = text[4].strip()
        city.wind = text[5].strip()
        city.wind_speed = text[6].strip()
        return city

weather_data = WeatherData()