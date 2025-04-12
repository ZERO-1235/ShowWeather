# 天气查询软件报告

### 李佳昊 PB22061305

```
Github：https://github.com/ZERO-1235/ShowWeather.git
视频：https://rec.ustc.edu.cn/share/bdbd7990-16ff-11f0-8ab9-b15d4b33ab23
```
## 一、软件功能

该软件可以实时查询全国各区域的天气情况，包括天气、温度、风力等。


## 二、软件设计的类及其方法

1 、class City
此类定义了一个区域（本来是城市）的信息，包括名字、url、天气、温度、风力等。
2 、class WeatherData
此类定义了天气数据及其获取方法。初始化定义了省份列表、区域列表和待查区域。get_provinces()方法用于从网站获取省份信息并形成列表，get_cities()方法用于从网站获取给定省份的区域信息并形成列表，get_weather()方法用于根据给定的区域从网站获取当天的天气情况。
3 、class WeatherApp
此类主要用于GUI展示。初始化定义了标题、两个下拉框（一个展示省份，一个展示区域）和一个信息显示框。update_province_combo()方法用于从data_source.py中获取省份信息并更新，on_province_changed()方法用于检测省份框内容的变化，并调用update_city_combo()获取区域信息，update_city_combo()方法用于从data_source.py中获取区域信息并更新，query_weather()方法用于从data_source.py中获取当前区域的天气信息并更新，display_weather()方法用于将天气信息展示到信息显示框。

## 三、困难及收获

1 、在此之前不会编写GUI或网站。在deepseek的帮助下，初步尝试了利用PyQt5 库对GUI进行编写，效果基本符合预期。
2 、学习了如何实现py文件之间的相互调用。
3 、对类及其方法的编写更加熟练。
4 、学会了使用github远程仓库和vscode本地代码之间的拉取、推送等操作。
5 、初次尝试录屏。

## 四、软件使用方法

### 1 、安装依赖库
```
pip install requests
pip install beautifulsoup4
pip install PyQt5
```
2 、直接运行GUI.py即可打开软件图形界面，首先点击第一个下拉框选择省份，然后点击第二个下拉框选择区域，最后点击“查询天气”即可，详细操作参见视频。