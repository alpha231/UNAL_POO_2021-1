from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication
from user_interface.main import Ui_MainWindow  # importa nuestro archivo generado
from user_interface.propMainWindow import Ui_PropMainWindow  # importa nuestro archivo generado
from user_interface.crearUsuario import Ui_crearUsuario
from user_interface.consultarUsuario import Ui_consultarUsuario
from user_interface.desafiliarUsuario import Ui_desafiliarUsuario
from user_interface.vacunarUsuario import Ui_vacunarUsuario
import sys
sys.path.append('backend_POO')
import model
import logic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_PropMainWindow()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        
        self.ui.actionCrearUsuario.triggered.connect(self.gotoCrearUsuario)
        self.ui.actionConsultarUsuario.triggered.connect(self.gotoConsultarUsuario)
        self.ui.actionDesafiliarUsuario.triggered.connect(self.gotoDesafiliarUsuario)
        self.ui.actionVacunarUsuario.triggered.connect(self.gotoVacunarUsuario)
        
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
        self.close()
    def gotoConsultarUsuario(self):
        self.anotherWindow = ConsultarUsuarioWindow()
        self.anotherWindow.show()
        self.close()
    def gotoDesafiliarUsuario(self):
        self.anotherWindow = DesafiliarUsuarioWindow()
        self.anotherWindow.show()
        self.close()
    def gotoVacunarUsuario(self):
        self.anotherWindow = VacunarUsuarioWindow()
        self.anotherWindow.show()
        self.close()
       
class CrearUsuarioWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CrearUsuarioWindow, self).__init__()
        self.ui = Ui_crearUsuario()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        self.ui.noId.textEdited.connect(self.BuscarUsuario)
        self.ui.pushButton_2.clicked.connect(self.btnGuardarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
    def BuscarUsuario(self):
        self.persona.noId = self.ui.noId.text()
        if self.persona.noId != '':
            resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
            if not resultado:
                self.ui.splitter_3.setEnabled(True)
                self.ui.pushButton_2.setEnabled(True)
                self.ui.mensaje.setText('')
            else:
                self.ui.splitter_3.setEnabled(False)
                self.ui.pushButton_2.setEnabled(False)
                self.ui.mensaje.setText('<font color="red">El usuario con el numero de documento '+self.persona.noId+' ya existe</font>')
            
    def btnGuardarClicked(self):
        self.persona.noId = self.ui.noId.text()
        self.persona.noId = self.ui.noId.text()
        self.persona.nombre = self.ui.nombre.text()
        self.persona.apellido = self.ui.apellido.text()
        self.persona.direccion = self.ui.direccion.text()
        self.persona.telefono = self.ui.telefono.text()
        self.persona.correo = self.ui.correo.text()
        self.persona.ciudad = self.ui.ciudad.text()
        fechaNacimiento = self.ui.fechaNacimiento.date()
        fechaAfiliacion = self.ui.fechaAfiliacion.date()
        self.persona.fechaNacimiento = fechaNacimiento
        self.persona.fechaAfiliacion = fechaAfiliacion
        self.persona.vacunado = 'N'
        self.persona.fechaDesafiliacion = None
        self.logicaPersona.crearUsuario(self.persona)
        self.ui.mensaje.setText('El paciente ha sido creado')
        self.ui.pushButton.setEnabled(False)
    
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
        
        self.ui.nombre.setText('')
        self.ui.apellido.setText('')
        self.ui.direccion.setText('')
        self.ui.telefono.setText('')
        self.ui.correo.setText('')
        self.ui.ciudad.setText('')
        self.ui.fechaNacimiento.setText('')
        self.ui.fechaAfiliacion.setText('')
        self.ui.vacunado.setText('')
        self.ui.fechaDesafiliacion.setText('')
        
    def btnBuscarClicked(self):
        self.persona = model.Persona()
        self.persona.noId = self.ui.noId.text()
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        if resultado:
            self.persona = resultado
            self.ui.nombre.setText(self.persona.nombre)
            self.ui.apellido.setText(self.persona.apellido)
            self.ui.direccion.setText(self.persona.direccion)
            self.ui.telefono.setText(str(self.persona.telefono))
            self.ui.correo.setText(self.persona.correo)
            self.ui.ciudad.setText(self.persona.ciudad)
            self.ui.fechaNacimiento.setText(str(self.persona.fechaNacimiento))
            self.ui.fechaAfiliacion.setText(str(self.persona.fechaAfiliacion))
            if self.persona.vacunado == 'S':
                self.ui.vacunado.setText('Si')
            else:
                self.ui.vacunado.setText('No')
            if self.persona.fechaDesafiliacion:
                self.ui.fechaDesafiliacion.setText(self.persona.fechaDesafiliacion)
            else:
                self.ui.fechaDesafiliacion.setText('La persona continua afiliada')
            self.ui.mensaje.setText('')
        else:
            self.ui.nombre.setText('')
            self.ui.apellido.setText('')
            self.ui.direccion.setText('')
            self.ui.telefono.setText('')
            self.ui.correo.setText('')
            self.ui.ciudad.setText('')
            self.ui.fechaNacimiento.setText('')
            self.ui.fechaAfiliacion.setText('')
            self.ui.vacunado.setText('')
            self.ui.fechaDesafiliacion.setText('')
            self.ui.mensaje.setText('<font color="red">El usuario con el numero de documento '+self.persona.noId+' no existe</font>')
    
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

class DesafiliarUsuarioWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(DesafiliarUsuarioWindow, self).__init__()
        self.ui = Ui_desafiliarUsuario()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        self.ui.noId.textEdited.connect(self.BuscarUsuario)
        self.ui.pushButton_2.clicked.connect(self.btnActualizarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        self.ui.pushButton_2.setEnabled(False)
        
    def BuscarUsuario(self):
        self.persona.noId = self.ui.noId.text()
        if self.persona.noId != '':
            resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
            if resultado:
                self.persona = resultado
                self.ui.nombre.setText(self.persona.nombre)
                self.ui.apellido.setText(self.persona.apellido)
                self.ui.direccion.setText(self.persona.direccion)
                self.ui.telefono.setText(str(self.persona.telefono))
                self.ui.correo.setText(self.persona.correo)
                self.ui.ciudad.setText(self.persona.ciudad)
                self.ui.fechaNacimiento.setText(str(self.persona.fechaNacimiento))
                self.ui.fechaAfiliacion.setText(str(self.persona.fechaAfiliacion))
                if self.persona.vacunado == 'S':
                    self.ui.vacunado.setText('Si')
                else:
                    self.ui.vacunado.setText('No')
                if self.persona.fechaDesafiliacion:
                    self.ui.mensaje.setText('Este usuario ya es encuentra desafiliado')
                    self.ui.fechaAfiliacion.setEnabled(False)
                    self.ui.pushButton_2.setEnabled(False)
                else:
                    self.ui.fechaAfiliacion.setEnabled(True)
                    self.ui.pushButton_2.setEnabled(True)
            else:
                self.ui.nombre.setText('')
                self.ui.apellido.setText('')
                self.ui.direccion.setText('')
                self.ui.telefono.setText('')
                self.ui.correo.setText('')
                self.ui.ciudad.setText('')
                self.ui.fechaNacimiento.setText('')
                self.ui.fechaAfiliacion.setText('')
                self.ui.vacunado.setText('')
                self.ui.fechaAfiliacion.setEnabled(False)
                self.ui.pushButton_2.setEnabled(False)
                self.ui.mensaje.setText('<font color="red">El usuario con el numero de documento '+self.persona.noId+' no existe</font>')
        
            
    def btnActualizarClicked(self):
        self.persona.noId = self.ui.noId.text()
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        self.persona = resultado
        fechaDesafiliacion = self.ui.fechaDesafiliacion.date()
        self.persona.fechaDesafiliacion = fechaDesafiliacion
        self.logicaPersona.desafiliarUsuario(self.persona)
        self.ui.mensaje.setText('El paciente ha sido desafiliado')
        self.ui.pushButton_2.setEnabled(False)
    
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()
     
class VacunarUsuarioWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(VacunarUsuarioWindow, self).__init__()
        self.ui = Ui_vacunarUsuario()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        self.ui.noId.textEdited.connect(self.BuscarUsuario)
        self.ui.pushButton.clicked.connect(self.btnVacunarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        self.ui.pushButton.setEnabled(False)
        
    def BuscarUsuario(self):
        self.persona.noId = self.ui.noId.text()
        if self.persona.noId != '':
            resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
            if resultado:
                self.persona = resultado
                if self.persona.vacunado == 'S':
                    self.ui.mensaje.setText('El paciente ya se encuentra vacunado')
                    self.ui.pushButton.setEnabled(False)
                else:
                    self.ui.mensaje.setText('')
                    self.ui.pushButton.setEnabled(True)
                if self.persona.fechaDesafiliacion:
                    self.ui.mensaje.setText('Este usuario es encuentra desafiliado')
                    self.ui.pushButton.setEnabled(False)
                else:
                    self.ui.mensaje.setText('')
                    self.ui.pushButton.setEnabled(True)
            else:
                self.ui.pushButton.setEnabled(False)
                self.ui.mensaje.setText('<font color="red">El usuario con el numero de documento '+self.persona.noId+' no existe</font>')
        
            
    def btnVacunarClicked(self):
        self.persona.noId = self.ui.noId.text()
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        self.persona = resultado
        self.persona.vacunado = 'S'
        self.logicaPersona.vacunarPacientes(self.persona)
        self.ui.mensaje.setText('El paciente ha sido vacunado')
        self.ui.pushButton.setEnabled(False)
    
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()
   

app = QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())