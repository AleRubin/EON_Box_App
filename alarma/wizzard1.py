from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt
import sys
from home import MainUI
from PyQt5 import QtWidgets
import sqlite3
connection = sqlite3.connect("alarma.db")
cursor = connection.cursor()

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Teclado Numérico")
        self.setGeometry(0, 0,1024,600)
        self.setStyleSheet("background-color: rgba(38,64,67,255);")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        hbox_top = QHBoxLayout()

        hbox_top.setAlignment(Qt.AlignLeft | Qt.AlignTop)  

        logo_image_top_left = QLabel()
        logo_image_top_left.setPixmap(QPixmap("images/logo.png").scaledToWidth(20).scaledToHeight(20))               
        logo_image_top_left.setScaledContents(True)

        logo_image_top_right = QLabel()
        logo_image_top_right.setPixmap(QPixmap("images/titulo.png").scaledToWidth(198))  
        logo_image_top_right.setScaledContents(True)

        hbox_top.addWidget(logo_image_top_left)
        hbox_top.addWidget(logo_image_top_right)

        welcome_label = QLabel("Ingrese su contraseña.")
        welcome_label.setStyleSheet("color: white; font-size: 40px; font-weight: bold;")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setContentsMargins(0, 50, 0, 20)

        central_layout = QVBoxLayout()
        central_layout.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        # layout.setContentsMargins(50, 50, 50, 50)
        password_label = QLabel("Ingrese su contraseña de acceso")
        password_label.setStyleSheet("font-size: 18px; color: #ffffff;")
        layout.addWidget(password_label)

        password_field = QLineEdit()
        layout.addWidget(password_field)
        password_field.setPlaceholderText("Contraseña")
        password_field.setStyleSheet("color: #000; max-width: 300; height: 30px; font-size: 18px; background-color: #ffffff;")
        password_field.setReadOnly(True)

        numpad_grid = QGridLayout()
        numpad_grid.setHorizontalSpacing(10)
        numpad_grid.setVerticalSpacing(10)

        buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "", "0", ""]
        positions = [(i, j) for i in range(4) for j in range(3)]

        for position, button_text in zip(positions, buttons):
            if button_text:
                button = QPushButton(button_text)
                button.setStyleSheet("min-width: 60px; min-height: 60px; background-color: #000; color: #ffffff; font-size: 20px;")
                button.clicked.connect(lambda _, text=button_text: self.on_numpad_button_click(text,password_field))
                numpad_grid.addWidget(button, *position)

        layout.addLayout(numpad_grid)

        login_button = QPushButton("Ingresar")
        login_button.setStyleSheet("min-width: 120px; min-height: 60px; background-color: #388e3c; color: #ffffff;")
        login_button.clicked.connect(lambda _, text=password_field.text(): self.login(text, password_field))
        layout.addWidget(login_button)
        central_layout.addLayout(hbox_top)
        central_layout.addWidget(welcome_label)
        central_layout.addStretch(1)
        central_layout.addLayout(layout)
        central_layout.addStretch(1)
        central_widget.setLayout(central_layout)

        

    def on_numpad_button_click(self, text,password_field):
        password_field.setText(password_field.text() + text)

    def login(self,text, password_field):
        cursor.execute('SELECT * FROM cuenta')
        data = cursor.fetchone()
        password = data[5]

        if password_field.text() == password:
            self.home = MainUI()
            self.home.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Contraseña incorrecta")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
