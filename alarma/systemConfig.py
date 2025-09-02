from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt

class SystemConfig(QWidget):
    def __init__(self, app_state):
        super().__init__()

        main_layout = QVBoxLayout()
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
        main_layout.addStretch(1)
        central_layout = QHBoxLayout()
        main_layout.addLayout(central_layout)

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
        central_layout.addStretch(1)
        grid_layout = QGridLayout()
        central_layout.addLayout(grid_layout)
        central_layout.addStretch(1)
        main_layout.addLayout(grid_layout)
        grid_layout.setAlignment(Qt.AlignCenter)
        buttons_info = [
            ("images/retardo.png", "Retardo", 0, 0, self.gotoRetardo),
            ("images/conexion_nube.png", "Conexion nube EON", 0, 1, self.gotoConexionNube),
            ("images/cambiar_correo.png", "Cambiar correo electronico", 0, 2, self.gotoCambiarCorreo),
            ("images/tiempo_hora.png", "Tiempo y hora", 0, 3, self.gotoTiempoHora),
            ("images/configuracion_red.png", "Configuracion de red", 1, 0, self.gotoConfiguracionRed),
            ("images/restaurar.png", "Restaurar valores de fabrica", 1, 1, self.gotoRestaurarValores),
            ("images/cambiar_contrasenia.png", "Cambiar contraseña", 1, 2, self.gotoCambiarContrasenia),
            ("images/apagar.png", "Apagar equipo", 1, 3, self.gotoApagarEquipo) 
        ]

        for url, label_text, row, column, function in buttons_info:
            button = QPushButton()
            button.setStyleSheet("background-color: rgb(77, 128, 119); color: white; font-size: 11px;")
            button.setFixedSize(int(400*0.55), int(400*0.55))

            icon_label = QLabel()
            icon_label.setPixmap(QPixmap(url).scaledToWidth(int(150*0.55)))  
            icon_label.setAlignment(Qt.AlignCenter)
            text_label = QLabel(label_text)
            text_label.setAlignment(Qt.AlignCenter)

            layout = QVBoxLayout(button)
            layout.addStretch(1)
            layout.addWidget(icon_label)
            layout.addStretch(1)
            layout.addWidget(text_label)
            layout.setAlignment(Qt.AlignCenter)  

            button.clicked.connect(function)

            grid_layout.addWidget(button, row, column)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

    
    def gotoHome(self, app_state):
        app_state.set_stack(5)

    def gotoInfo(self, app_state):
        app_state.set_stack(8)

    def gotoRetardo(self):
        print("Go to Retardo")

    def gotoConexionNube(self):
        print("Go to Conexion Nube")

    def gotoCambiarCorreo(self):
        print("Go to Cambiar Correo")

    def gotoTiempoHora(self):
        print("Go to Tiempo Hora")

    def gotoConfiguracionRed(self):
        print("Go to Configuracion Red")

    def gotoRestaurarValores(self):
        print("Go to Restaurar Valores")

    def gotoCambiarContrasenia(self):
        print("Go to Cambiar Contrasenia")

    def gotoApagarEquipo(self):
        print("Go to Apagar Equipo")
