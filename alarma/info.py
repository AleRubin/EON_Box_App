from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QScrollArea, QScrollArea, QScrollArea, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
class Info(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main UI")
        self.setGeometry(0, 0, 1024, 600)
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
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        center_layout.addLayout(left_layout)

        info_layout = QVBoxLayout()
        button_home = QPushButton()
        button_home.setIcon(QIcon("images/home.png"))
        button_home.setIconSize(QSize(50, 50))
        button_home.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_home.clicked.connect(self.gotoHome)
        left_layout.addWidget(button_home)
        content_widget = QWidget()
        scroll_area.setWidget(content_widget)
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(10)
        content_widget.setStyleSheet("background-color: #ecf0f1;")

        label_info = QLabel("Información")
        label_info.setStyleSheet("font-size: 24px; font-weight: bold; padding: 4px;")
        label_info.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(label_info)

        label_heading = QLabel("Heading")
        label_heading.setStyleSheet("font-size: 18px; font-weight: bold;")
        content_layout.addWidget(label_heading)

        label_paragraph1 = QLabel("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        label_paragraph1.setWordWrap(True)
        content_layout.addWidget(label_paragraph1)

        label_paragraph2 = QLabel("Información del loggeo con la nube EON")
        label_paragraph2.setWordWrap(True)
        content_layout.addWidget(label_paragraph2)

        scroll_area.setStyleSheet("border: none;")
        scroll_area.setContentsMargins(50, 20, 50, 20)

        info_layout.addWidget(scroll_area)
        center_layout.addLayout(info_layout)
        main_layout.addLayout(center_layout)
        self.showFullScreen()

    def gotoHome(self):
        from home import MainUI
        self.home = MainUI()
        self.home.show()
        self.hide()
if __name__ == "__main__":
    app = QApplication([])
    window = Info()
    window.show()
    app.exec_()
