import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QStackedLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from pantallaInicio import InicioWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicación de Saludo")
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
        vbox_center.setAlignment(Qt.AlignCenter)

        logo_image_center = QLabel()
        logo_image_center.setPixmap(QPixmap("images/logo.png").scaledToWidth(379))  # Escalar al ancho de 379
        logo_image_center.setScaledContents(True)

        text_label = QLabel("EON Innovaction")
        font = QFont()
        font.setPointSize(23)
        text_label.setFont(font)
        text_label.setStyleSheet("color: white;")
        
        vbox_center.addStretch(1)
        vbox_center.addWidget(logo_image_center)
        vbox_center.addWidget(text_label)
        vbox_center.addStretch(1)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)
        central_layout.addLayout(hbox_top)
        central_layout.addLayout(vbox_center)
        logo_image_center.mousePressEvent = self.switch_to_new_screen

    def switch_to_new_screen(self, event):
        self.inicio_window = InicioWindow()
        self.inicio_window.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
