import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QComboBox, QLabel, QFrame, QHBoxLayout, QPushButton)
from PyQt5.QtCore import Qt, QTimer

from data_source import weather_data

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("城市天气预报")
        self.setGeometry(100, 100, 500, 400)
        
        self.data = weather_data
        self.init_ui()
        self.update_province_combo()
    
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 标题
        self.title_label = QLabel("城市天气预报查询")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        # 省份选择
        self.province_combo = QComboBox()
        self.province_combo.setPlaceholderText("请选择省份")
        self.province_combo.currentTextChanged.connect(self.on_province_changed)
        
        # 城市选择
        self.city_combo = QComboBox()
        self.city_combo.setPlaceholderText("请先选择省份")
        self.city_combo.setEnabled(False)
        
        # 查询按钮
        self.query_btn = QPushButton("查询天气")
        self.query_btn.setEnabled(False)
        self.query_btn.clicked.connect(self.query_weather)
        
        # 信息显示框
        self.info_box = QFrame()
        self.info_box.setFrameShape(QFrame.Box)
        self.info_box.setLineWidth(2)
        self.info_box.setStyleSheet("background-color: #f9f9f9;")
        
        self.info_label = QLabel("请先选择省份和城市")
        self.info_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.info_label.setWordWrap(True)
        self.info_label.setStyleSheet("padding: 10px; font-size: 14px;")
        
        info_layout = QVBoxLayout()
        info_layout.addWidget(self.info_label)
        self.info_box.setLayout(info_layout)
        
        # 布局
        main_layout.addWidget(self.title_label)
        
        combo_layout = QHBoxLayout()
        combo_layout.addWidget(QLabel("省份:"))
        combo_layout.addWidget(self.province_combo)
        combo_layout.addWidget(QLabel("城市:"))
        combo_layout.addWidget(self.city_combo)
        
        main_layout.addLayout(combo_layout)
        main_layout.addWidget(self.query_btn)
        main_layout.addWidget(self.info_box)
    
    def update_province_combo(self):
        self.province_combo.clear()
        provinces = self.data.get_provinces()
        if provinces:
            self.province_combo.addItems(provinces)
            self.province_combo.setCurrentIndex(-1)
    
    def on_province_changed(self, province):
        if not province:
            self.city_combo.clear()
            self.city_combo.setEnabled(False)
            self.city_combo.setPlaceholderText("请先选择省份")
            self.query_btn.setEnabled(False)
            return
        
        self.city_combo.clear()
        self.city_combo.setEnabled(False)
        self.city_combo.setPlaceholderText("加载中...")
        self.query_btn.setEnabled(False)
        
        QTimer.singleShot(500, lambda: self.update_city_combo(province))
    
    def update_city_combo(self, province):
        cities = self.data.get_cities(province)
        self.city_combo.clear()
        
        if cities:
            self.city_combo.addItems(cities)
            self.city_combo.setEnabled(True)
            self.city_combo.setPlaceholderText("请选择城市")
            self.query_btn.setEnabled(True)
        else:
            self.city_combo.setPlaceholderText("无城市数据")
            self.city_combo.setEnabled(False)
            self.query_btn.setEnabled(False)
    
    def query_weather(self):
        city = self.city_combo.currentText()
        if not city:
            self.info_label.setText("请选择城市")
            return
        
        self.info_label.setText("正在获取天气数据...")
        self.query_btn.setEnabled(False)
        
        QTimer.singleShot(800, lambda: self.display_weather(city))
    
    def display_weather(self, city):
        weather_info = self.data.get_weather(city)
        
        info_text = (
            f"🏙️ {city}天气预报\n\n"
            f"天气: {weather_info.weather}\n"
            f"温度: {weather_info.low_temp} ~ {weather_info.high_temp}\n"
            f"风力: {weather_info.wind} {weather_info.wind_speed}\n"
        )
        
        self.info_label.setText(info_text)
        self.query_btn.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())