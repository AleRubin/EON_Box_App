from helloView import MainWindow
import sys
from PyQt5.QtWidgets import QApplication
def main():
    # Crear una instancia de QApplication
    app = QApplication(sys.argv)

    # Crear una instancia de la ventana principal de tu aplicación
    ventana_principal = MainWindow()
    ventana_principal.show()

    # Ejecutar el bucle de eventos de la aplicación
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
