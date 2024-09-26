from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class InicioWindow(QWidget):
    def __init__(self, app_state):
        super().__init__()

        self.vbox_center = QVBoxLayout()
        self.vbox_center.setAlignment(Qt.AlignCenter)
        self.vbox_center.setSpacing(20)

        self.welcome_label = QLabel(
            "Bienvenido a su sistema inteligente de Alarma")
        self.welcome_label.setStyleSheet("color: white; font-size: 40px;")
        self.welcome_label.setAlignment(Qt.AlignCenter)

        self.instruction_label = QLabel(
            "Para iniciar su configuración, el asistente lo guiará por tres sencillos pasos")
        self.instruction_label.setStyleSheet("color: white; font-size: 20px;")
        self.instruction_label.setAlignment(Qt.AlignCenter)

        self.vbox_center.addWidget(self.welcome_label)
        self.vbox_center.addWidget(self.instruction_label)

        self.setLayout(self.vbox_center)
