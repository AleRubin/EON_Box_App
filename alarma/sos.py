from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize


class Sos(QWidget):
    def __init__(self, app_state):
        super().__init__()

        main_layout = QVBoxLayout()
        hbox_top = QHBoxLayout()

        hbox_top.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        hbox_top.setSpacing(1)

        logo_image_top_left = QLabel()
        logo_image_top_left.setPixmap(
            QPixmap("images/logo.png").scaledToWidth(40).scaledToHeight(40))
        logo_image_top_left.setScaledContents(True)

        logo_image_top_right = QLabel()
        logo_image_top_right.setPixmap(
            QPixmap("images/titulo.png").scaledToWidth(198))
        logo_image_top_right.setScaledContents(True)

        hbox_top.addWidget(logo_image_top_left)
        hbox_top.addWidget(logo_image_top_right)
        hbox_top.addStretch(1)
        main_layout.addLayout(hbox_top)
        center_layout = QHBoxLayout()
        main_layout.addLayout(center_layout)

        central_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        central_layout.addLayout(left_layout)

        button_home = QPushButton()
        button_home.setIcon(QIcon("images/home.png"))
        button_home.setIconSize(QSize(50, 50))
        button_home.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_home.clicked.connect(lambda: self.gotoHome(app_state))
        left_layout.addWidget(button_home)

        # Botón de Info
        button_info = QPushButton()
        button_info.setIcon(QIcon("images/info.png"))
        button_info.setIconSize(QSize(50, 50))
        button_info.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_info.clicked.connect(lambda: self.gotoInfo(app_state))
        left_layout.addWidget(button_info)

        vbox_layout = QVBoxLayout()
        vbox_layout.setAlignment(Qt.AlignCenter)

        warning_label = QLabel("Advertencia")
        warning_label.setStyleSheet(
            "color: white; font-size: 16px; background-color: #e74c3c; padding: 20px; border-radius: 5px; border-width: 2px;")
        vbox_layout.addWidget(warning_label)

        alert_label = QLabel("Alerta SOS")
        alert_label.setStyleSheet(
            "color: white; font-size: 24px; font-weight: bold; background-color: #e74c3c; padding: 20px; border-radius: 5px; border-width: 2px;")
        vbox_layout.addWidget(alert_label)

        alert_sent_label = QLabel("Su alerta ha sido enviada....")
        alert_sent_label.setStyleSheet(
            "color: white; font-size: 16px; background-color: #e74c3c; padding: 20px; border-radius: 5px; border-width: 2px;")
        vbox_layout.addWidget(alert_sent_label)

        central_layout.addItem(QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        central_layout.addLayout(vbox_layout)
        central_layout.addItem(QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        center_layout.addItem(QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        center_layout.addLayout(central_layout)
        center_layout.addItem(QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_layout.addLayout(center_layout)

        self.setLayout(main_layout)

    def gotoHome(self, app_state):
        app_state.set_stack(5)

    def gotoInfo(self, app_state):
        app_state.set_stack(8)
