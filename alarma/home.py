from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QSize
from armado import Armado
from alertas import Alertas
from monitor import Monitor
from systemConfig import SystemConfig
import requests
import json

import sqlite3
connection = sqlite3.connect("alarma.db")
cursor = connection.cursor()

class MainUI(QWidget):
    def __init__(self, app_state):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.hbox_top = QHBoxLayout()

        self.hbox_top.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        # self.hbox_top.setSpacing(1)

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
        # self.hbox_top.addStretch(1)
        self.main_layout.addLayout(self.hbox_top)
        self.main_layout.addStretch(1)
        self.center_layout = QHBoxLayout()
        self.center_layout.setAlignment(Qt.AlignCenter)
        self.main_layout.addLayout(self.center_layout)
        self.left_layout = QVBoxLayout()
        self.left_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        self.center_layout.addLayout(self.left_layout)

        self.button_home = QPushButton()
        self.button_home.setIcon(QIcon("images/info.png"))
        self.button_home.setIconSize(QSize(50, 50))
        self.button_home.setStyleSheet("background-color: rgba(38,64,67,255);")
        self.button_home.clicked.connect(self.info)
        self.left_layout.addWidget(self.button_home)
        self.center_layout.addStretch(1)
        self.left_vbox = QVBoxLayout()
        self.left_vbox.setSpacing(10)
        self.left_vbox.setContentsMargins(10, 10, 10, 10)

        self.grid_label = QLabel("Fecha")
        self.grid_label.setStyleSheet(
            "background-color: #ffffff; border-radius: 10px;")
        self.grid_label.setAlignment(Qt.AlignCenter)
        self.grid_label.setFont(QFont("Arial", 18))
        self.grid_label.setFixedWidth(100)
        self.left_vbox.addWidget(self.grid_label)

        self.center_layout.addLayout(self.left_vbox)

        self.right_vbox = QVBoxLayout()
        self.right_vbox.setSpacing(10)
        self.right_vbox.setContentsMargins(10, 10, 10, 10)

        labels = [
            {"text": "Estado del sistema", "background": "#e3c800",
                "weight": True, "top": 15},
            {"text": "Nombre del sensor armado",
                "background": "#ffffff", "top": 30},
            {"text": "Sensor 3 armado", "background": "#ffffff"},
            {"text": "Notificaciones", "background": "#ffffff",
                "underline": True, "underline_color": "red", "size": 18},
            {"text": "Alertas del sistema", "background": "#ffffff",
                "border": "2px solid red", "text_color": "red", "size": 20}
        ]

        for item in labels:
            self.label = QLabel(item["text"])
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setStyleSheet(
                f"background-color: {item['background']}; border-radius: 10px;")
            if "weight" in item:
                self.label.setFont(QFont("Arial", 18, QFont.Bold))
            if "top" in item:
                margin = f"margin-top: {item['top']}px;"
                self.label.setStyleSheet(self.label.styleSheet() + margin)
            if "underline" in item:
                self.label.setStyleSheet(self.label.styleSheet(
                ) + f"color: {item['underline_color']}; text-decoration: underline;")
                self.label.setFont(QFont("Arial", item["size"]))
            if "border" in item:
                self.label.setStyleSheet(self.label.styleSheet(
                ) + f"border: {item['border']}; color: {item['text_color']};")
                self.label.setFont(QFont("Arial", item["size"]))
            self.right_vbox.addWidget(self.label)
        self.center_layout.addLayout(self.right_vbox)
        self.bottom_layout = QVBoxLayout()
        self.center_layout.addLayout(self.bottom_layout)
        self.center_layout.addStretch(1)

        self.bottom_grid1 = QHBoxLayout()
        self.bottom_layout.addLayout(self.bottom_grid1)
        buttons_ad = [
            {"image_path": "images/armado.png", "action": lambda: self.gotoArmadoDesarmado(app_state)},
            {"image_path": "images/alertas.png", "action": lambda: self.gotoAlertas(app_state)}
        ]

        for item in buttons_ad:
            button = QPushButton()
            image = QPixmap(item["image_path"])
            scaled_pixmap = image.scaled(
                QSize(int(image.width() * .8), int(image.height() * .8)))
            button.setIcon(QIcon(scaled_pixmap))
            button.setIconSize(QPixmap(item["image_path"]).size() * .8)
            button.setStyleSheet("background-color: rgba(38,64,67,255);")
            button.clicked.connect(item["action"])
            self.bottom_grid1.addWidget(button)

        # Second QHBoxLayout for Monitor, SOS, and Configuración buttons
        self.bottom_grid2 = QHBoxLayout()
        self.bottom_layout.addLayout(self.bottom_grid2)
        self.main_layout.addStretch(1)
        buttons_msc = [
            {"image_path": "images/monitor.png", "action": lambda: self.gotoMonitor(app_state)},
            {"image_path": "images/sos.png", "action": lambda: self.gotoSOS(app_state)},
            {"image_path": "images/configuracion.png",
                "action": lambda: self.gotoConfiguracion(app_state)}
        ]

        for item in buttons_msc:
            button = QPushButton()
            image = QPixmap(item["image_path"])
            scaled_pixmap = image.scaled(
                QSize(int(image.width() * .8), int(image.height() * .8)))
            button.setIcon(QIcon(scaled_pixmap))
            button.setIconSize(QPixmap(item["image_path"]).size() * .8)
            button.setStyleSheet("background-color: rgba(38,64,67,255);")
            button.clicked.connect(item["action"])
            self.bottom_grid2.addWidget(button)

        self.setLayout(self.main_layout)

        self._validarIdYMandarPost()

    def _validarIdYMandarPost(self):
        # intervalo de 30 segundos
        # mandar post a la API
        id = self._getBaseDatos()
        if id:
            response = requests.post(
                'https://cloudsecurity-api.eonproduccion.net/api/cajas/ultimo_ping/' + str(id))
            response = json.loads(response.text)
            print(response)


    def _getBaseDatos(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS cuenta (id INTEGER, id_nube TEXT, mac TEXT, identificador TEXT, nombre TEXT, pin TEXT, fk_idCatEstatusDispositivo INT)")
        cursor.execute('SELECT * FROM cuenta')
        informacion = cursor.fetchone()
        id = 0
        if informacion:
            id = informacion[1]

        print(id)
        return id
    def gotoArmadoDesarmado(self, app_state):
        indice_actual = app_state.get_stack()
        app_state.set_stack(indice_actual + 1)


    def gotoAlertas(self, app_state):
        indice_actual = app_state.get_stack()
        app_state.set_stack(indice_actual + 2)

    def gotoMonitor(self, app_state):
        indice_actual = app_state.get_stack()
        app_state.set_stack(indice_actual + 3)

    def gotoSOS(self, app_state):
        indice_actual = app_state.get_stack()
        app_state.set_stack(indice_actual + 4)

    def gotoConfiguracion(self, app_state):
        indice_actual = app_state.get_stack()
        app_state.set_stack(indice_actual + 5)

    def info(self, app_state):
        app_state.set_stack(8)
