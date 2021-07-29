from PyQt5 import QtCore, QtWidgets, QtGui
from user_interface.propMainWindow import Ui_PropMainWindow  # importa nuestro archivo generado
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

app = QtWidgets.QApplication([])
application = PropMainWindow()
application.show()
sys.exit(app.exec())
