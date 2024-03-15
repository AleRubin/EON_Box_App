from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QSize
from armado import Armado
from alertas import Alertas
from monitor import Monitor
from systemConfig import SystemConfig
class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main UI")
        self.setGeometry(0, 0,1024,600)
        self.setStyleSheet("background-color: rgba(38,64,67,255);")
    
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        hbox_top = QHBoxLayout()

        hbox_top.setAlignment(Qt.AlignLeft | Qt.AlignTop)  
        # hbox_top.setSpacing(1)

        logo_image_top_left = QLabel()
        logo_image_top_left.setPixmap(QPixmap("images/logo.png").scaledToWidth(40).scaledToHeight(40))      
        logo_image_top_left.setScaledContents(True)

        logo_image_top_right = QLabel()
        logo_image_top_right.setPixmap(QPixmap("images/titulo.png").scaledToWidth(198))  
        logo_image_top_right.setScaledContents(True)

        hbox_top.addWidget(logo_image_top_left)
        hbox_top.addWidget(logo_image_top_right)
        # hbox_top.addStretch(1)
        main_layout.addLayout(hbox_top)
        main_layout.addStretch(1)
        center_layout = QHBoxLayout()
        center_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(center_layout)
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        center_layout.addLayout(left_layout)

        button_home = QPushButton()
        button_home.setIcon(QIcon("images/info.png"))
        button_home.setIconSize(QSize(50, 50))
        button_home.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_home.clicked.connect(self.info)
        left_layout.addWidget(button_home)
        center_layout.addStretch(1)
        left_vbox = QVBoxLayout()
        left_vbox.setSpacing(10)
        left_vbox.setContentsMargins(10, 10, 10, 10)

        grid_label = QLabel("Fecha")
        grid_label.setStyleSheet("background-color: #ffffff; border-radius: 10px;")
        grid_label.setAlignment(Qt.AlignCenter)
        grid_label.setFont(QFont("Arial", 18))
        grid_label.setFixedWidth(200)
        left_vbox.addWidget(grid_label)

        center_layout.addLayout(left_vbox)

        right_vbox = QVBoxLayout()
        right_vbox.setSpacing(10)
        right_vbox.setContentsMargins(10, 10, 10, 10)

        labels = [
            {"text": "Estado del sistema", "background": "#e3c800", "weight": True, "top": 15},
            {"text": "Nombre del sensor armado", "background": "#ffffff", "top": 30},
            {"text": "Sensor 3 armado", "background": "#ffffff"},
            {"text": "Notificaciones", "background": "#ffffff", "underline": True, "underline_color": "red", "size": 18},
            {"text": "Alertas del sistema", "background": "#ffffff", "border": "2px solid red", "text_color": "red", "size": 20}
        ]

        for item in labels:
            label = QLabel(item["text"])
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet(f"background-color: {item['background']}; border-radius: 10px;")
            if "weight" in item:
                label.setFont(QFont("Arial", 18, QFont.Bold))
            if "top" in item:
                margin = f"margin-top: {item['top']}px;"
                label.setStyleSheet(label.styleSheet() + margin)
            if "underline" in item:
                label.setStyleSheet(label.styleSheet() + f"color: {item['underline_color']}; text-decoration: underline;")
                label.setFont(QFont("Arial", item["size"]))
            if "border" in item:
                label.setStyleSheet(label.styleSheet() + f"border: {item['border']}; color: {item['text_color']};")
                label.setFont(QFont("Arial", item["size"]))
            right_vbox.addWidget(label)
        center_layout.addLayout(right_vbox)
        bottom_layout = QVBoxLayout()
        center_layout.addLayout(bottom_layout)
        center_layout.addStretch(1)

        bottom_grid1 = QHBoxLayout()
        bottom_layout.addLayout(bottom_grid1)
        buttons_ad = [
            {"image_path": "images/armado.png", "action": self.gotoArmadoDesarmado},
            {"image_path": "images/alertas.png", "action": self.gotoAlertas}
        ]

        for item in buttons_ad:
            button = QPushButton()
            image = QPixmap(item["image_path"])
            scaled_pixmap = image.scaled(QSize(int(image.width() * 1.0), int(image.height() * 1.0)))
            button.setIcon(QIcon(scaled_pixmap))
            button.setIconSize(QPixmap(item["image_path"]).size() *1.0)
            button.setStyleSheet("background-color: rgba(38,64,67,255);")
            button.clicked.connect(item["action"])
            bottom_grid1.addWidget(button)

        # Second QHBoxLayout for Monitor, SOS, and Configuración buttons
        bottom_grid2 = QHBoxLayout()
        bottom_layout.addLayout(bottom_grid2)
        main_layout.addStretch(1)
        buttons_msc = [
            {"image_path": "images/monitor.png", "action": self.gotoMonitor},
            {"image_path": "images/sos.png", "action": self.gotoSOS},
            {"image_path": "images/configuracion.png", "action": self.gotoConfiguracion}
        ]

        for item in buttons_msc:
            button = QPushButton()
            image = QPixmap(item["image_path"])
            scaled_pixmap = image.scaled(QSize(int(image.width() * 1.0), int(image.height() * 1.0)))
            button.setIcon(QIcon(scaled_pixmap))
            button.setIconSize(QPixmap(item["image_path"]).size() * 1.0)
            button.setStyleSheet("background-color: rgba(38,64,67,255);")
            button.clicked.connect(item["action"])
            bottom_grid2.addWidget(button)
        self.showFullScreen()

    def gotoArmadoDesarmado(self):
        self.armado = Armado()
        self.armado.show()
        self.close()
    
    def gotoAlertas(self):
        self.alertas = Alertas()
        self.alertas.show()
        self.close()

    def gotoMonitor(self):
        self.monitor = Monitor()
        self.monitor.show()
        self.close()

    def gotoSOS(self):
        from sos import Sos
        self.sos = Sos()
        self.sos.show()
        self.close()

    def gotoConfiguracion(self):
        self.configuracion = SystemConfig()
        self.configuracion.show()
        self.close()

    def info(self):
        from info import Info
        self.info = Info()  
        self.info.show()
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    window = MainUI()
    window.show()
    app.exec_()
