from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QPixmap, QIcon
import requests

class Alertas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main UI")
        self.setGeometry(0, 0,1024,570)
        self.setStyleSheet("background-color: rgba(38,64,67,255); color: white;")

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
        central_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        central_layout.addLayout(left_layout)
        main_layout.addLayout(central_layout)

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
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignCenter)
        vbox.setSpacing(20)
        vbox.setContentsMargins(20, 20, 20, 20)
        central_layout.addLayout(vbox)
        # main_layout.addLayout(vbox)

        label = QLabel("Registro de alertas del sistema")
        label.setStyleSheet("font-size: 26px; color: white;")  # Cambia el color del título de las columnas
        label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(label)

        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["id", "estado", "fecha", "activo", "id_componente"])
        table.setStyleSheet("background-color: rgba(255,255,255,255); color: black; border-radius: 10px;")

        # Establecer el tamaño de las columnas
        table.setColumnWidth(0, 50)
        table.setColumnWidth(1, 200)
        table.setColumnWidth(2, 300)
        table.setColumnWidth(3, 150)
        table.setColumnWidth(4, 150)
        table.horizontalHeader().setStretchLastSection(True)  
        
        data = requests.get("https://cloudsecurity-api.eonproduccion.net/api/log_componentes/2").json()
        data = data["data"]
        for row, rowData in enumerate(data):
            table.insertRow(row)
            for col, value in enumerate(rowData.items()):
                table.setItem(row, col, QTableWidgetItem(str(value[1])))
                # center text
                table.item(row, col).setTextAlignment(Qt.AlignCenter)
                
                
        vbox.addWidget(table)
        


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


if __name__ == "_main_":
    app = QApplication([])
    window = Alertas()
    window.show()
    app.exec_()