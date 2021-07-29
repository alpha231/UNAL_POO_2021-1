from PyQt5 import QtCore, QtWidgets, QtGui
from user_interface.propMainWindow import Ui_PropMainWindow  # importa nuestro archivo generado
from user_interface.crearVacunado import Ui_MainWindow 
import webbrowser
import sys
sys.path.append('backend_POO')
import model
import logic

class PropMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
       super(PropMainWindow, self).__init__()
       self.ui = Ui_PropMainWindow()
       self.ui.setupUi(self)
       self.persona = model.Persona()
       self.logicaPersona = logic.Persona()
       self.ui.actionCrear_5.triggered.connect(self.abrir_crearVacunado)
       self.ui.DocumentacionUsuario.clicked.connect(self.ayudaUsuario)

    def abrir_crearVacunado(self):
        self.crearVacunadoWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.crearVacunadoWindow)
        self.crearVacunadoWindow.show()

    def ayudaUsuario(self):
        # Se almacena un link correspondiente a la ubicación del pdf
        path = 'https://drive.google.com/file/d/1L8BBeJP-mc_QLmNplzYemZgxe4j1F_Bx/view?usp=sharing'
        # Abrimos el archivo en el navegador siguiendo la variable (path) por el método webbrowser.open_new() de la librería webbrowser
        webbrowser.open_new(path)
        

app = QtWidgets.QApplication([])
application = PropMainWindow()
application.show()
sys.exit(app.exec())
