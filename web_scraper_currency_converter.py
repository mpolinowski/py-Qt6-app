from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt

from bs4 import BeautifulSoup
import requests

def get_conversion(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate_float = float(rate[:-4])

    return rate_float

def calc_value():
    number = float(number_input.text())
    in_currency = select_inCurrency.currentText()
    out_currency = select_outCurrency.currentText()
    rate = get_conversion(in_currency, out_currency)
    calculated_value = str(number * rate)
    message = f'{number} {in_currency} is {calculated_value} {out_currency}'
    number_output.setText(message)

# App scaffolding

app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

layoutMain = QVBoxLayout()
layoutContainer = QHBoxLayout()
layoutMain.addLayout(layoutContainer)

layoutLeftBox = QVBoxLayout()
layoutContainer.addLayout(layoutLeftBox)
layoutRightBox = QVBoxLayout()
layoutContainer.addLayout(layoutRightBox)


# Select Currencies

currencies = ['USD','EUR','GBP','CNY']

select_inCurrency = QComboBox()
select_inCurrency.addItems(currencies)
layoutLeftBox.addWidget(select_inCurrency)

select_outCurrency = QComboBox()
select_outCurrency.addItems(currencies)
layoutLeftBox.addWidget(select_outCurrency)

# Convert to Target Currency

number_input = QLineEdit()
layoutRightBox.addWidget(number_input)

btn = QPushButton('Convert')
layoutMain.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(calc_value)

number_output = QLabel('')
layoutRightBox.addWidget(number_output)

## Execute

window.setLayout(layoutMain)
window.show()
app.exec()