from PyQt5 import QtCore, QtWidgets, QtGui
from user_interface.crearVacunado import Ui_MainWindow  # importa nuestro archivo generado
import sys
sys.path.append('/home/alpha23/Juan/Programacion/unal/poo_2021/UNAL_POO_2021-1/backend_POO')
import model
import logic

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        self.ui.pushButton.clicked.connect(self.btnBuscarClicked)
        self.ui.pushButton_2.clicked.connect(self.btnGuardarClicked)
        
    def btnBuscarClicked(self):
        self.persona.noId = self.ui.noId.text()
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        if not resultado:
            self.ui.splitter_3.setEnabled(True)
            self.ui.pushButton_2.setEnabled(True)
            self.ui.vacunado.setEnabled(False)
            self.ui.fechaDesafiliacion.setEnabled(False)
            
    def btnGuardarClicked(self):
        self.persona.noId = self.ui.noId.text()
        self.persona.nombre = self.ui.nombre.text()
        self.persona.apellido = self.ui.apellido.text()
        self.persona.direccion = self.ui.direccion.text()
        self.persona.telefono = self.ui.telefono.text()
        self.persona.correo = self.ui.correo.text()
        self.persona.ciudad = self.ui.ciudad.text()
        self.persona.fechaNacimiento = self.ui.fechaNacimiento.date()
        self.persona.fechaAfiliacion = self.ui.fechaAfiliacion.date()
        if self.ui.vacunado.checkState() != True:
            self.persona.vacunado = 'N'
        self.persona.fechaDesafiliacion = None
        self.logicaPersona.crearUsuario(self.persona)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())