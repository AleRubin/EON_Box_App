import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from wizzard1 import LoginWindow

class MovilUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Configuración de usuario")
        self.setGeometry(0, 0, 1024, 600)
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
        vbox_center.setAlignment(Qt.AlignCenter)
        vbox_center.setSpacing(20)

        welcome_label = QLabel("Configuración de usuario")
        welcome_label.setStyleSheet("color: white; font-size: 40px; font-weight: bold;")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setContentsMargins(0, 50, 0, 20)

        grid = QGridLayout()
        grid.setAlignment(Qt.AlignCenter)
        grid.setSpacing(10)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(1, 1)
        grid.setRowStretch(2, 1)        

        user_label = QLabel("Id usuario")
        user_label.setStyleSheet("color: white; font-size: 1.5em;")
        user_label.setMaximumSize(60, 50)
        grid.addWidget(user_label, 0, 0)

        user_id = QLineEdit()
        user_id.setStyleSheet("font-size: 1.5em; background-color: white; color: black;")
        user_id.setMaximumSize(300, 50)
        grid.addWidget(user_id, 0, 1)

        qr_image = QLabel()
        qr_image.setPixmap(QPixmap("images/qrcode.png").scaledToWidth(200).scaledToHeight(150))  
        qr_image.setScaledContents(False)
        qr_image.setAlignment(Qt.AlignCenter)
        grid.addWidget(qr_image, 1, 1)

        qr_label = QLabel("Escanee el código con la aplicación móvil cuando lo solicite")
        qr_label.setStyleSheet("color: #bdc3c7; font-size: 11px;")
        qr_label.setMaximumSize(400, 50)
        qr_label.setAlignment(Qt.AlignCenter)

        grid.addWidget(qr_label, 2, 1)

        grid.setRowMinimumHeight(0, 50)
        grid.setRowMinimumHeight(1, 200)
        grid.setRowMinimumHeight(2, 50)

        vbox_center.addWidget(welcome_label)
        vbox_center.addStretch(1)
        vbox_center.addLayout(grid)
        vbox_center.addStretch(1)

        hbox_bottom = QHBoxLayout()
        hbox_bottom.setAlignment(Qt.AlignCenter)
        hbox_bottom.setSpacing(10)

        next_button = QPushButton("Siguiente")
        next_button.setStyleSheet("background-color: #27ae60; color: white; font-size: 1.5em; font-weight: bold; padding: 10px 20px;")
        hbox_bottom.addWidget(next_button)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)
        central_layout.addLayout(hbox_top)
        central_layout.addLayout(vbox_center)
        central_layout.addLayout(hbox_bottom)

        next_button.clicked.connect(self.gotoLogin)
        

    def gotoLogin(self):
        self.login = LoginWindow()
        self.login.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovilUserWindow()
    window.show()
    sys.exit(app.exec_())