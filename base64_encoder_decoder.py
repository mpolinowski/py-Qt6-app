from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

import base64

def to_base64():
    input_text = text_encode.text()
    encoded_bytes = base64.urlsafe_b64encode(input_text.encode("utf-8"))
    encoded_text = str(encoded_bytes, "utf-8")
    output_encode.setText("Encoded String: " + encoded_text)

def from_base64():
    input_text = text_decode.text()
    decoded_bytes = base64.urlsafe_b64decode(input_text.encode("utf-8"))
    decoded_text = str(decoded_bytes, "utf-8")
    output_decode.setText("Decoded String: " + decoded_text)

# App scaffolding

app = QApplication([])
window = QWidget()
window.setWindowTitle('base64 de/encoder')
layout = QVBoxLayout()

# Encode string to base64

text_encode = QLineEdit()
layout.addWidget(text_encode)

btn = QPushButton('base64 Encode')
layout.addWidget(btn)
btn.clicked.connect(to_base64)

output_encode = QLabel('')
layout.addWidget(output_encode)

# Decode string from base64

text_decode = QLineEdit()
layout.addWidget(text_decode)

btn = QPushButton('base64 Decode')
layout.addWidget(btn)
btn.clicked.connect(from_base64)

output_decode = QLabel('')
layout.addWidget(output_decode)

## Execute

window.setLayout(layout)
window.show()
app.exec()