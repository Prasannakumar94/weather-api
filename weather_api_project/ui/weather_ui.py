from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from services.weather_service import fetch_weather
from utils.weather_icons import get_weather_emoji
import requests


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()

        self.city_label = QLabel('Enter city name:', self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton('Get Weather', self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')
        self.resize(500, 650)   # ⭐ makes window bigger like original

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        # Alignment
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Object names (IMPORTANT for styling)
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # ⭐ ORIGINAL BIG UI STYLE RESTORED
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;
            }

            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }

            QLineEdit#city_input {
                font-size: 40px;
            }

            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }

            QLabel#temperature_label {
                font-size: 75px;
            }

            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI Emoji;
            }

            QLabel#description_label {
                font-size: 50px;
                font-style: italic;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):

        city = self.city_input.text()

        try:
            data = fetch_weather(city)

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            self.display_error(f"HTTP error:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck Internet")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size:30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):

        self.temperature_label.setStyleSheet("font-size:75px;")

        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)
