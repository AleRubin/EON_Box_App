import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QVBoxLayout, QLabel, QWidget, QPushButton, QHBoxLayout, QLineEdit, QComboBox, QCheckBox, QScrollArea, QDialog, QDialogButtonBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from advancedWizard import AdvancedWizard
from user_wizard import UserWizard
import wifi
from getmac import get_mac_address as gma
import requests
import json
import sqlite3
connection = sqlite3.connect("alarma.db")
cursor = connection.cursor()


class Wizard1Window(QWidget):
    def __init__(self, app_state):
        super().__init__()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS cuenta (id INTEGER, id_nube TEXT, mac TEXT, identificador TEXT, nombre TEXT, pin TEXT, fk_idCatEstatusDispositivo INT)")

        self.central_layout = QVBoxLayout()

        self.scroll_area = QScrollArea()
        self.central_layout.addWidget(self.scroll_area)

        self.scroll_content = QWidget()
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.setWidgetResizable(True)

        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)

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
        self.scroll_layout.addLayout(self.hbox_top)

        self.vbox_center = QVBoxLayout()
        self.vbox_center.setAlignment(Qt.AlignCenter)
        self.vbox_center.setSpacing(20)

        self.welcome_label = QLabel("Configuración de zona Wifi")
        self.welcome_label.setStyleSheet(
            "color: white; font-size: 40px; font-weight: bold;")
        self.welcome_label.setAlignment(Qt.AlignCenter)

        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignCenter)

        self.network_label = QLabel("Red")
        self.network_label.setMaximumWidth(200)
        self.network_label.setStyleSheet("color: white; font-size: 20px;")
        self.network_label.setMaximumSize(200, 50)
        self.grid.addWidget(self.network_label, 0, 0)

        self.network_combo = QComboBox()
        self.network_combo.addItems(["Red 1", "Red 2", "Red 3"])
        self.network_combo.setStyleSheet(
            "color: black; font-size: 1.5em; background-color: white;")
        self.network_combo.setMaximumWidth(300)
        self.network_combo.setMaximumHeight(70)
        self.grid.addWidget(self.network_combo, 0, 1)

        self.security_label = QLabel("Seguridad")
        self.security_label.setMaximumWidth(200)
        self.security_label.setStyleSheet("color: white; font-size: 20px;")
        self.security_label.setMaximumHeight(50)
        self.grid.addWidget(self.security_label, 1, 0)

        self.security_combo = QComboBox()
        self.security_combo.addItems(["WPA/WPA2", "WEP", "Ninguna"])
        self.security_combo.setStyleSheet(
            "color: black; font-size: 1.5em; background-color: white;")
        self.security_combo.setMaximumSize(300, 50)
        self.grid.addWidget(self.security_combo, 1, 1)

        self.password_label = QLabel("Contraseña")
        self.password_label.setMaximumWidth(200)
        self.password_label.setStyleSheet("color: white; font-size: 20px;")
        self.grid.addWidget(self.password_label, 2, 0)

        self.password_field = QLineEdit()
        self.password_field.setStyleSheet(
            "color: black; font-size: 1.5em; background-color: white;")
        self.password_field.setPlaceholderText("Ingresar una contraseña")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setMaximumSize(300, 50)
        self.grid.addWidget(self.password_field, 2, 1)

        self.show_password = QCheckBox()
        self.show_password.setStyleSheet("color: white; font-size: 1.5em;")
        self.show_password.stateChanged.connect(self.show_password_on_click)
        self.grid.addWidget(self.show_password, 3, 0)

        self.password_label = QLabel("Mostrar contraseña")
        self.password_label.setMaximumWidth(200)
        self.password_label.setStyleSheet("color: white; font-size: 20px;")
        self.grid.addWidget(self.password_label, 3, 1)

        self.band_label = QLabel("Seleccionar banda")
        self.band_label.setMaximumWidth(200)
        self.band_label.setStyleSheet("color: white; font-size: 20px;")
        self.grid.addWidget(self.band_label, 4, 0)

        self.band_combo = QComboBox()
        self.band_combo.addItems(["2.4 GHz", "5 GHz"])
        self.band_combo.setStyleSheet(
            "color: black; font-size: 1.5em; background-color: white;")
        self.band_combo.setMaximumWidth(300)
        self.band_combo.setMaximumHeight(50)
        self.grid.addWidget(self.band_combo, 4, 1)

        self.vbox_center.addWidget(self.welcome_label)
        self.vbox_center.addLayout(self.grid)

        self.scroll_layout.addLayout(self.vbox_center)

        self.hbox_bottom = QHBoxLayout()
        self.hbox_bottom.setAlignment(Qt.AlignCenter)
        self.hbox_bottom.setSpacing(10)

        self.advanced_button = QPushButton("Configuración avanzada")
        self.advanced_button.setStyleSheet(
            "background-color: #3498db; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        self.advanced_button.clicked.connect(
            lambda: self.advanced_button_on_click(app_state))
        self.hbox_bottom.addWidget(self.advanced_button)

        self.next_button = QPushButton("Siguiente")
        self.next_button.setStyleSheet(
            "background-color: #2ecc71; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        # pasar app_state como argumento
        self.next_button.clicked.connect(
            lambda: self.next_button_on_click(app_state))
        self.hbox_bottom.addWidget(self.next_button)

        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.setStyleSheet(
            "background-color: #e74c3c; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        self.cancel_button.clicked.connect(lambda: self.regresar(app_state))
        self.hbox_bottom.addWidget(self.cancel_button)

        self.scroll_layout.addLayout(self.hbox_bottom)

        self.vbox_center.addLayout(self.hbox_bottom)

        self.central_layout.addLayout(self.hbox_top)
        self.central_layout.addLayout(self.vbox_center)

        self.setLayout(self.central_layout)

        # self.populate_networks()

    def next_button_on_click(self, app_state):
        # get https://anam.eonproduccion.net:9001/alarmas/api/dispositivo/mac/b8:27:eb:6a:7b:4c
        try:
            response = requests.get(
                'https://cloudsecurity-api.eonproduccion.net/api/cajas/mac/2c:cf:67:4e:45:70')
            # response = requests.get('https://cloudsecurity-api.eonproduccion.net/api/cajas/mac/' + gma())
            response = json.loads(response.text)
            response = response['data']
            ''' si existe el id actualizar'''
            cursor.execute("SELECT * FROM cuenta WHERE id = 1")
            data = cursor.fetchone()
            if data:
                cursor.execute("UPDATE cuenta SET id_nube = ?, mac = ?, identificador = ?, nombre = ?, pin = ?, fk_idCatEstatusDispositivo = ? WHERE id = 1",
                               (response['id'], response['mac'], response['identificador'],
                                response['identificador'], response['pin'], response['id_estatus_dispositivo'],
                                ))
            else:
                cursor.execute("INSERT INTO cuenta (id, id_nube, mac, identificador, nombre, pin, fk_idCatEstatusDispositivo) VALUES (?,?,?,?,?,?,?)",
                               (1,
                                response['id'], response['mac'], response['identificador'],
                                response['identificador'], response['pin'], response['id_estatus_dispositivo'],
                                ))

            connection.commit()
            indice_actual = app_state.get_stack()
            app_state.set_stack(indice_actual + 2)
        except Exception as e:
            dialog = QDialog()
            QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            buttonBox = QDialogButtonBox(QBtn)
            buttonBox.accepted.connect(dialog.accept)
            buttonBox.rejected.connect(dialog.reject)

            layout = QVBoxLayout()
            layout.addWidget(QLabel("No se pudo conectar al servidor"))
            layout.addWidget(buttonBox)
            dialog.setLayout(layout)

            dialog.exec_()
            pass

    def advanced_button_on_click(self, app_state):
        indice_actual = app_state.get_stack()
        app_state.set_stack(indice_actual + 1)

    def regresar(self, app_state):
        indice_actual = app_state.get_stack()
        app_state.set_stack(indice_actual - 1)

    def populate_networks(self):
        networks = wifi.Cell.all('wlan0')

        # Agregar los nombres de las redes al QComboBox
        for network in networks:
          self.network_combo.addItem(network.ssid)

    def show_password_on_click(self):
        if self.show_password.isChecked():
            self.password_field.setEchoMode(QLineEdit.Normal)
        else:
            self.password_field.setEchoMode(QLineEdit.Password)
