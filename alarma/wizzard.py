import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QLabel, QWidget, QPushButton, QHBoxLayout, QLineEdit, QComboBox, QCheckBox, QScrollArea
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from advancedWizard import AdvancedWizard
from user_wizard import UserWizard
import wifi 
import requests
import json 
import sqlite3
connection = sqlite3.connect("alarma.db")
cursor = connection.cursor()

class Wizard1Window(QMainWindow):
    def __init__(self):
        super().__init__()

        cursor.execute("CREATE TABLE IF NOT EXISTS cuenta (id INTEGER, id_nube TEXT, mac TEXT, identificador TEXT, nombre TEXT, pin TEXT, fk_idCatEstatusDispositivo INT, fk_idCatProveedorServicio INT, fechaRegistro INT, catEstatusDispositivo TEXT, catProveedorServicio TEXT)")

        self.setWindowTitle("Asistente de Configuración")
        self.setGeometry(0, 0,1024,600)

        self.setStyleSheet("background-color: rgba(38,64,67,255);")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)

        scroll_area = QScrollArea()
        central_layout.addWidget(scroll_area)

        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)
        scroll_area.setWidgetResizable(True)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setAlignment(Qt.AlignCenter)

        hbox_top = QHBoxLayout()
        hbox_top.setAlignment(Qt.AlignLeft | Qt.AlignTop)  
        hbox_top.setSpacing(10)
        
        
        logo_image_top_left = QLabel()
        logo_image_top_left.setPixmap(QPixmap("images/logo.png").scaledToWidth(40).scaledToHeight(40))         
        logo_image_top_left.setScaledContents(True)
        
        logo_image_top_right = QLabel()
        logo_image_top_right.setPixmap(QPixmap("images/titulo.png").scaledToWidth(198))  
        logo_image_top_right.setScaledContents(True)

        hbox_top.addWidget(logo_image_top_left)
        hbox_top.addWidget(logo_image_top_right)
        hbox_top.addStretch(1)

        scroll_layout.addLayout(hbox_top)

        vbox_center = QVBoxLayout()
        vbox_center.setAlignment(Qt.AlignCenter)
        vbox_center.setSpacing(20)

        welcome_label = QLabel("Configuración de zona Wifi")
        welcome_label.setStyleSheet("color: white; font-size: 40px; font-weight: bold;")
        welcome_label.setAlignment(Qt.AlignCenter)

        grid = QGridLayout()
        grid.setAlignment(Qt.AlignCenter)
        
        network_label = QLabel("Red")
        network_label.setMaximumWidth(200)
        network_label.setStyleSheet("color: white; font-size: 20px;")
        network_label.setMaximumSize(200, 50)
        grid.addWidget(network_label, 0, 0)

        self.network_combo = QComboBox()
        self.network_combo.addItems(["Red 1", "Red 2", "Red 3"])
        self.network_combo.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.network_combo.setMaximumWidth(300)
        self.network_combo.setMaximumHeight(70)
        grid.addWidget(self.network_combo, 0, 1)

        security_label = QLabel("Seguridad")
        security_label.setMaximumWidth(200)
        security_label.setStyleSheet("color: white; font-size: 20px;")
        security_label.setMaximumHeight(50)
        grid.addWidget(security_label, 1, 0)

        self.security_combo = QComboBox()
        self.security_combo.addItems(["WPA/WPA2", "WEP", "Ninguna"])
        self.security_combo.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.security_combo.setMaximumSize(300, 50)
        grid.addWidget(self.security_combo, 1, 1)

        password_label = QLabel("Contraseña")
        password_label.setMaximumWidth(200)
        password_label.setStyleSheet("color: white; font-size: 20px;")
        grid.addWidget(password_label, 2, 0)

        self.password_field = QLineEdit()
        self.password_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.password_field.setPlaceholderText("Ingresar una contraseña")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setMaximumSize(300, 50)
        grid.addWidget(self.password_field, 2, 1)

        self.show_password = QCheckBox()
        self.show_password.setStyleSheet("color: white; font-size: 1.5em;")
        self.show_password.stateChanged.connect(self.show_password_on_click)
        grid.addWidget(self.show_password, 3, 0)

        show_password_label = QLabel("Mostrar contraseña")
        show_password_label.setMaximumWidth(200)
        show_password_label.setStyleSheet("color: white; font-size: 20px;")
        grid.addWidget(show_password_label, 3, 1)

        band_label = QLabel("Seleccionar banda")
        band_label.setMaximumWidth(200)
        band_label.setStyleSheet("color: white; font-size: 20px;")
        grid.addWidget(band_label, 4, 0)

        self.band_combo = QComboBox()
        self.band_combo.addItems(["2.4 GHz", "5 GHz"])
        self.band_combo.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.band_combo.setMaximumWidth(300)
        self.band_combo.setMaximumHeight(50)
        grid.addWidget(self.band_combo, 4, 1)

        vbox_center.addWidget(welcome_label)
        vbox_center.addLayout(grid)

        scroll_layout.addLayout(vbox_center)

        hbox_bottom = QHBoxLayout()
        hbox_bottom.setAlignment(Qt.AlignCenter)
        hbox_bottom.setSpacing(10)

        advanced_button = QPushButton("Configuración avanzada")
        advanced_button.setStyleSheet("background-color: #3498db; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        advanced_button.clicked.connect(self.advanced_button_on_click)
        hbox_bottom.addWidget(advanced_button)

        next_button = QPushButton("Siguiente")
        next_button.setStyleSheet("background-color: #2ecc71; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        next_button.clicked.connect(self.next_button_on_click)
        hbox_bottom.addWidget(next_button)

        cancel_button = QPushButton("Cancelar")
        cancel_button.setStyleSheet("background-color: #e74c3c; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        hbox_bottom.addWidget(cancel_button)

        scroll_layout.addLayout(hbox_bottom)

        vbox_center.addLayout(hbox_bottom)

        central_layout.addLayout(hbox_top)
        central_layout.addLayout(vbox_center)

        self.populate_networks()

        self.showFullScreen()

    def next_button_on_click(self):
        # get https://anam.eonproduccion.net:9001/alarmas/api/dispositivo/mac/b8:27:eb:6a:7b:4c

        response = requests.get('https://anam.eonproduccion.net:9001/alarmas/api/dispositivo/mac/b8:27:eb:6a:7b:4c')
        response = json.loads(response.text)
        response = response['data'][0]

        response['catEstatusDispositivo'] = json.dumps(response['catEstatusDispositivo'])
        response['catProveedorServicio'] = json.dumps(response['catProveedorServicio'])
        cursor.execute("INSERT INTO cuenta (id, id_nube, mac, identificador, nombre, pin, fk_idCatEstatusDispositivo, fk_idCatProveedorServicio, fechaRegistro, catEstatusDispositivo, catProveedorServicio) VALUES (?,?,?,?,?,?,?,?,?,?,?)", 
                       (1, response['id'], response['mac'], response['identificador'], response['nombre'], response['pin'], response['fk_idCatEstatusDispositivo'], response['fk_idCatProveedorServicio'], response['fechaRegistro'], 
                        response['catEstatusDispositivo'], 
                        response['catProveedorServicio']))
        
        connection.commit()
        self.wizard1_window = UserWizard()
        self.wizard1_window.show()
        self.hide()
    
    def advanced_button_on_click(self):
        self.wizard1_window = AdvancedWizard()
        self.wizard1_window.show()
        self.hide()

    def regresar(self):
         self.hide()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Wizard1Window()
    window.show()
    sys.exit(app.exec_())