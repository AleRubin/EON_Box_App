from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys
from home import MainUI
from PyQt5 import QtWidgets
import sqlite3
connection = sqlite3.connect("alarma.db")
cursor = connection.cursor()


class LoginWindow(QWidget):
    def __init__(self, app_state):
        super().__init__()

        self.central_widget = QWidget()
        self.hbox_top = QHBoxLayout()

        self.hbox_top.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.logo_image_top_left = QLabel()
        self.logo_image_top_left.setPixmap(
            QPixmap("images/logo.png").scaledToWidth(40).scaledToHeight(40))
        self.logo_image_top_left.setScaledContents(True)

        self.logo_image_top_right = QLabel()
        self.logo_image_top_right.setPixmap(
            QPixmap("images/titulo.png").scaledToWidth(198))
        self.logo_image_top_right.setScaledContents(True)

        self.hbox_top.addWidget(self.logo_image_top_left)
        self.hbox_top.addWidget(self.logo_image_top_right)

        self.welcome_label = QLabel("Ingrese su contraseña.")
        self.welcome_label.setStyleSheet(
            "color: white; font-size: 30px; font-weight: bold;")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setContentsMargins(0, 0, 0, 20)

        self.central_layout = QVBoxLayout()
        self.central_layout.setAlignment(Qt.AlignTop)
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        # self.layout.setContentsMargins(50, 50, 50, 50)
       # password_label = QLabel("Ingrese su contraseña de acceso")
        # password_label.setStyleSheet("font-size: 18px; color: #ffffff;")
        # self.layout.addWidget(password_label)

        self.password_field = QLineEdit()
        self.layout.addWidget(self.password_field)
        self.password_field.setPlaceholderText("Contraseña")
        self.password_field.setStyleSheet(
            "color: #000; max-width: 300; height: 30px; font-size: 18px; background-color: #ffffff;")
        self.password_field.setReadOnly(True)

        self.numpad_grid = QGridLayout()
        self.numpad_grid.setHorizontalSpacing(10)
        self.numpad_grid.setVerticalSpacing(10)

        self.buttons = ["1", "2", "3", "4", "5",
                        "6", "7", "8", "9", "", "0", "C"]
        self.positions = [(i, j) for i in range(4) for j in range(3)]

        for position, button_text in zip(self.positions, self.buttons):
            if button_text:
                button = QPushButton(button_text)
                button.setStyleSheet(
                    "min-width: 50px; min-height: 50px; background-color: #000; color: #ffffff; font-size: 20px;")
                button.clicked.connect(lambda _, text=button_text: self.on_numpad_button_click(
                    text, self.password_field))
                self.numpad_grid.addWidget(button, *position)

        self.layout.addLayout(self.numpad_grid)

        self.login_button = QPushButton("Ingresar")
        self.login_button.setStyleSheet(
            "min-width: 120px; min-height: 50px; background-color: #388e3c; color: #ffffff;")
        self.login_button.clicked.connect(
            lambda _, text=self.password_field.text(): self.login(text, self.password_field, app_state))
        self.layout.addWidget(self.login_button)
        self.central_layout.addLayout(self.hbox_top)
        self.central_layout.addWidget(self.welcome_label)
        self.central_layout.addLayout(self.layout)
        self.setLayout(self.central_layout)

    def on_numpad_button_click(self, text, password_field):
        if (text == "C"):
            self.password_field.setText("")
        else:
            self.password_field.setText(password_field.text() + text)

    def login(self, text, password_field, app_state):
        try:
            cursor.execute('SELECT * FROM cuenta')
            data = cursor.fetchone()
            password = data[5]

            if len(password) == 0:
                indice_actual = app_state.get_stack()
                app_state.set_stack(indice_actual + 1)

            if password_field.text() == password:
                indice_actual = app_state.get_stack()
                app_state.set_stack(indice_actual + 1)
            else:
                QtWidgets.QMessageBox.warning(
                    self, "Error", "Contraseña incorrecta")
        except Exception as e:
            QtWidgets.QMessageBox.warning(
                self, "Error", "No hay una contraseña establecida")
