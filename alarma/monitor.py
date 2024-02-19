from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QVBoxLayout, QFrame, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class Monitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main UI")
        self.setGeometry(0, 0, 1920, 1080)
        self.setStyleSheet("background-color: rgba(38,64,67,255); color: white;")

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        hbox_top = QHBoxLayout()

        hbox_top.setAlignment(Qt.AlignLeft | Qt.AlignTop)  

        logo_image_top_left = QLabel()
        logo_image_top_left.setPixmap(QPixmap("images/logo.png").scaledToWidth(40).scaledToHeight(40))      
        logo_image_top_left.setScaledContents(True)

        logo_image_top_right = QLabel()
        logo_image_top_right.setPixmap(QPixmap("images/titulo.png").scaledToWidth(198))  
        logo_image_top_right.setScaledContents(True)

        hbox_top.addWidget(logo_image_top_left)
        hbox_top.addWidget(logo_image_top_right)
        main_layout.addLayout(hbox_top)

        central_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        central_layout.addLayout(left_layout)

        button_home = QPushButton()
        button_home.setIcon(QIcon("images/home.png"))
        button_home.setIconSize(QSize(50, 50))
        button_home.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_home.clicked.connect(self.gotoHome)
        left_layout.addWidget(button_home)

        button_info = QPushButton()
        button_info.setIcon(QIcon("images/info.png"))
        button_info.setIconSize(QSize(50, 50))
        button_info.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_info.clicked.connect(self.gotoInfo)
        left_layout.addWidget(button_info)

        center_layout = QVBoxLayout()

        center_layout.setAlignment(Qt.AlignCenter)
        central_layout.addLayout(center_layout)

        button_monitor_exterior = QPushButton("Monitor exterior")
        button_monitor_exterior.setIcon(QIcon("images/camara.png"))
        button_monitor_exterior.setIconSize(QSize(200, 200))
        button_monitor_exterior.setStyleSheet("background-color: rgb(77, 128, 119); color: white;")
        center_layout.addWidget(button_monitor_exterior)

        button_monitor_interior = QPushButton("Monitor interior")
        button_monitor_interior.setIcon(QIcon("images/camara_interior.png"))
        button_monitor_interior.setIconSize(QSize(200, 200))
        button_monitor_interior.setStyleSheet("background-color: rgb(77, 128, 119); color: white;")
        center_layout.addWidget(button_monitor_interior)

        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        central_layout.addLayout(right_layout)

        # Frame para representar el video
        video_frame = QFrame()
        video_frame.setStyleSheet("background-color: black;")

        video_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        right_layout.addWidget(video_frame)
        main_layout.addLayout(central_layout)

    def gotoHome(self):
        from home import MainUI 
        self.window = MainUI()
        self.window.show()
        self.hide()

    def gotoInfo(self):
        from info import Info
        self.info = Info()
        self.info.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication([])
    window = Monitor()
    window.show()
    app.exec_()
