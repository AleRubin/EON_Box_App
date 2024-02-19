from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

class WarningSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Warning System")
        self.setGeometry(0, 0, 1920, 1080)
        self.setStyleSheet("background-color: rgba(38,64,67,255);")
    
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        hbox_top = QHBoxLayout()

        hbox_top.setAlignment(Qt.AlignLeft | Qt.AlignTop)  
        hbox_top.setSpacing(1)

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
        # Layout para la parte izquierda
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        center_layout.addLayout(left_layout)

        # Botón de Home
        button_home = QPushButton()
        button_home.setIcon(QIcon("images/home.png"))
        button_home.setIconSize(QSize(50, 50))
        button_home.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_home.clicked.connect(self.gotoHome)
        left_layout.addWidget(button_home)

        # Botón de Info
        button_info = QPushButton()
        button_info.setIcon(QIcon("images/info.png"))
        button_info.setIconSize(QSize(50, 50))
        button_info.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_info.clicked.connect(self.gotoInfo)
        left_layout.addWidget(button_info)

       
        frame = QFrame()
        frame.setStyleSheet("background-color: rgba(0,80,239,255); border-radius: 10px;") # Rectángulo azul con bordes redondeados
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
    def gotoHome(self):
        from home import MainUI 
        self.window = MainUI()
        self.window.show()
        self.hide()

    def gotoInfo(self):
        from info import Info
        self.window = Info()
        self.window.show()
        self.hide()
        

if __name__ == "__main__":
    app = QApplication([])
    window = WarningSystem()
    window.show()
    app.exec_()
