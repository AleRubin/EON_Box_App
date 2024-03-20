from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QPixmap, QIcon

class Alertas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main UI")
        self.setGeometry(0, 0,1024,600)
        self.setStyleSheet("background-color: rgba(38,64,67,255); color: white;")

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        hbox_top = QHBoxLayout()

        hbox_top.setAlignment(Qt.AlignLeft | Qt.AlignTop)  
        hbox_top.setSpacing(1)

        logo_image_top_left = QLabel()
        logo_image_top_left.setPixmap(QPixmap("images/logo.png").scaledToWidth(20).scaledToHeight(20))               
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
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["No.", "Nom. de alarma", "Horario", "Tipo", "Duración", "Acciones"])
        table.setStyleSheet("background-color: rgba(255,255,255,255); color: black; border-radius: 10px;")

        # Establecer el tamaño de las columnas
        table.setColumnWidth(0, 50)  # No.
        table.setColumnWidth(1, 200)  # Nom. de alarma
        table.setColumnWidth(2, 100)  # Horario
        table.setColumnWidth(3, 150)  # Tipo
        table.setColumnWidth(4, 100)  # Duración
        table.horizontalHeader().setStretchLastSection(True)  
        
        data = [
            ("1", "Alarma 1", "10:00", "Tipo 1", "10 min", "Acción 1"),
            ("2", "Alarma 2", "11:00", "Tipo 2", "15 min", "Acción 2"),
            ("3", "Alarma 3", "12:00", "Tipo 3", "20 min", "Acción 3")
        ]
        for row, rowData in enumerate(data):
            table.insertRow(row)  
            for col, value in enumerate(rowData):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row, col, item)

            if row % 2 == 0:
                for col in range(table.columnCount()):
                    table.item(row, col).setBackground(QColor(200, 200, 200))  

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


if __name__ == "__main__":
    app = QApplication([])
    window = Alertas()
    window.show()
    app.exec_()
