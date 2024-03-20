import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit, QComboBox, QRadioButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from wizardMoviluser import MovilUserWindow
import sqlite3
connection = sqlite3.connect("alarma.db")
cursor = connection.cursor()

class UserWizard(QMainWindow):
    def __init__(self):
        super().__init__()

        cursor.execute('SELECT * FROM cuenta')
        data = cursor.fetchone()
        user_id = data[1]

        self.setWindowTitle("Configuración de usuario")
        self.setGeometry(0, 0,1024,600)

        self.setStyleSheet("background-color: rgba(38,64,67,255);")

        hbox_top = QHBoxLayout()

        hbox_top.setAlignment(Qt.AlignLeft | Qt.AlignTop)  
        hbox_top.setSpacing(10)

        logo_image_top_left = QLabel()
            logo_image_top_left.setPixmap(QPixmap("images/logo.png").scaledToWidth(20).scaledToHeight(20))                  
        logo_image_top_left.setScaledContents(True)
        logo_image_top_right = QLabel()
        logo_image_top_right.setPixmap(QPixmap("images/titulo.png").scaledToWidth(198))  
        logo_image_top_right.setScaledContents(True)

        hbox_top.addWidget(logo_image_top_left)
        hbox_top.addWidget(logo_image_top_right)
        hbox_top.addStretch(1)
        
        vbox_center = QVBoxLayout()
        # align center vertically and horizontally
        vbox_center.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        vbox_center.setSpacing(20)

        welcome_label = QLabel("Configuración de usuario")
        welcome_label.setStyleSheet("color: white; font-size: 40px; font-weight: bold;")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setContentsMargins(0, 50, 0, 20)

        grid = QGridLayout()
        grid.setAlignment(Qt.AlignCenter)
        grid.setSpacing(10)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(1, 1)
        grid.setRowStretch(2, 1)
        grid.setRowStretch(3, 1)

        user_id_label = QLabel("Id usuario")
        user_id_label.setStyleSheet("color: white; font-size: 20px;")
        user_id_label.setMaximumSize(300, 50)
        grid.addWidget(user_id_label, 0, 0)
        self.user_id_field = QLineEdit()
        self.user_id_field.setText(user_id)
        self.user_id_field.setReadOnly(True)
        grid.addWidget(self.user_id_field, 0, 1)
        self.user_id_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.user_id_field.setMaximumSize(300, 50)
        self.user_id_field.setPlaceholderText("Ingrese un id de usuario")


        email_label = QLabel("Ingrese un correo electrónico")
        email_label.setStyleSheet("color: white; font-size: 20px;")
        email_label.setMaximumSize(300, 50)
        grid.addWidget(email_label, 1, 0)
        self.email_field = QLineEdit()
        grid.addWidget(self.email_field, 1, 1)
        self.email_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.email_field.setMaximumSize(300, 50)
        self.email_field.setPlaceholderText("Ingrese un correo electrónico")


        password_label = QLabel("Contraseña (6 dígitos numéricos)")
        password_label.setStyleSheet("color: white; font-size: 20px;")
        password_label.setMaximumSize(300, 50)
        grid.addWidget(password_label, 2, 0)
        self.password_edit = QLineEdit()
        grid.addWidget(self.password_edit, 2, 1)
        self.password_edit.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.password_edit.setMaximumSize(300, 50)
        self.password_edit.setPlaceholderText("Ingrese una contraseña")
        self.password_edit.setReadOnly(True)

        layout = QVBoxLayout()
        numpad_grid = QGridLayout()
        numpad_grid.setHorizontalSpacing(10)
        numpad_grid.setVerticalSpacing(10)

        buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "", "0", ""]
        positions = [(i, j) for i in range(4) for j in range(3)]

        for position, button_text in zip(positions, buttons):
            if button_text:
                button = QPushButton(button_text)
                button.clicked.connect(lambda _, text=button_text: self.on_numpad_button_click(text))
                button.setStyleSheet("min-width: 60px; min-height: 60px; background-color: black; color: white; font-size: 1.5em;")
                numpad_grid.addWidget(button, *position)

        
        layout.addLayout(numpad_grid)
        grid.addLayout(layout, 3, 1)

        grid.setRowMinimumHeight(0, 40)
        grid.setRowMinimumHeight(1, 40)
        grid.setRowMinimumHeight(2, 40)
        grid.setRowMinimumHeight(3, 40)

        vbox_center.addWidget(welcome_label)
        vbox_center.addStretch(1)
        vbox_center.addLayout(grid)
        vbox_center.addStretch(1)

        hbox_bottom = QHBoxLayout()
        hbox_bottom.setAlignment(Qt.AlignCenter)
        hbox_bottom.setSpacing(10)
        
        next_button = QPushButton("Siguiente")
        next_button.setStyleSheet("background-color: #2ecc71; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")

        hbox_bottom.addWidget(next_button)
        next_button.clicked.connect(self.on_next_button_click)

        back_button = QPushButton("Regresar")
        hbox_bottom.addWidget(back_button)
        back_button.setStyleSheet("background-color: #3498db; color: white; font-size: 1em; font-weight: bold; padding: 10px 20px;")
        back_button.clicked.connect(self.on_back_button_click)

        vbox_center.addLayout(hbox_bottom)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_layout = QVBoxLayout(central_widget)
        central_layout.addLayout(hbox_top)
        central_layout.addLayout(vbox_center)
        

    def on_numpad_button_click(self, text):
        self.password_edit.setText(self.password_edit.text() + text)

    def on_next_button_click(self):
        cursor.execute('UPDATE cuenta SET pin = ? WHERE id = ?', (self.password_edit.text(), 1))
        connection.commit()

        self.user_wizard = MovilUserWindow()
        self.user_wizard.show()
        self.close()

    def on_back_button_click(self):
        from wizzard import Wizard1Window
        self.wizard1 = Wizard1Window()
        self.wizard1.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserWizard()
    window.show()
    sys.exit(app.exec_())