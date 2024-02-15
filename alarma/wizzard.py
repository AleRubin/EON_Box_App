import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QLabel, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from wizzard1 import LoginWindow

class Wizard1Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Asistente de Configuración")
        self.setGeometry(100, 100, 640, 480)

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
        grid.setSpacing(10)

        network_label = QLabel("Red")
        network_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(network_label, 0, 0)

        security_label = QLabel("Seguridad")
        security_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(security_label, 1, 0)

        password_label = QLabel("Contraseña")
        password_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(password_label, 2, 0)

        band_label = QLabel("Seleccionar banda")
        band_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(band_label, 4, 0)

        vbox_center.addStretch(1)
        vbox_center.addWidget(welcome_label)
        vbox_center.addLayout(grid)
        vbox_center.addStretch(1)

        hbox_bottom = QHBoxLayout()
        hbox_bottom.setAlignment(Qt.AlignCenter)
        hbox_bottom.setSpacing(10)

        advanced_button = QPushButton("Configuración avanzada")
        advanced_button.setStyleSheet("background-color: rgba(96,169,23,255); color: white; font-size: 1em;")
        hbox_bottom.addWidget(advanced_button)

        next_button = QPushButton("Siguiente")
        next_button.setStyleSheet("background-color: rgba(96,169,23,255); color: white; font-size: 1em;")
        next_button.clicked.connect(self.next_button_on_click)
        hbox_bottom.addWidget(next_button)

        cancel_button = QPushButton("Cancelar")
        cancel_button.setStyleSheet("background-color: rgba(96,169,23,255); color: white; font-size: 1em;")
        hbox_bottom.addWidget(cancel_button)

        vbox_center.addLayout(hbox_bottom)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)
        central_layout.addLayout(hbox_top)
        central_layout.addLayout(vbox_center)

    def next_button_on_click(self):
        self.wizard1_window = LoginWindow()
        self.wizard1_window.show()
        self.hide()

    def regresar(self):
         self.hide()

    

    

    

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Wizard1Window()
    window.show()
    sys.exit(app.exec_())