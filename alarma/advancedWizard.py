import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit, QComboBox, QRadioButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from user_wizard import UserWizard
# from wizzard import Wizard1Window
class AdvancedWizard(QMainWindow):
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

        welcome_label = QLabel("Configuración avanzada de zona Wifi")
        welcome_label.setStyleSheet("color: white; font-size: 2em; font-weight: bold;")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setContentsMargins(0, 50, 0, 20)

        grid = QGridLayout()
        grid.setAlignment(Qt.AlignCenter)
        grid.setSpacing(10)

        network_label = QLabel("IP")
        network_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(network_label, 0, 0)
        network_field = QLineEdit()
        grid.addWidget(network_field, 0, 1)
        network_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        network_field.setPlaceholderText("Ingrese una dirección IP")
        security_label = QLabel("Netmask")
        security_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(security_label, 1, 0)
        security_field = QLineEdit()
        grid.addWidget(security_field, 1, 1)
        security_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        security_field.setPlaceholderText("Ingrese una máscara de red")

        password_label = QLabel("DNS Server")
        password_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(password_label, 2, 0)
        password_field = QLineEdit()
        grid.addWidget(password_field, 2, 1)
        password_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        password_field.setPlaceholderText("Ingrese una dirección DNS")

        band_label = QLabel("IP Gateway")
        band_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(band_label, 4, 0)
        band_field = QLineEdit()
        grid.addWidget(band_field, 4, 1)
        band_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        band_field.setPlaceholderText("Ingrese una dirección de puerta de enlace")

        vbox_center.addStretch(1)
        vbox_center.addWidget(welcome_label)
        vbox_center.addLayout(grid)
        vbox_center.addStretch(1)

        hbox_bottom = QHBoxLayout()
        hbox_bottom.setAlignment(Qt.AlignCenter)

        hbox_bottom.setSpacing(10)

        back_button = QPushButton("Regresar")
        back_button.setStyleSheet("background-color: #3498db; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        back_button.clicked.connect(self.back_button_on_click)
        hbox_bottom.addWidget(back_button)


        next_button = QPushButton("Siguiente")
        next_button.setStyleSheet("background-color: #2ecc71; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        hbox_bottom.addWidget(next_button)

        cancel_button = QPushButton("Cancelar")
        cancel_button.setStyleSheet("background-color: #e74c3c; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        cancel_button.clicked.connect(self.cancel_button_on_click)
        hbox_bottom.addWidget(cancel_button)

        vbox_center.addLayout(hbox_bottom)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)
        central_layout.addLayout(hbox_top)
        central_layout.addLayout(vbox_center)

        next_button.clicked.connect(self.next_button_on_click)
        cancel_button.clicked.connect(self.cancel_button_on_click)

    def back_button_on_click(self):
        from wizzard import Wizard1Window
        self.wizard1 = Wizard1Window()
        self.wizard1.show()
        self.close()

    def next_button_on_click(self):
        self.user_wizard = UserWizard()
        self.user_wizard.show()
        self.close()

    def cancel_button_on_click(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdvancedWizard()
    window.show()
    sys.exit(app.exec_())
        