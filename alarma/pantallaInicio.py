import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QLabel, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from wizzard import Wizard1Window

class InicioWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pantalla de Inicio")
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

         # Center Area
        vbox_center = QVBoxLayout()
        vbox_center.setAlignment(Qt.AlignCenter)
        vbox_center.setSpacing(20)

        welcome_label = QLabel("Bienvenido a su sistema inteligente de Alarma")
        welcome_label.setStyleSheet("color: white; font-size: 2em;")
        welcome_label.setAlignment(Qt.AlignCenter)

        instruction_label = QLabel("Para iniciar su configuración, el asistente lo guiará por tres sencillos pasos")
        instruction_label.setStyleSheet("color: white; font-size: 2em;")
        instruction_label.setAlignment(Qt.AlignCenter)

        button_start = QPushButton("Iniciar asistente")
        button_start.setStyleSheet("background-color: rgba(96,169,23,255); color: white; font-size: 1em;")
        button_start.clicked.connect(self.on_hello_button_click)
        vbox_center.addStretch(1)
        vbox_center.addWidget(welcome_label)
        vbox_center.addWidget(instruction_label)
        vbox_center.addWidget(button_start)
        vbox_center.addStretch(1)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)
        central_layout.addLayout(hbox_top)
        central_layout.addLayout(vbox_center)
        self.showFullScreen()

    def on_hello_button_click(self):
        self.wizard1_window = Wizard1Window()
        self.wizard1_window.show()
        self.hide()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    inicioWindow = InicioWindow()
    inicioWindow.show()
    sys.exit(app.exec_())
