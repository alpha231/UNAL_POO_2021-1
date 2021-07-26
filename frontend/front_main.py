from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication
from user_interface.main import Ui_MainWindow  # importa nuestro archivo generado
from user_interface.crearUsuario import Ui_crearUsuario
from user_interface.consultarUsuario import Ui_consultarUsuario
import sys
sys.path.append('backend_POO')
import model
import logic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        
        self.ui.actionCrearUsuario.triggered.connect(self.gotoCrearUsuario)
        self.ui.actionConsultarUsuario.triggered.connect(self.gotoConsultarUsuario)
        # self.ui.actionDesafiliarUsuario.triggered.connect(self.gotoDesafiliarUsuario)
        # self.ui.actionVacunarUsuario.triggered.connect(self.gotoVacunarUsuario)
        
        # self.ui.actionCrearLote.triggered.connect(self.gotoCrearLote)
        # self.ui.actionConsultaIndividualLote.triggered.connect(self.gotoConsultaIndLote)
        # self.ui.actionConsultaCompletaLote.triggered.connect(self.gotoConsultaComLote)
        
        # self.ui.actionCrearPlan.triggered.connect(self.gotoCrearPlan)
        # self.ui.actionConsultaIndividualPlan.triggered.connect(self.gotoConsultaIndPlan)
        # self.ui.actionConsultaCompletaPlan.triggered.connect(self.gotoConsultaComPlan)
        
        # self.ui.actionCrearProgramacion.triggered.connect(self.gotoCrearProgramacion)
        # self.ui.actionConsultaIndividualProgramacion.triggered.connect(self.gotoConsultaIndProgramacion)
        # self.ui.actionConsultaCompletaProgramacion.triggered.connect(self.gotoConsultaComProgramacion)
        
    def gotoCrearUsuario(self):
        self.anotherWindow = CrearUsuarioWindow()
        self.anotherWindow.show()
        self.hide()
    def gotoConsultarUsuario(self):
        self.anotherWindow = ConsultarUsuarioWindow()
        self.anotherWindow.show()
        self.hide()
       
class CrearUsuarioWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CrearUsuarioWindow, self).__init__()
        self.ui = Ui_crearUsuario()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        self.ui.pushButton.clicked.connect(self.btnBuscarClicked)
        self.ui.pushButton_2.clicked.connect(self.btnGuardarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
    def btnBuscarClicked(self):
        self.persona.noId = self.ui.noId.text()
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        if not resultado:
            self.ui.splitter_3.setEnabled(True)
            self.ui.pushButton_2.setEnabled(True)
        else:
            self.ui.splitter_3.setEnabled(False)
            self.ui.pushButton_2.setEnabled(False)
            
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
        self.persona.vacunado = 'N'
        self.persona.fechaDesafiliacion = None
        self.logicaPersona.crearUsuario(self.persona)
    
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()
     
class ConsultarUsuarioWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsultarUsuarioWindow, self).__init__()
        self.ui = Ui_consultarUsuario()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        self.ui.pushButton.clicked.connect(self.btnBuscarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
        self.ui.splitter_2.setVisible(False)
        self.ui.nombre.setReadOnly(True)
        self.ui.apellido.setReadOnly(True)
        self.ui.direccion.setReadOnly(True)
        self.ui.telefono.setReadOnly(True)
        self.ui.correo.setReadOnly(True)
        self.ui.ciudad.setReadOnly(True)
        self.ui.fechaNacimiento.setReadOnly(True)
        self.ui.fechaAfiliacion.setReadOnly(True)
        self.ui.vacunado_2.setCheckable(False)
        self.ui.fechaDesafiliacion_2.setReadOnly(True)
        
    def btnBuscarClicked(self):
        self.persona = model.Persona()
        self.persona.noId = self.ui.noId.text()
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        if resultado:
            self.persona = resultado
            self.ui.splitter_2.setVisible(True)
            self.ui.splitter_2.setEnabled(True)
            self.ui.splitter_3.setEnabled(True)
            self.ui.nombre.setText(self.persona.nombre)
            self.ui.apellido.setText(self.persona.apellido)
            self.ui.direccion.setText(self.persona.direccion)
            self.ui.telefono.setText(str(self.persona.telefono))
            self.ui.correo.setText(self.persona.correo)
            self.ui.ciudad.setText(self.persona.ciudad)
            # self.ui.fechaNacimiento.text
            # self.ui.fechaAfiliacion.text
            # self.ui.vacunado_2.text
            # self.ui.fechaDesafiliacion_2.text
        else:
            self.persona = resultado
            self.ui.splitter_2.setVisible(False)
            self.ui.splitter_3.setEnabled(False)
    
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

app = QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())