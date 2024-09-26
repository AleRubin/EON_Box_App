import sys
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class HelloView(QWidget):
    def __init__(self, app_state):
        super().__init__()
        self.layout_hello = QHBoxLayout()

        self.layout_hello.addStretch(1)

        self.logo_image_top_right = QLabel()
        self.logo_image_top_right.setPixmap(
            QPixmap("images/titulo.png")
            .scaled(500, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        self.layout_hello.addWidget(self.logo_image_top_right)
        self.layout_hello.addStretch(1)
        self.setLayout(self.layout_hello)

        