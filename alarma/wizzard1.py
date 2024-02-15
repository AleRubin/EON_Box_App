import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 640, 480)

        self.setStyleSheet("background-color: rgba(38,64,67,255);")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)

        logo_top_left = QLabel()
        pixmap_left = QPixmap("../images/logo.png")
        logo_top_left.setPixmap(pixmap_left)
        top_layout.addWidget(logo_top_left)

        logo_top_right = QLabel()
        pixmap_right = QPixmap("../images/titulo.png")
        logo_top_right.setPixmap(pixmap_right)
        top_layout.addWidget(logo_top_right)

        center_layout = QVBoxLayout()
        layout.addLayout(center_layout)

        password_label = QLabel("Ingrese su contraseña de acceso")
        center_layout.addWidget(password_label)

        self.password_field = QLineEdit()
        center_layout.addWidget(self.password_field)

        num_pad_layout = QVBoxLayout()
        center_layout.addLayout(num_pad_layout)

        row1_layout = QHBoxLayout()
        num_pad_layout.addLayout(row1_layout)
        for i in range(1, 4):
            button = QPushButton(str(i))
            row1_layout.addWidget(button)

        row2_layout = QHBoxLayout()
        num_pad_layout.addLayout(row2_layout)
        for i in range(4, 7):
            button = QPushButton(str(i))
            row2_layout.addWidget(button)

        row3_layout = QHBoxLayout()
        num_pad_layout.addLayout(row3_layout)
        for i in range(7, 10):
            button = QPushButton(str(i))
            row3_layout.addWidget(button)

        row4_layout = QHBoxLayout()
        num_pad_layout.addLayout(row4_layout)
        zero_button = QPushButton("0")
        row4_layout.addWidget(zero_button)

        login_button = QPushButton("Ingresar")
        center_layout.addWidget(login_button)

        left_layout = QVBoxLayout()
        layout.addLayout(left_layout)

        info_button = QPushButton()
        info_button.setIcon(QIcon("../images/info.png"))
        info_button.setIconSize(QSize(61, 51))
        left_layout.addWidget(info_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
