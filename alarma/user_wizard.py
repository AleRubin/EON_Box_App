import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit, QComboBox, QRadioButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from wizardMoviluser import MovilUserWindow
class UserWizard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Configuración de usuario")
        self.setGeometry(0, 0, 1920, 1080)

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
        # align center vertically and horizontally
        vbox_center.setAlignment(Qt.AlignCenter)
        vbox_center.setSpacing(20)

        welcome_label = QLabel("Configuración de usuario")
        welcome_label.setStyleSheet("color: white; font-size: 2em; font-weight: bold;")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setContentsMargins(0, 50, 0, 20)

        grid = QGridLayout()
        grid.setAlignment(Qt.AlignCenter)
        grid.setSpacing(10)

        user_id_label = QLabel("Id usuario")
        user_id_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(user_id_label, 0, 0)
        self.user_id_field = QLineEdit()
        grid.addWidget(self.user_id_field, 0, 1)
        self.user_id_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.user_id_field.setPlaceholderText("Ingrese un id de usuario")

        password_label = QLabel("Contraseña (6 dígitos numéricos)")
        password_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(password_label, 1, 0)
        self.password_field = QLineEdit()
        grid.addWidget(self.password_field, 1, 1)
        self.password_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.password_field.setPlaceholderText("Ingresar una contraseña numérica de 6 dígitos")
        self.password_field.setEchoMode(QLineEdit.Password)

        confirm_password_label = QLabel("Confirmar Contraseña")
        confirm_password_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(confirm_password_label, 2, 0)
        self.confirm_password_field = QLineEdit()
        grid.addWidget(self.confirm_password_field, 2, 1)
        self.confirm_password_field.setStyleSheet("color: black; font-size: 1.5em; background-color: white;")
        self.confirm_password_field.setPlaceholderText("Confirmar la contraseña")
        self.confirm_password_field.setEchoMode(QLineEdit.Password)

        email_label = QLabel("Ingrese un correo electrónico")
        email_label.setStyleSheet("color: white; font-size: 1.5em;")
        grid.addWidget(email_label, 3, 0)
        self.email_field = QLineEdit()
        grid.addWidget(self.email_field, 3, 1)
        self.email_field.setStyleSheet("color: black; font-size: 1.5em;")
        self.email_field.setStyleSheet("background-color: white;")
        self.email_field.setPlaceholderText("Ingrese un correo electrónico")

        vbox_center.addStretch(1)
        vbox_center.addWidget(welcome_label)
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

    def on_next_button_click(self):
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