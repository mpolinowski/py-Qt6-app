from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

from bs4 import BeautifulSoup
import requests

def get_prize():
    url = f'https://www.instar.com/produkte/wlan-aussenkameras-poe-ip-kameras-wetterfeste-netzwerkkameras-outdoor-uberwachungskameras/in-9408-2k-serie-wlan-uberwachungskamera-ai-objekterkennung-apple-homekit-mqtt-sftp-nachtsicht/in-9408-2k-poe-weiss-ip-kamera.html'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    prize = soup.find("span", class_="price").get_text()
    prize_intl = prize.replace(',', '.')
    prize_float = float(prize_intl[:-2])
    
    return prize_float


def calc_value():
    number = float(number_input.text())
    prize = get_prize()
    calculated_value = str(number * prize)
    number_output.setText(calculated_value)

# App scaffolding

app = QApplication([])
window = QWidget()
window.setWindowTitle('Price Calculator - INSTAR IN-9408 2k+')
layout = QVBoxLayout()

# Encode string to base64

number_input = QLineEdit()
layout.addWidget(number_input)

btn = QPushButton('Get Price')
layout.addWidget(btn)
btn.clicked.connect(calc_value)

number_output = QLabel('')
layout.addWidget(number_output)

## Execute

window.setLayout(layout)
window.show()
app.exec()