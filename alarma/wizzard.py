import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QLabel, QWidget, QPushButton, QHBoxLayout, QLineEdit, QComboBox, QCheckBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from advancedWizard import AdvancedWizard
from user_wizard import UserWizard
class Wizard1Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Asistente de Configuración")
        self.setGeometry(0, 0, 1920, 1080)

        self.setStyleSheet("background-color: rgba(38,64,67,255);")

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

        vbox_center = QVBoxLayout()
        vbox_center.setAlignment(Qt.AlignTop)
        vbox_center.setSpacing(20)

        welcome_label = QLabel("Configuración de zona Wifi")
        welcome_label.setStyleSheet("color: white; font-size: 2em; font-weight: bold;")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setContentsMargins(0, 50, 0, 20)

        grid = QGridLayout()
        grid.setAlignment(Qt.AlignCenter)
        grid.setSpacing(15)

        grid.setRowStretch(0, 1)
        grid.setRowStretch(1, 1)
        grid.setRowStretch(2, 1)
        grid.setRowStretch(3, 1)
        grid.setRowStretch(4, 1)


        network_label = QLabel("Red")
        network_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(network_label, 0, 0)
        # add a combo box
        self.network_combo = QComboBox()
        self.network_combo.addItem("Red 1")
        self.network_combo.addItem("Red 2")
        self.network_combo.addItem("Red 3")
        self.network_combo.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        grid.addWidget(self.network_combo, 0, 1)

        security_label = QLabel("Seguridad")
        security_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(security_label, 1, 0)
        self.security_combo = QComboBox()
        self.security_combo.addItem("WPA/WPA2")
        self.security_combo.addItem("WEP")
        self.security_combo.addItem("Ninguna")
        self.security_combo.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        grid.addWidget(self.security_combo, 1, 1)
        password_label = QLabel("Contraseña")
        password_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(password_label, 2, 0)
        self.password_field = QLineEdit()
        grid.addWidget(self.password_field, 2, 1)
        self.password_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.password_field.setPlaceholderText("Ingresar una contraseña")
        self.password_field.setEchoMode(QLineEdit.Password)

        self.show_password = QCheckBox()
        self.show_password.setStyleSheet("color: white; font-size: 1.5em;padding-left: 100px;")
        self.show_password.stateChanged.connect(self.show_password_on_click)
        grid.addWidget(self.show_password, 3, 0)
        show_password_label = QLabel("Mostrar contraseña")
        show_password_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(show_password_label, 3, 1)
        band_label = QLabel("Seleccionar banda")
        band_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(band_label, 4, 0)
        self.band_combo = QComboBox()
        self.band_combo.addItem("2.4 GHz")
        self.band_combo.addItem("5 GHz")
        self.band_combo.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        grid.addWidget(self.band_combo, 4, 1)

        vbox_center.addStretch(1)
        vbox_center.addWidget(welcome_label)
        vbox_center.addLayout(grid)
        vbox_center.addStretch(1)

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

        vbox_center.addLayout(hbox_bottom)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)
        central_layout.addLayout(hbox_top)
        central_layout.addLayout(vbox_center)

    def next_button_on_click(self):
        self.wizard1_window = UserWizard()
        self.wizard1_window.show()
        self.hide()
    
    def advanced_button_on_click(self):
        self.wizard1_window = AdvancedWizard()
        self.wizard1_window.show()
        self.hide()

    def regresar(self):
         self.hide()

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