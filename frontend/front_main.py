import shutil
import webbrowser
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from user_interface.main import Ui_MainWindow  # importa nuestro archivo generado
from user_interface.propMainWindow import Ui_PropMainWindow  # importa nuestro archivo generado
from user_interface.crearUsuario import Ui_crearUsuario
from user_interface.consultarUsuario import Ui_consultarUsuario
from user_interface.desafiliarUsuario import Ui_desafiliarUsuario
from user_interface.vacunarUsuario import Ui_vacunarUsuario
from user_interface.crearLote import Ui_crearLote
from user_interface.consultaLoteIndividual import Ui_ConsultarLoteIndividual

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir
import sys
import os
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
        
        self.ui.actionCrearLote.triggered.connect(self.gotoCrearLote)
        self.ui.actionConsultaIndividualLote.triggered.connect(self.gotoConsultaIndLote)
        # self.ui.actionConsultaCompletaLote.triggered.connect(self.gotoConsultaComLote)
        
        # self.ui.actionCrearPlan.triggered.connect(self.gotoCrearPlan)
        # self.ui.actionConsultaIndividualPlan.triggered.connect(self.gotoConsultaIndPlan)
        # self.ui.actionConsultaCompletaPlan.triggered.connect(self.gotoConsultaComPlan)
        
        # self.ui.actionCrearProgramacion.triggered.connect(self.gotoCrearProgramacion)
        # self.ui.actionConsultaIndividualProgramacion.triggered.connect(self.gotoConsultaIndProgramacion)
        # self.ui.actionConsultaCompletaProgramacion.triggered.connect(self.gotoConsultaComProgramacion)
        
        self.ui.DocumentacionUsuario.clicked.connect(self.abrirDocumentacionUsuario)

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
    def gotoCrearLote(self):
        self.anotherWindow = CrearLoteWindow()
        self.anotherWindow.show()
        self.close()
    def gotoConsultaIndLote(self):
        self.anotherWindow = ConsultarLoteWindow()
        self.anotherWindow.show()
        self.close()
    def abrirDocumentacionUsuario(self):
        path = 'https://docs.google.com/document/d/1RsPZYYKPNPl37ZHKIk5YJEVjrR-C3OAtvPPaQx1nl3A/edit?usp=sharing'
        webbrowser.open_new(path)
       
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
        self.ui.pushButton_2.setEnabled(False)
    
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
   
class CrearLoteWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CrearLoteWindow, self).__init__()
        self.ui = Ui_crearLote()
        self.ui.setupUi(self)
        self.lote = model.Lote()
        self.logicaLote = logic.Lote()
        self.ruta = None
        self.ui.noLote.textEdited.connect(self.BuscarLote)
        self.ui.buscarImagen.clicked.connect(self.btnBuscarImagenClicked)
        self.ui.btnGuardar.clicked.connect(self.btnGuardarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
    def BuscarLote(self):
        self.lote.noLote = self.ui.noLote.text()
        if self.lote.noLote != '':
            resultado = self.logicaLote.consultarLote(self.lote.noLote)
            if not resultado:
                self.ui.fabricante.setEnabled(True)
                self.ui.tipoVacuna.setEnabled(True)
                self.ui.cantidadRecibida.setEnabled(True)
                self.ui.dosisNecesarias.setEnabled(True)
                self.ui.temperatura.setEnabled(True)
                self.ui.efectividad.setEnabled(True)
                self.ui.tiempoProteccion.setEnabled(True)
                self.ui.fechaVencimiento.setEnabled(True)
                self.ui.buscarImagen.setEnabled(True)
                self.ui.imagen.setEnabled(True)
                self.ui.btnGuardar.setEnabled(True)
                self.ui.mensaje.setText('')
            else:
                self.ui.fabricante.setEnabled(False)
                self.ui.tipoVacuna.setEnabled(False)
                self.ui.cantidadRecibida.setEnabled(False)
                self.ui.dosisNecesarias.setEnabled(False)
                self.ui.temperatura.setEnabled(False)
                self.ui.efectividad.setEnabled(False)
                self.ui.tiempoProteccion.setEnabled(False)
                self.ui.fechaVencimiento.setEnabled(False)
                self.ui.buscarImagen.setEnabled(False)
                self.ui.imagen.setEnabled(False)
                self.ui.btnGuardar.setEnabled(False)
                self.ui.mensaje.setText('<font color="red">El lote con el numero de lote '+self.lote.noLote+' ya existe</font>')
            
    def btnGuardarClicked(self):
        self.lote.noLote = self.ui.noLote.text()
        self.lote.fabricante = self.ui.fabricante.text()
        self.lote.tipoVacuna = self.ui.tipoVacuna.text()
        self.lote.cantidadRecibida = self.ui.cantidadRecibida.text()
        self.lote.cantidadAsignada = 0
        self.lote.cantidadUsada = 0
        self.lote.dosisNecesaria = self.ui.dosisNecesarias.text()
        self.lote.temperatura = self.ui.temperatura.text()
        self.lote.efectividad = self.ui.efectividad.text()
        self.lote.tiempoProteccion = self.ui.tiempoProteccion.text()
        fechaVencimiento = self.ui.fechaVencimiento.date()
        # self.lote.fechaVencimiento = fechaVencimiento
        with open(self.ruta, "rb") as File:
            self.lote.imagen = File.read()
        self.logicaLote.crearLote(self.lote)
        self.ui.mensaje.setText('El lote ha sido creado')
        self.ui.btnGuardar.setEnabled(False)
    
    def btnBuscarImagenClicked(self):
        self.ruta, _ = QFileDialog.getOpenFileName(self, 'Open File Image', r'./imagenes/', 'Image Files (*.jpg *jpeg *webp)')
        self.ui.imagen.setPixmap(QPixmap(self.ruta))
        self.ui.imagen.setScaledContents(True)
        
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()
     
class ConsultarLoteWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsultarLoteWindow, self).__init__()
        self.ui = Ui_ConsultarLoteIndividual()
        self.ui.setupUi(self)
        self.lote = model.Lote()
        self.logicaLote = logic.Lote()
        self.ui.btnBuscar.clicked.connect(self.btnBuscarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
        self.ui.fabricante.setText('')
        self.ui.tipoVacuna.setText('')
        self.ui.cantidadRecibida.setText('')
        self.ui.cantidadAsignada.setText('')
        self.ui.cantidadUsada.setText('')
        self.ui.dosis.setText('')
        self.ui.temperatura.setText('')
        self.ui.efectividad.setText('')
        self.ui.tiempoProteccion.setText('')
        self.ui.fechaVencimiento.setText('')
        self.ui.imagen.setText('')
        
    def btnBuscarClicked(self):
        self.lote = model.Lote()
        self.lote.noLote = self.ui.noLote.text()
        resultado = self.logicaLote.consultarLote(self.lote.noLote)
        if resultado:
            self.lote = resultado
            self.ui.fabricante.setText(str(self.lote.fabricante))
            self.ui.tipoVacuna.setText(str(self.lote.tipoVacuna))
            self.ui.cantidadRecibida.setText(str(self.lote.cantidadRecibida))
            self.ui.cantidadAsignada.setText(str(self.lote.cantidadAsignada))
            self.ui.cantidadUsada.setText(str(self.lote.cantidadUsada))
            self.ui.dosis.setText(str(self.lote.dosisNecesaria))
            self.ui.temperatura.setText(str(self.lote.temperatura))
            self.ui.efectividad.setText(str(self.lote.efectividad))
            self.ui.tiempoProteccion.setText(str(self.lote.tiempoProteccion))
            self.ui.fechaVencimiento.setText(str(self.lote.fechaVencimiento))
            directorio = "imagenesDescargadas/"
            try:
                os.stat(directorio)
            except FileNotFoundError:
                os.mkdir(directorio)
            rutaDeGuardado = '{}imagenVacuna.jpg'.format(directorio)
            with open(rutaDeGuardado, "wb") as File:
                File.write(self.lote.imagen)
            # Se abre la imagen abriendo su ruta almacenada en (rutaDeGuardado) con el método .open() y se visualiza con el método .show()
            self.ui.imagen.setPixmap(QPixmap(rutaDeGuardado))
            self.ui.imagen.setScaledContents(True)
            shutil.rmtree(directorio)
        else:
            self.ui.fabricante.setText('')
            self.ui.tipoVacuna.setText('')
            self.ui.cantidadRecibida.setText('')
            self.ui.cantidadAsignada.setText('')
            self.ui.cantidadUsada.setText('')
            self.ui.dosis.setText('')
            self.ui.temperatura.setText('')
            self.ui.efectividad.setText('')
            self.ui.tiempoProteccion.setText('')
            self.ui.fechaVencimiento.setText('')
            self.ui.imagen.setText('')
            self.ui.mensaje.setText('<font color="red">El usuario con el numero de documento '+self.persona.noId+' no existe</font>')
    
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()


app = QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
