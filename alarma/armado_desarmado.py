from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

class WarningSystem(QWidget):
    def __init__(self, app_state):
        super().__init__()

        main_layout = QVBoxLayout()
        
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
        main_layout.addLayout(hbox_top)

        center_layout = QHBoxLayout()
        main_layout.addLayout(center_layout)

        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        center_layout.addLayout(left_layout)

        button_home = QPushButton()
        button_home.setIcon(QIcon("images/home.png"))
        button_home.setIconSize(QSize(50, 50))
        button_home.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_home.clicked.connect(lambda: self.gotoHome(app_state))
        left_layout.addWidget(button_home)

        button_info = QPushButton()
        button_info.setIcon(QIcon("images/info.png"))
        button_info.setIconSize(QSize(50, 50))
        button_info.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_info.clicked.connect(lambda: self.gotoInfo(app_state))
        left_layout.addWidget(button_info)

        frame = QFrame()
        frame.setStyleSheet("background-color: rgba(0,80,239,255); border-radius: 10px;")
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Expande en todas direcciones
        frame_layout = QVBoxLayout(frame)
        
        warning_label = QLabel("Advertencia")
        warning_label.setStyleSheet("color: white; font-size: 24px; padding: 20px; background-color: #e74c3c; border-top-left-radius: 10px; border-top-right-radius: 10px;")
        frame_layout.addWidget(warning_label)

        status_label = QLabel("Sistema Armado/desarmado")
        status_label.setStyleSheet("color: white; font-size: 24px; padding: 20px;")
        frame_layout.addWidget(status_label)

        message_label = QLabel("Su sistema está armado/Su sistema está armado/desarmado parcialmente")
        message_label.setStyleSheet("color: white; font-size: 24px; padding: 20px;")
        frame_layout.addWidget(message_label)

        center_layout.addWidget(frame)

        self.setLayout(main_layout)

    def gotoHome(self, app_state):
        app_state.set_stack(5)

    def gotoInfo(self, app_state):
        app_state.set_stack(8)