import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMenuBar, QMainWindow, QAction, QStackedWidget, QVBoxLayout, QPushButton, QWidget, QLabel, QHBoxLayout
from helloView import HelloView
from pantallaInicio import InicioWindow
from wizzard import Wizard1Window
from advancedWizard import AdvancedWizard
from wizzard1 import LoginWindow
from getmac import get_mac_address as gma
from home import MainUI
from alertas import Alertas
from  monitor import Monitor
from  sos import Sos
from armado import Armado
from systemConfig import SystemConfig
import json
import requests
import time

import sqlite3
connection = sqlite3.connect("alarma.db")
cursor = connection.cursor()


class AppState:
    def __init__(self):
        self.id = 0
        self.stack = QStackedWidget()

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def get_stack(self):
        return self.stack.currentIndex()
    
    def set_stack(self, index):
        self.stack.setCurrentIndex(index)
    
    def stack_count(self):
        return self.stack.count()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Caja")
        self.setGeometry(0, 0, 1024, 600)
        self.setStyleSheet("background-color: rgba(38,64,67,255);")

        app_state = AppState()

        app_state.set_id(self._getBaseDatos())
        self.widget_central = QWidget(self)
        self.setCentralWidget(self.widget_central)
        self.layout = QVBoxLayout(self.widget_central)

        self.step1 = HelloView(app_state)
        self.step2 = InicioWindow(app_state)
        self.step3 = Wizard1Window(app_state)
        self.step4 = AdvancedWizard(app_state)
        self.step5 = LoginWindow(app_state)
        self.step6 = MainUI(app_state)
        self.step7 = Armado(app_state)
        self.step8 = Alertas(app_state)
        self.step9 = Monitor(app_state)
        self.step10 = Sos(app_state)
        self.step11 = SystemConfig(app_state)

        app_state.stack.addWidget(self.step1)
        app_state.stack.addWidget(self.step2)
        app_state.stack.addWidget(self.step3)
        app_state.stack.addWidget(self.step4)
        app_state.stack.addWidget(self.step5)
        app_state.stack.addWidget(self.step6)
        app_state.stack.addWidget(self.step7)
        app_state.stack.addWidget(self.step8)
        app_state.stack.addWidget(self.step9)
        app_state.stack.addWidget(self.step10)
        app_state.stack.addWidget(self.step11)

        self.layout_botones = QHBoxLayout()
        self.boton_anterior = QPushButton("Anterior", self)
        self.boton_anterior.setStyleSheet(
            """
            QPushButton {
                width: 100px;
                background-color: orange;
                color: white;  /* Texto en blanco */
                border-radius: 10px;  /* Esquinas redondeadas */
                padding: 10px 20px;  /* Espaciado */
                font-size: 16px;  /* Tamaño de fuente */
            }
            QPushButton:hover {
                background-color: #45a049;  /* Color más oscuro al pasar el mouse */
            }
            QPushButton:pressed {
                background-color: #2e7d32;  /* Color aún más oscuro al hacer clic */
            }
        """)
        self.boton_siguiente = QPushButton("Siguiente", self)
        self.boton_siguiente.setStyleSheet(
            """
            QPushButton {
                width: 100px;
                background-color: #4CAF50;  /* Fondo verde */
                color: white;  /* Texto en blanco */
                border-radius: 10px;  /* Esquinas redondeadas */
                padding: 10px 20px;  /* Espaciado */
                font-size: 16px;  /* Tamaño de fuente */
            }
            QPushButton:hover {
                background-color: #45a049;  /* Color más oscuro al pasar el mouse */
            }
            QPushButton:pressed {
                background-color: #2e7d32;  /* Color aún más oscuro al hacer clic */
            }
        """)

        self.boton_anterior.clicked.connect(lambda: self.paso_anterior(app_state))
        self.boton_siguiente.clicked.connect(lambda: self.siguiente_paso(app_state))

        self.layout_botones.addStretch()  # Espaciador a la izquierda
        self.layout_botones.addWidget(self.boton_anterior)
        self.layout_botones.addWidget(self.boton_siguiente)
        self.layout_botones.addStretch()  # Espaciador a la derecha

        self.layout.addWidget(app_state.stack)
        self.layout.addLayout(self.layout_botones)

        self.setLayout(self.layout)

        app_state.set_stack(0)

        self._validarIdYMandarPost(app_state)

    def _validarIdYMandarPost(self, app_state):
        # intervalo de 30 segundos
        # mandar post a la API
        id = self._getBaseDatos()
        if id:
            pass

    def _createMenuBar(self):
        menuBar = QMenuBar(self)

        helpMenu = menuBar.addMenu("Help")
        helpMenu.addAction("About")
        helpMenu.addAction("Exit")
        menuBar.addMenu(helpMenu)

        helpMenu.addAction(self.aboutAction)
        helpMenu.addAction(self.exitAction)

        self.setMenuBar(menuBar)

    def _createActions(self):
        self.aboutAction = QAction("About", self)
        self.exitAction = QAction("Exit", self)

    def _getBaseDatos(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS cuenta (id INTEGER, id_nube TEXT, mac TEXT, identificador TEXT, nombre TEXT, pin TEXT, fk_idCatEstatusDispositivo INT)")
        cursor.execute('SELECT * FROM cuenta')
        informacion = cursor.fetchone()
        id = 0
        if informacion:
            id = informacion[0]

        return id

    def siguiente_paso(self, app_state):
        indice_actual = app_state.get_stack()

        if indice_actual < app_state.stack_count() - 1:
            app_state.set_stack(indice_actual + 1)

        if indice_actual == 0:
            self.boton_siguiente.setText("Iniciar asistente")
            self.boton_siguiente.setStyleSheet(
                """
                QPushButton {
                    width: 200px;
                    background-color: #4CAF50;  /* Fondo verde */
                    color: white;  /* Texto en blanco */
                    border-radius: 10px;  /* Esquinas redondeadas */
                    padding: 10px 20px;  /* Espaciado */
                    font-size: 16px;  /* Tamaño de fuente */
                }
                QPushButton:hover {
                    background-color: #45a049;  /* Color más oscuro al pasar el mouse */
                }
                QPushButton:pressed {
                    background-color: #2e7d32;  /* Color aún más oscuro al hacer clic */
                }
            """)
        elif indice_actual == 1:
            self.boton_siguiente.setText("Siguiente")

        if(app_state.get_stack() > 1):
            self.hide_layout_widgets(self.layout_botones)

    def hide_layout_widgets(self, layout):
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.hide()

    def paso_anterior(self, app_state):
        indice_actual = app_state.get_stack()
        if indice_actual > 0:
            app_state.set_stack(indice_actual - 1)

    def keyPressEvent(self, event):
        # Verificar si la tecla presionada es 'Q' o 'q'
        if event.key() == ord('Q') or event.key() == ord('q'):
            self.close()  # Cerrar la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = MainWindow()
    ventana_principal.show()
    sys.exit(app.exec_())
