from PyQt5 import QtCore, QtWidgets, QtGui
from user_interface.propMainWindow import Ui_PropMainWindow  # importa nuestro archivo generado
from user_interface.crearVacunado import Ui_MainWindow 
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


     def abrir_crearVacunado(self):
         self.crearVacunadoWindow=QtWidgets.QMainWindow()
         self.ui=Ui_MainWindow()
         self.ui.setupUi(self.crearVacunadoWindow)
         self.crearVacunadoWindow.show()
         

app = QtWidgets.QApplication([])
application = PropMainWindow()
application.show()
sys.exit(app.exec())
