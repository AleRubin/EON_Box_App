from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFrame
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QSize

class Armado(QMainWindow):
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
        main_layout.addStretch(1)
        hbox = QHBoxLayout()
        main_layout.addLayout(hbox)
        central_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        central_layout.addLayout(left_layout)
        central_layout.addStretch(1)

        button_home = QPushButton()
        button_home.setIcon(QIcon("images/home.png"))
        button_home.setIconSize(QSize(50, 50))
        button_home.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_home.clicked.connect(self.gotoHome)
        left_layout.addWidget(button_home)

        armado_layout = QVBoxLayout()
        button_info = QPushButton()
        button_info.setIcon(QIcon("images/info.png"))
        button_info.setIconSize(QSize(50, 50))
        button_info.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_info.clicked.connect(self.gotoInfo)
        left_layout.addWidget(button_info)
        # Left VBox
        central_layout.addLayout(armado_layout)
        # Buttons in left VBox
        armado_desarmado_button = QPushButton()
        image = QPixmap("images/armado_desarmado_total1.png")
        scaled_pixmap = image.scaled(QSize(image.width() * 1.2, image.height() * 1.2))
        armado_desarmado_button.setIcon(QIcon(scaled_pixmap))
        armado_desarmado_button.setIconSize(QPixmap("images/armado_desarmado_total1.png").size() * 1.2)
        armado_desarmado_button.setStyleSheet("background-color: rgba(38,64,67,255); color: white; font-weight: bold;")
        armado_layout.addWidget(armado_desarmado_button)

        armado_sensor_buttons = [
            {"text": "Armado Sensor 1", "color": "rgb(77, 128, 119)"},
            {"text": "Armado Sensor 2", "color": "rgb(77, 128, 119)"},
            {"text": "Armado Sensor 3", "color": "rgb(77, 128, 119)"}
        ]

        for item in armado_sensor_buttons:
            button = QPushButton(item["text"])
            button.setStyleSheet(f"background-color: {item['color']}; color: white; font-weight: bold; font-size: 30px;")
            button.setFixedWidth(image.width() * 1.2 + 20)
            button.setFixedHeight(70)
            armado_layout.addWidget(button)

        # Right VBox
        right_vbox = QVBoxLayout()
        right_vbox.setAlignment(Qt.AlignCenter)
        right_vbox.setSpacing(20)
        right_vbox.setContentsMargins(20, 20, 20, 20)

        right_frame = QFrame()
        # right_vbox.addStretch(1)

        central_layout.addLayout(right_vbox)

        right_frame.setStyleSheet("background-color: rgba(38,64,67,255);")

        hbox.addWidget(right_frame)

        # Labels and Buttons in right VBox
        labels_and_buttons = [
            {"text": "Información de los sensores", "font_size": 20},
            {"text": "Sensor magnético 1", "input_placeholder": "Nombre_sensor", "button_texts": ["Armado", "Conexion del sensor", "En línea"]},
            {"text": "Sensor magnético 2", "input_placeholder": "Nombre_sensor", "button_texts": ["Desarmado", "Conexion del sensor", "Fuera de línea"]},
            {"text": "Sensor magnético 3", "input_placeholder": "Nombre_sensor", "button_texts": ["Armado", "Conexion del sensor", "En línea"]}
        ]

        for item in labels_and_buttons:
            if item["text"] == "Información de los sensores":
                label = QLabel(item["text"])
                label.setStyleSheet("color: white; font-size: 24px;")
                right_vbox.addWidget(label)
                right_vbox.addStretch(1)
                
            else:
                label = QLabel(item["text"])
                label.setStyleSheet("color: white;")
                label.setFont(QFont("Arial", item.get("font_size", 14)))
                right_vbox.addWidget(label)

            if "input_placeholder" in item:
                text_field = QLineEdit()
                text_field.setPlaceholderText(item["input_placeholder"])
                text_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
                text_field.setFixedHeight(40)
                text_field.setFixedWidth(400)
                right_vbox.addWidget(text_field)

            if "button_texts" in item:
                hbox_buttons = QHBoxLayout()
                hbox_buttons.setSpacing(10)
                for btn_text in item["button_texts"]:
                    if btn_text == "Armado":
                        button = QPushButton(btn_text)
                        button.setStyleSheet("background-color: #e74c3c; color: white; font-weight: bold;")
                        hbox_buttons.addWidget(button)
                    elif btn_text == "Desarmado":
                        button = QPushButton(btn_text)
                        button.setStyleSheet("background-color: #27ae60; color: white; font-weight: bold;")
                        hbox_buttons.addWidget(button)
                    elif btn_text == "Conexion del sensor":
                        button = QPushButton(btn_text)
                        button.setStyleSheet("background-color: #000000; color: white; font-weight: bold;")
                        hbox_buttons.addWidget(button)
                    elif btn_text == "Fuera de línea":
                        button = QPushButton(btn_text)
                        button.setStyleSheet("background-color: #e74c3c; color: white; font-weight: bold;")
                        hbox_buttons.addWidget(button)
                    elif btn_text == "En línea":
                        button = QPushButton(btn_text)
                        button.setStyleSheet("background-color: #27ae60; color: white; font-weight: bold;")
                        hbox_buttons.addWidget(button)
                    else:
                        button = QPushButton(btn_text)
                        button.setStyleSheet("background-color: rgba(38,64,67,255); color: white; font-weight: bold;")
                        hbox_buttons.addWidget(button)
                right_vbox.addLayout(hbox_buttons)
        central_layout.addStretch(1)
        main_layout.addLayout(central_layout)
        main_layout.addStretch(1)
        # main_layout.addStretch(1)
        

    def gotoHome(self):
            from home import MainUI
            self.main_ui = MainUI()
            self.main_ui.show()
            self.hide()

    def gotoInfo(self):
            print("Info")

if __name__ == "__main__":
    app = QApplication([])
    window = Armado()
    window.show()
    app.exec_()