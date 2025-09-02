import sys 
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit, QComboBox, QRadioButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from user_wizard import UserWizard

class AdvancedWizard(QWidget):
    def __init__(self, app_state):
        super().__init__()

        self.vbox_center = QVBoxLayout()
        self.vbox_center.setAlignment(Qt.AlignTop)
        self.vbox_center.setSpacing(20)

        self.welcome_label = QLabel("Configuración avanzada de zona Wifi")
        self.welcome_label.setStyleSheet("color: white; font-size: 40px; font-weight: bold;")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setContentsMargins(0, 50, 0, 20)

        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignCenter)
        self.grid.setSpacing(10)
        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 1)
        self.grid.setRowStretch(0, 1)
        self.grid.setRowStretch(1, 1)
        self.grid.setRowStretch(2, 1)
        self.grid.setRowStretch(3, 1)
        self.grid.setRowStretch(4, 1)

        self.network_label = QLabel("IP")
        self.network_label.setStyleSheet("color: white; font-size: 20px;")
        self.network_label.setMaximumSize(200, 50)
        self.grid.addWidget(self.network_label, 0, 0)
        self.network_field = QLineEdit()
        self.grid.addWidget(self.network_field, 0, 1)
        self.network_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.network_field.setMaximumHeight(70)
        self.network_field.setMaximumWidth(300)
        self.network_field.setPlaceholderText("Ingrese una dirección IP")
        self.security_label = QLabel("Netmask")
        self.security_label.setStyleSheet("color: white; font-size: 20px;")
        self.security_label.setMaximumSize(200, 50)
        self.grid.addWidget(self.security_label, 1, 0)
        self.security_field = QLineEdit()
        self.grid.addWidget(self.security_field, 1, 1)
        self.security_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.security_field.setMaximumSize(300, 50)
        self.security_field.setPlaceholderText("Ingrese una máscara de red")

        self.password_label = QLabel("DNS Server")
        self.password_label.setStyleSheet("color: white; font-size: 20px;")
        self.password_label.setMaximumSize(200, 50)
        self.grid.addWidget(self.password_label, 2, 0)
        self.password_field = QLineEdit()
        self.grid.addWidget(self.password_field, 2, 1)
        self.password_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.password_field.setPlaceholderText("Ingrese una dirección DNS")
        self.password_field.setMaximumSize(300, 50)

        self.band_label = QLabel("IP Gateway")
        self.band_label.setStyleSheet("color: white; font-size: 20px;")
        self.band_label.setMaximumSize(200, 50)
        self.grid.addWidget(self.band_label, 4, 0)
        self.band_field = QLineEdit()
        self.grid.addWidget(self.band_field, 4, 1)
        self.band_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.band_field.setMaximumSize(300, 50)
        self.band_field.setPlaceholderText("Ingrese una dirección de puerta de enlace")
        self.grid.setRowMinimumHeight(0, 40)
        self.grid.setRowMinimumHeight(1, 40)
        self.grid.setRowMinimumHeight(2, 40)
        self.grid.setRowMinimumHeight(3, 40)
        self.grid.setRowMinimumHeight(4, 40)

        # self.vbox_center.addStretch(1)
        self.vbox_center.addWidget(self.welcome_label)
        self.vbox_center.addStretch(1)
        self.vbox_center.addLayout(self.grid)
        self.vbox_center.addStretch(1)

        self.hbox_bottom = QHBoxLayout()
        self.hbox_bottom.setAlignment(Qt.AlignCenter)

        self.hbox_bottom.setSpacing(10)

        self.back_button = QPushButton("Regresar")
        self.back_button.setStyleSheet("background-color: #3498db; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        self.back_button.clicked.connect(lambda: self.back_button_on_click(app_state))
        self.hbox_bottom.addWidget(self.back_button)


        self.next_button = QPushButton("Siguiente")
        self.next_button.setStyleSheet("background-color: #2ecc71; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        self.next_button.clicked.connect(lambda: self.next_button_on_click(app_state))
        self.hbox_bottom.addWidget(self.next_button)

        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.setStyleSheet("background-color: #e74c3c; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        self.cancel_button.clicked.connect(lambda: self.cancel_button_on_click(app_state))
        self.hbox_bottom.addWidget(self.cancel_button)

        self.vbox_center.addLayout(self.hbox_bottom)

        self.central_layout = QVBoxLayout()
        self.central_layout.addLayout(self.vbox_center)

        self.setLayout(self.central_layout)
        

    def back_button_on_click(self, app_state):
        indice_actual = app_state.get_stack()
        app_state.set_stack(indice_actual - 1)

    def next_button_on_click(self, app_state):
        indice_actual = app_state.get_stack()
        app_state.set_stack(indice_actual + 1)

    def cancel_button_on_click(self, app_state):
        indice_actual = app_state.get_stack()
        app_state.set_stack(indice_actual - 1)
