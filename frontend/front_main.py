from datetime import datetime
import shutil
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QApplication, QFileDialog
'''============== Ventana principal=============='''
from user_interface.main import Ui_MainWindow  # importa nuestro archivo generado
from user_interface.propMainWindow import Ui_PropMainWindow  # importa nuestro archivo generado
'''============== Ventanas usuario=============='''
from user_interface.crearUsuario import Ui_crearUsuario
from user_interface.consultarUsuario import Ui_consultarUsuario
from user_interface.desafiliarUsuario import Ui_desafiliarUsuario
from user_interface.vacunarUsuario import Ui_vacunarUsuario
'''============== Ventanas lote=============='''
from user_interface.crearLote import Ui_crearLote
from user_interface.consultaLoteIndividual import Ui_ConsultarLoteIndividual
'''============== Ventanas plan=============='''
from user_interface.crearPlanVacunacion import Ui_CrearPlanVacunacion
from user_interface.consultaPlanVacunacionIndividual import Ui_MainWindow as Ui_ConsultarPlanIndividual
from user_interface.consultaTodoPlan import Ui_ConsultarTodoPlan
'''============== Ventanas programacion=============='''
from user_interface.crearProgramacionVacunacion import Ui_CrearProgramacionVacunacion
from user_interface.consultaProgramacionVacuna import Ui_ConsultaProgramacion

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDate, QDateTime
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
        self.ui.actionConsultaCompletaLote.triggered.connect(self.gotoConsultaComLote)
        
        self.ui.actionCrearPlan.triggered.connect(self.gotoCrearPlan)
        self.ui.actionConsultaIndividualPlan.triggered.connect(self.gotoConsultaIndPlan)
        self.ui.actionConsultaCompletaPlan.triggered.connect(self.gotoConsultaComPlan)
        
        self.ui.actionCrearProgramacion.triggered.connect(self.gotoCrearProgramacion)
        self.ui.actionConsultaIndividualProgramacion.triggered.connect(self.gotoConsultaIndProgramacion)
        self.ui.actionConsultaCompletaProgramacion.triggered.connect(self.gotoConsultaComProgramacion)
        
        self.ui.DocumentacionUsuario.clicked.connect(self.gotoDocumentacion)

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
    def gotoConsultaComLote(self):
        # self.anotherWindow = ConsultarLoteWindow()
        # self.anotherWindow.show()
        # self.close()
        pass

    def gotoCrearPlan(self):
        self.anotherWindow = CrearPlanWindow()
        self.anotherWindow.show()
        self.close()
    def gotoConsultaIndPlan(self):
        self.anotherWindow = ConsultarPlanWindow()
        self.anotherWindow.show()
        self.close()
    def gotoConsultaComPlan(self):
        self.anotherWindow = ConsultarPlanesWindow()
        self.anotherWindow.show()
        self.close()

    def gotoCrearProgramacion(self):
        self.anotherWindow = CrearVacunacionWindow()
        self.anotherWindow.show()
        self.close()
    def gotoConsultaIndProgramacion(self):
        self.anotherWindow = ConsultarVacunacionWindow()
        self.anotherWindow.show()
        self.close()
    def gotoConsultaComProgramacion(self):
        self.anotherWindow = ConsultarLoteWindow()
        self.anotherWindow.show()
        self.close()
        
    def gotoDocumentacion(self):
        logic.documentacionUsuario()
        
'''============Modulo de usuarios============'''
   
class CrearUsuarioWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CrearUsuarioWindow, self).__init__()
        self.ui = Ui_crearUsuario()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        self.ui.noId.textEdited.connect(self.BuscarUsuario)
        self.ui.fechaNacimiento.dateChanged.connect(self.verificarFechas)
        self.ui.fechaAfiliacion.dateChanged.connect(self.verificarFechas)
        self.ui.pushButton_2.clicked.connect(self.btnGuardarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
    def verificarFechas(self):
        fechaNacimientoDt = self.ui.fechaNacimiento.dateTime().toPyDateTime()
        fechaAfiliacionDt = self.ui.fechaAfiliacion.dateTime().toPyDateTime()
        fechaActual = datetime.now()
        if (fechaActual > fechaAfiliacionDt > fechaNacimientoDt):
            self.ui.pushButton_2.setEnabled(True)
        else:
            self.ui.pushButton_2.setEnabled(False)
    
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
        fechaNacimientoDt = self.ui.fechaNacimiento.dateTime().toPyDateTime()
        fechaAfiliacionDt = self.ui.fechaAfiliacion.dateTime().toPyDateTime()
        self.persona.fechaNacimiento = fechaNacimientoDt.strftime("%Y-%m-%d")
        self.persona.fechaAfiliacion = fechaAfiliacionDt.strftime("%Y-%m-%d")
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
        self.ui.fechaDesafiliacion.dateChanged.connect(self.verificarFechas)
        self.ui.pushButton_2.clicked.connect(self.btnActualizarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.fechaDesafiliacion.setEnabled(False)
        
    def verificarFechas(self):
        fechaDesafiliacionDt = self.ui.fechaDesafiliacion.dateTime().toPyDateTime()
        fechaAfiliacionDt = datetime.strptime(self.ui.fechaAfiliacion.text(), "%Y-%m-%d")
        fechaActual = datetime.now()
        if (fechaActual > fechaDesafiliacionDt > fechaAfiliacionDt):
            self.ui.pushButton_2.setEnabled(True)
        else:
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
                    self.ui.fechaDesafiliacion.setEnabled(False)
                    self.ui.pushButton_2.setEnabled(False)
                else:
                    self.ui.fechaDesafiliacion.setEnabled(True)
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
                self.ui.fechaDesafiliacion.setEnabled(False)
                self.ui.pushButton_2.setEnabled(False)
                self.ui.mensaje.setText('<font color="red">El usuario con el numero de documento '+self.persona.noId+' no existe</font>')
        
    def btnActualizarClicked(self):
        self.persona.noId = self.ui.noId.text()
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        self.persona = resultado
        fechaDesafiliacionDt = self.ui.fechaDesafiliacion.dateTime().toPyDateTime()
        self.persona.fechaDesafiliacion = fechaDesafiliacionDt.strftime("%Y-%m-%d")
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

'''============Modulo de lotes============'''
   
class CrearLoteWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CrearLoteWindow, self).__init__()
        self.ui = Ui_crearLote()
        self.ui.setupUi(self)
        self.lote = model.Lote()
        self.logicaLote = logic.Lote()
        self.ruta = None
        self.ui.noLote.textEdited.connect(self.BuscarLote)
        self.ui.fechaVencimiento.dateChanged.connect(self.verificarFechas)
        self.ui.buscarImagen.clicked.connect(self.btnBuscarImagenClicked)
        self.ui.btnGuardar.clicked.connect(self.btnGuardarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        self.ui.btnGuardar.setEnabled(False)
        
    def verificarFechas(self):
        fechaVencimientoDt = self.ui.fechaVencimiento.dateTime().toPyDateTime()
        fechaActual = datetime.now()
        if fechaVencimientoDt > fechaActual:
            self.ui.btnGuardar.setEnabled(True)
        else:
            self.ui.btnGuardar.setEnabled(False)

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
        fechaVencimientoDt = self.ui.fechaVencimiento.dateTime().toPyDateTime()
        self.lote.fechaVencimiento = fechaVencimientoDt.strftime("%Y-%m-%d")
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
            self.ui.mensaje.setText('')
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
            self.ui.mensaje.setText('<font color="red">El lote con el numero de lote '+self.lote.noLote+' no existe</font>')
    
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

class ConsultarLotesWindow(QtWidgets.QMainWindow):
    pass

'''============Modulo de plan============'''

class CrearPlanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CrearPlanWindow, self).__init__()
        self.ui = Ui_CrearPlanVacunacion()
        self.ui.setupUi(self)
        self.plan = model.PlanDeVacunacion()
        self.logicaPlan = logic.PlanDeVacunacion()
        self.ui.idPlan.textEdited.connect(self.BuscarPlan)
        self.ui.edadMinima.textEdited.connect(self.verificarEdades)
        self.ui.edadMaxima.textEdited.connect(self.verificarEdades)
        self.ui.fechaInicio.dateChanged.connect(self.verificarFechas)
        self.ui.fechaFinal.dateChanged.connect(self.verificarFechas)
        self.ui.btnGuardar.clicked.connect(self.btnGuardarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
    def verificarEdades(self):
        if self.ui.edadMaxima.text() != '' and self.ui.edadMinima.text() != '':
            retornoEdadMinima = self.logicaPlan.verificarEdad(int(self.ui.edadMinima.text()))
            retornoEdadMaxima = self.logicaPlan.verificarEdad(int(self.ui.edadMaxima.text()))
            if retornoEdadMinima[0] and retornoEdadMaxima[0]: 
                self.ui.mensaje.setText('')
                self.ui.btnGuardar.setEnabled(True)
            else: 
                self.ui.mensaje.setText(retornoEdadMaxima[1])
                self.ui.btnGuardar.setEnabled(False)
        
    def verificarFechas(self):
        fechaInicioDt = self.ui.fechaInicio.dateTime().toPyDateTime()
        fechaFinalDt = self.ui.fechaFinal.dateTime().toPyDateTime()
        fechaActual = datetime.now()
        if (fechaFinalDt >= fechaInicioDt > fechaActual):
            self.ui.btnGuardar.setEnabled(True)
        else:
            self.ui.btnGuardar.setEnabled(False)
    
    def BuscarPlan(self):
        self.plan.idPlan = self.ui.idPlan.text()
        if self.plan.idPlan != '':
            resultado = self.logicaPlan.consultarPlanVacunacion(self.plan.idPlan)
            if not resultado:
                self.ui.edadMinima.setEnabled(True)
                self.ui.edadMaxima.setEnabled(True)
                self.ui.fechaInicio.setEnabled(True)
                self.ui.fechaFinal.setEnabled(True)
                self.ui.mensaje.setText('')
            else:
                self.ui.edadMinima.setEnabled(False)
                self.ui.edadMaxima.setEnabled(False)
                self.ui.fechaInicio.setEnabled(False)
                self.ui.fechaFinal.setEnabled(False)
                self.ui.btnGuardar.setEnabled(False)
                self.ui.mensaje.setText('<font color="red">El plan con el numero de plan '+self.plan.idPlan+' ya existe</font>')
            
    def btnGuardarClicked(self):
        self.plan.idPlan = self.ui.idPlan.text()
        self.plan.edadMinima = self.ui.edadMinima.text()
        self.plan.edadMaxima = self.ui.edadMaxima.text()
        fechaInicioDt = self.ui.fechaInicio.dateTime().toPyDateTime()
        self.plan.fechaInicio = fechaInicioDt.strftime("%Y-%m-%d")
        fechaFinalDt = self.ui.fechaFinal.dateTime().toPyDateTime()
        self.plan.fechaFinal = fechaFinalDt.strftime("%Y-%m-%d")
        self.logicaPlan.crearPlanVacunacion(self.plan)
        self.ui.mensaje.setText('El plan ha sido creado')
        self.ui.btnGuardar.setEnabled(False)
        
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()
     
class ConsultarPlanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsultarPlanWindow, self).__init__()
        self.ui = Ui_ConsultarPlanIndividual()
        self.ui.setupUi(self)
        self.plan = model.PlanDeVacunacion()
        self.logicaPlan = logic.PlanDeVacunacion()
        self.ui.btnBuscar.clicked.connect(self.btnBuscarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
        self.ui.edadMinima.setText('')
        self.ui.edadMaxima.setText('')
        self.ui.fechaInicio.setText('')
        self.ui.fechaFinal.setText('')
        
    def btnBuscarClicked(self):
        self.plan = model.PlanDeVacunacion()
        self.plan.idPlan = self.ui.idPlan.text()
        resultado = self.logicaPlan.consultarPlanVacunacion(self.plan.idPlan)
        if resultado:
            self.plan = resultado
            self.ui.edadMinima.setText(str(self.plan.edadMinima))
            self.ui.edadMaxima.setText(str(self.plan.edadMaxima))
            self.ui.fechaInicio.setText(str(self.plan.fechaInicio))
            self.ui.fechaFinal.setText(str(self.plan.fechaFinal))
            self.ui.mensaje.setText('')
        else:
            self.ui.edadMinima.setText('')
            self.ui.edadMaxima.setText('')
            self.ui.fechaInicio.setText('')
            self.ui.fechaFinal.setText('')
            self.ui.mensaje.setText('<font color="red">El plan con el numero de plan '+self.plan.idPlan+' no existe</font>')
    
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

class ConsultarPlanesWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsultarPlanesWindow, self).__init__()
        self.ui = Ui_ConsultarTodoPlan()
        self.ui.setupUi(self)
        self.plan = model.PlanDeVacunacion()
        self.logicaPlan = logic.PlanDeVacunacion()
        self.ui.btnBuscar.clicked.connect(self.btnCargarDataClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
    
    def btnCargarDataClicked(self):
        resultados = self.logicaPlan.consultarPlanesVacunacion()
        data = []
        if resultados:
            for plan in resultados:
                data.append((str(plan.idPlan), str(plan.edadMinima), str(plan.edadMaxima), plan.fechaInicio, plan.fechaFinal))
        self.ui.tableWidget.setRowCount(len(resultados)) 
        row=0
        for tup in data:
            col=0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled) #make it not editable
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1

    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

'''============Modulo de programacion============'''

class CrearVacunacionWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CrearVacunacionWindow, self).__init__()
        self.ui = Ui_CrearProgramacionVacunacion()
        self.ui.setupUi(self)
        self.programacion = model.ProgramacionDeVacunas()
        self.logicaProgramacion = logic.ProgramacionDeVacunas()
        self.fechaInicioIngresada = None
        self.ui.fechaInicio.dateChanged.connect(self.verificarFechas)
        self.ui.btnCrear.clicked.connect(self.btnCrearClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
    def verificarFechas(self):
        fechaInicioIngresadaDt = self.ui.fechaInicio.dateTime().toPyDateTime()
        fechaActual = datetime.now()
        if (fechaInicioIngresadaDt > fechaActual):
            self.ui.btnCrear.setEnabled(True)
        else:
            self.ui.btnCrear.setEnabled(False)
            
    def btnCrearClicked(self):
        fechaIngresadaDt = self.ui.fechaInicio.dateTime().toPyDateTime()
        retorno = self.logicaProgramacion.crearProgramacion(fechaIngresadaDt)
        self.ui.mensaje.setText('La programacion de vacunacion ha sido creado')
        self.ui.btnCrear.setEnabled(False)
        
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()
     
class ConsultarVacunacionWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsultarVacunacionWindow, self).__init__()
        self.ui = Ui_ConsultaProgramacion()
        self.ui.setupUi(self)
        self.programacion = model.ProgramacionDeVacunas()
        self.logicaProgramacion = logic.ProgramacionDeVacunas()
        self.ui.btnBuscar.clicked.connect(self.btnBuscarClicked)
        self.ui.btnConsultaCompleta.clicked.connect(self.btnConsultaClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
        self.ui.tableWidget.setRowCount(0)
        
    def btnBuscarClicked(self):
        self.programacion = model.ProgramacionDeVacunas()
        self.programacion.noId = self.ui.noId.text()
        resultado = self.logicaProgramacion.consultarProgramacionIndividual(self.programacion.noId)
        if resultado:
            persona = resultado[0]
            programacion = resultado[1]
            lote = resultado[2]
            data = ((str(persona.noId), str(persona.nombre), str(persona.apellido), str(persona.direccion), str(persona.telefono), str(persona.correo), str(programacion.fechaProgramada), str(programacion.horaProgramada), str(lote.noLote), str(lote.fabricante)))
            self.ui.tableWidget.setRowCount(1)
            col = 0
            for item in data:
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled) #make it not editable
                self.ui.tableWidget.setItem(0, col, cellinfo)
                col += 1
                
            self.ui.mensaje.setText('')
        else:
            self.ui.mensaje.setText('<font color="red">La cita del paciente con el numero de identificacion '+self.programacion.noId+' no existe</font>')
    
    def btnConsultaClicked(self):
        opcionConsulta = self.ui.campoConsulta.currentText()
        if opcionConsulta == 'Número de Identificación': datoConsulta = 0
        elif opcionConsulta == 'Nombre': datoConsulta = 1
        elif opcionConsulta == 'Apellido': datoConsulta = 2
        elif opcionConsulta == 'Dirección': datoConsulta = 3
        elif opcionConsulta == 'Teléfono': datoConsulta = 4
        elif opcionConsulta == 'Correo': datoConsulta = 5
        elif opcionConsulta == 'Fecha Programada': datoConsulta = 6
        elif opcionConsulta == 'Hora Programada': datoConsulta = 7
        elif opcionConsulta == 'Número de lote': datoConsulta = 8
        elif opcionConsulta == 'Fabricante': datoConsulta = 9
        resultados = self.logicaProgramacion.consultarProgramacionCompleta(datoConsulta)
        data = []
        if resultados:
            for plan in resultados:
                persona = plan[0]
                programacion = plan[1]
                lote = plan[2]
                tup = (str(persona.noId), str(persona.nombre), str(persona.apellido), str(persona.direccion), str(persona.telefono), str(persona.correo), str(programacion.fechaProgramada), str(programacion.horaProgramada), str(lote.noLote), str(lote.fabricante))
                data.append(tup)
        self.ui.tableWidget.setRowCount(len(resultados)) 
        row=0
        for tup in data:
            col=0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled) #make it not editable
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1
        self.ui.mensaje.setText('')
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

logic.crearTablas()

app = QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())