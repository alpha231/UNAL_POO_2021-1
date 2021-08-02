# Se importan las librerias, clases y metodos necesarios para el programa
# Librería datetime esta incluida por defecto, permite la correcta elaboración para formatos de fecha
from datetime import datetime 
# Librería shutil esta incluida por defecto, permite la operación de archivos
import shutil
# Librería PyQt5 requerida para la creación de la interfaz grafica de este programa
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QFileDialog
# Se importan archivos generados con la app QtDesigner y almacenados en user_interface
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
from user_interface.consultaTodoLote import Ui_ConsultarTodoLote
'''============== Ventanas plan=============='''
from user_interface.crearPlanVacunacion import Ui_CrearPlanVacunacion
from user_interface.consultaPlanVacunacionIndividual import Ui_MainWindow as Ui_ConsultarPlanIndividual
from user_interface.consultaTodoPlan import Ui_ConsultarTodoPlan
'''============== Ventanas programacion=============='''
from user_interface.crearProgramacionVacunacion import Ui_CrearProgramacionVacunacion
from user_interface.consultaProgramacionVacuna import Ui_ConsultaProgramacion

# se importa QtPixmap para utilizar imagenes en la interfaz
from PyQt5.QtGui import QPixmap
import sys
# se usa os para operar archivos 
import os
# se da una ruta del programa de donde importar
sys.path.append('backend_POO')
# se importan logic.py, model.py, requeridos para el programa
import model
import logic

# Se crea una clase identificada como MainWindow, relacionada a los valores y funciones propias de la pantalla principal
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_PropMainWindow()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        # funciones para pantallas del modulo usuario
        self.ui.actionCrearUsuario.triggered.connect(self.gotoCrearUsuario)
        self.ui.actionConsultarUsuario.triggered.connect(self.gotoConsultarUsuario)
        self.ui.actionDesafiliarUsuario.triggered.connect(self.gotoDesafiliarUsuario)
        self.ui.actionVacunarUsuario.triggered.connect(self.gotoVacunarUsuario)
        
        # funciones para pantallas del modulo lotes
        self.ui.actionCrearLote.triggered.connect(self.gotoCrearLote)
        self.ui.actionConsultaIndividualLote.triggered.connect(self.gotoConsultaIndLote)
        self.ui.actionConsultaCompletaLote.triggered.connect(self.gotoConsultaComLote)
        
        # funciones para pantallas del modulo planes de vacunación
        self.ui.actionCrearPlan.triggered.connect(self.gotoCrearPlan)
        self.ui.actionConsultaIndividualPlan.triggered.connect(self.gotoConsultaIndPlan)
        self.ui.actionConsultaCompletaPlan.triggered.connect(self.gotoConsultaComPlan)
        
        # funciones para pantallas del modulo programación de vacunación
        self.ui.actionCrearProgramacion.triggered.connect(self.gotoCrearProgramacion)
        self.ui.actionConsultarProgramacion.triggered.connect(self.gotoConsultaProgramacion)
        
        # funcion para el boton ayuda para usuarios
        self.ui.DocumentacionUsuario.clicked.connect(self.gotoDocumentacion)

    # se crea la función para ir a la pantalla CrearUsuarioWindow
    def gotoCrearUsuario(self):
        self.anotherWindow = CrearUsuarioWindow()
        self.anotherWindow.show()
        self.close()
    # se crea la función para ir a la pantalla ConsultarUsuarioWindow
    def gotoConsultarUsuario(self):
        self.anotherWindow = ConsultarUsuarioWindow()
        self.anotherWindow.show()
        self.close()
    # se crea la función para ir a la pantalla DesafiliarUsuarioWindow
    def gotoDesafiliarUsuario(self):
        self.anotherWindow = DesafiliarUsuarioWindow()
        self.anotherWindow.show()
        self.close()
    # se crea la función para ir a la pantalla VacunarUsuarioWindow
    def gotoVacunarUsuario(self):
        self.anotherWindow = VacunarUsuarioWindow()
        self.anotherWindow.show()
        self.close()
    
    # se crea la función para ir a la pantalla CrearLoteWindow
    def gotoCrearLote(self):
        self.anotherWindow = CrearLoteWindow()
        self.anotherWindow.show()
        self.close()
    # se crea la función para ir a la pantalla ConsultarLoteWindow
    def gotoConsultaIndLote(self):
        self.anotherWindow = ConsultarLoteWindow()
        self.anotherWindow.show()
        self.close()
    # se crea la función para ir a la pantalla ConsultarLotesWindow
    def gotoConsultaComLote(self):
        self.anotherWindow = ConsultarLotesWindow()
        self.anotherWindow.show()
        self.close()
        pass

    # se crea la función para ir a la pantalla CrearPlanWindow
    def gotoCrearPlan(self):
        self.anotherWindow = CrearPlanWindow()
        self.anotherWindow.show()
        self.close()
    # se crea la función para ir a la pantalla ConsultarPlanWindow
    def gotoConsultaIndPlan(self):
        self.anotherWindow = ConsultarPlanWindow()
        self.anotherWindow.show()
        self.close()
    # se crea la función para ir a la pantalla ConsultarPlanesWindow
    def gotoConsultaComPlan(self):
        self.anotherWindow = ConsultarPlanesWindow()
        self.anotherWindow.show()
        self.close()

    # se crea la función para ir a la pantalla CrearVacunacionWindow
    def gotoCrearProgramacion(self):
        self.anotherWindow = CrearVacunacionWindow()
        self.anotherWindow.show()
        self.close()
    # se crea la función para ir a la pantalla ConsultarVacunacionWindow
    def gotoConsultaProgramacion(self):
        self.anotherWindow = ConsultarVacunacionWindow()
        self.anotherWindow.show()
        self.close()

    # función para abrir el navegagor y abrir la documentación de usuario
    def gotoDocumentacion(self):
        logic.documentacionUsuario()
        
'''============Modulo de usuarios============'''

# Se crea una clase identificada como CrearUsuarioWindow, relacionada a la pantalla para crear afiliados
class CrearUsuarioWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CrearUsuarioWindow, self).__init__()
        self.ui = Ui_crearUsuario()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        self.ui.noId.textEdited.connect(self.BuscarUsuario)
        self.ui.fechaNacimiento.dateChanged.connect(self.verificarFechas)
        self.ui.fechaAfiliacion.dateChanged.connect(self.verificarFechas)
        self.ui.pushButton_2.clicked.connect(self.btnGuardarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
     
    # función para validar fechas recividas
    def verificarFechas(self):
        # se transforman los datos obtenidos a forma de fecha con el metodo dateTime().toPyDateTime()
        fechaNacimientoDt = self.ui.fechaNacimiento.dateTime().toPyDateTime()
        fechaAfiliacionDt = self.ui.fechaAfiliacion.dateTime().toPyDateTime()
        # se toma la fecha actual por el metodo datetime.now() y se almacena en (fechaActual)
        fechaActual = datetime.now()
        # si las fechas son validadas, se habilitará el botón para guardar
        if (fechaActual > fechaAfiliacionDt > fechaNacimientoDt):
            self.ui.pushButton_2.setEnabled(True)
        # de otra manera se inhabilitará
        else:
            self.ui.pushButton_2.setEnabled(False)
    
    # función para buscar un usuario registrado con un numero de identificación
    def BuscarUsuario(self):
        self.persona.noId = self.ui.noId.text()
        # si la información almacenada en (self.persona.noId) No esta vacía, se consultará y almacenará en la variable (resultado)
        if self.persona.noId != '':
            resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
            # si la variable (resultado) no esta vacia, se habilita el botón de guardado
            if not resultado:
                self.ui.splitter_3.setEnabled(True)
                self.ui.pushButton_2.setEnabled(True)
                # se vacia el mensaje de eventos
                self.ui.mensaje.setText('')
            # de otra forma se inhabilita el botón de guardado y aparece un mensaje
            else:
                self.ui.splitter_3.setEnabled(False)
                self.ui.pushButton_2.setEnabled(False)
                self.ui.mensaje.setText('<font color="red">El usuario con el numero de documento '+self.persona.noId+' ya existe</font>')
     
    # se crea la función para guardar información registrada al oprimir un boton
    def btnGuardarClicked(self):
        # Se guarda cada dato dentro de la clase model.Persona()
        self.persona.noId = self.ui.noId.text()
        self.persona.noId = self.ui.noId.text()
        self.persona.nombre = self.ui.nombre.text()
        self.persona.apellido = self.ui.apellido.text()
        self.persona.direccion = self.ui.direccion.text()
        self.persona.telefono = self.ui.telefono.text()
        self.persona.correo = self.ui.correo.text()
        self.persona.ciudad = self.ui.ciudad.text()
        # se transforman valores de fechas por el metodo strftime() y se almacenan
        fechaNacimientoDt = self.ui.fechaNacimiento.dateTime().toPyDateTime()
        fechaAfiliacionDt = self.ui.fechaAfiliacion.dateTime().toPyDateTime()
        self.persona.fechaNacimiento = fechaNacimientoDt.strftime("%Y-%m-%d")
        self.persona.fechaAfiliacion = fechaAfiliacionDt.strftime("%Y-%m-%d")
        self.persona.vacunado = 'N'
        self.persona.fechaDesafiliacion = None
        # se guarda la información de model.Persona() en la base de datos
        self.logicaPersona.crearUsuario(self.persona)
        # se genera un mensaje
        self.ui.mensaje.setText('El paciente ha sido creado')
        # se inhabilita el boton de guardado
        self.ui.pushButton_2.setEnabled(False)
    
    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

# Se crea una clase identificada como ConsultarUsuarioWindow, relacionada a la pantalla para consultar afiliados
class ConsultarUsuarioWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsultarUsuarioWindow, self).__init__()
        self.ui = Ui_consultarUsuario()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        self.ui.pushButton.clicked.connect(self.btnBuscarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
        # se inician los label para mostrar información vacíos
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
      
    # función para buscar un usuario al recivir un documento de identidad
    def btnBuscarClicked(self):
        self.persona = model.Persona()
        # se busca un documento de un usuario que coincida con lo recivido y su informacion se almacena en (resultado)
        self.persona.noId = self.ui.noId.text()
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        # si (resultado) No esta vacio, llena los labels con la información del usuario 
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
            # si el usuario esta marcado con "S" en su campo de estado de vacunación, el label se llenará con un "Si"
            if self.persona.vacunado == 'S':
                self.ui.vacunado.setText('Si')
            # de otra manera se marcara con "No"
            else:
                self.ui.vacunado.setText('No')
            # si el usuario cuenta con una fecha de desafiliación, esta se mostrará
            if self.persona.fechaDesafiliacion:
                self.ui.fechaDesafiliacion.setText(self.persona.fechaDesafiliacion)
            # de otra forma aparecera el mensaje 'La persona continua afiliada'
            else:
                self.ui.fechaDesafiliacion.setText('La persona continua afiliada')
            # se vacia el mensaje de eventos al usuario
            self.ui.mensaje.setText('')
        # si (resultado) esta vacio, los campos de información se vaciarán y generara un mensaje 
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
            # aparece un mensaje para el usuario
            self.ui.mensaje.setText('<font color="red">El usuario con el numero de documento '+self.persona.noId+' no existe</font>')
    
    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

# Se crea una clase identificada como DesafiliarUsuarioWindow, relacionada a la pantalla para desafiliar afiliados
class DesafiliarUsuarioWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(DesafiliarUsuarioWindow, self).__init__()
        self.ui = Ui_desafiliarUsuario()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        self.ui.noId.textEdited.connect(self.BuscarUsuario)
        self.ui.fechaDesafiliacion.dateChanged.connect(self.verificarFechas)
        self.ui.pushButton_2.clicked.connect(self.btnActualizarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.fechaDesafiliacion.setEnabled(False)
     
    # función para validar un fecha recivida
    def verificarFechas(self):
        # se toman valores dados en formato de fechas con el metodo .dateTime().toPyDateTime()
        fechaDesafiliacionDt = self.ui.fechaDesafiliacion.dateTime().toPyDateTime()
        fechaAfiliacionDt = datetime.strptime(self.ui.fechaAfiliacion.text(), "%Y-%m-%d")
        # se almacena la fecha actual con el metodo datetime.now()
        fechaActual = datetime.now()
        # si se validan las fechas recividas, se habilita el botón de guardado
        if (fechaActual > fechaDesafiliacionDt > fechaAfiliacionDt):
            self.ui.pushButton_2.setEnabled(True)
        # de otra manera se mantiene inhabilitado
        else:
            self.ui.pushButton_2.setEnabled(False)

    # función para buscar un usuario según un documento de identidad
    def BuscarUsuario(self):
        # se almacena el número de documento en (self.persona.noId)
        self.persona.noId = self.ui.noId.text()
        #si (self.persona.noId) No esta vacío, se consultara y se almacenara lo recivido en la variable (resultado)
        if self.persona.noId != '':
            resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
            # si (resultado) esta vacío, se mustrá su información y se dan cambios
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
                # si el usuario esta marcado con "S" en su campo de estado de vacunación, el label se llenará con un "Si"
                if self.persona.vacunado == 'S':
                    self.ui.vacunado.setText('Si')
                # de otra manera se marcara con "No"
                else:
                    self.ui.vacunado.setText('No')
                # si el usuario cuenta con una fecha de desafiliación, se mostrará un mensaje y se inhabilitará el botón actualizar
                if self.persona.fechaDesafiliacion:
                    self.ui.mensaje.setText('Este usuario ya es encuentra desafiliado')
                    self.ui.fechaDesafiliacion.setEnabled(False)
                    self.ui.pushButton_2.setEnabled(False)
                # de otra forma se habilitará la fecha y el botón actualizar
                else:
                    self.ui.fechaDesafiliacion.setEnabled(True)
                    self.ui.pushButton_2.setEnabled(True)
                    # se vacia el campo de mensaje
                    self.ui.mensaje.setText('')
            # si (resultado) NO esta vacío, se vacian los campos de información y se muestra un mensaje
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
                # se generá mensaje de evento para el usuario
                self.ui.mensaje.setText('<font color="red">El usuario con el numero de documento '+self.persona.noId+' no existe</font>')
        
    # función para actualizar información de desafiliación de usuario
    def btnActualizarClicked(self):
        self.persona.noId = self.ui.noId.text()
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        self.persona = resultado
        fechaDesafiliacionDt = self.ui.fechaDesafiliacion.dateTime().toPyDateTime()
        self.persona.fechaDesafiliacion = fechaDesafiliacionDt.strftime("%Y-%m-%d")
        self.logicaPersona.desafiliarUsuario(self.persona)
        self.ui.mensaje.setText('El paciente ha sido desafiliado')
        self.ui.pushButton_2.setEnabled(False)
    
    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

# Se crea una clase identificada como VacunarUsuarioWindow, relacionada a la pantalla para vacunar afiliados     
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
     
    # función para buscar un usuario dado un número de documento
    def BuscarUsuario(self):
        self.persona.noId = self.ui.noId.text()
        # si (self.persona.noId) No esta vacío, se consultara y se almacenara lo recivido en la variable (resultado)
        if self.persona.noId != '':
            resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
            # si (resultado) esta vacío, se mustrá su información y se dan cambios
            if resultado:
                self.persona = resultado
                # si el usuario cuenta con un estado de vacunación "S", se inhabilita el botón vacunar y aparece un mensaje
                if self.persona.vacunado == 'S':
                    self.ui.mensaje.setText('El paciente ya se encuentra vacunado')
                    self.ui.pushButton.setEnabled(False)
                else:
                    self.ui.mensaje.setText('')
                    self.ui.pushButton.setEnabled(True)
                    # si el usuario cuenta con una fecha de desafiliación, se inhabilita el botón vacunar y aparece un mensaje
                    if self.persona.fechaDesafiliacion:
                        self.ui.mensaje.setText('Este usuario es encuentra desafiliado')
                        self.ui.pushButton.setEnabled(False)
                    # de otra forma se guarda la información
                    else:
                        self.ui.mensaje.setText('')
                        self.ui.pushButton.setEnabled(True)
            # de otra forma se inhabilita el botón vacunar y aparece un mensaje
            else:
                self.ui.pushButton.setEnabled(False)
                self.ui.mensaje.setText('<font color="red">El usuario con el numero de documento '+self.persona.noId+' no existe</font>')
        
    # función para vacunar un usuario   
    def btnVacunarClicked(self):
        self.persona.noId = self.ui.noId.text()
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        self.persona = resultado
        self.persona.vacunado = 'S'
        self.logicaPersona.vacunarPacientes(self.persona)
        self.ui.mensaje.setText('El paciente ha sido vacunado')
        self.ui.pushButton.setEnabled(False)
    
    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

'''============Modulo de lotes============'''

# Se crea una clase identificada como CrearLoteWindow, relacionada a la pantalla para crear lotes de vacunas        
class CrearLoteWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CrearLoteWindow, self).__init__()
        self.ui = Ui_crearLote()
        self.ui.setupUi(self)
        self.lote = model.Lote()
        self.logicaLote = logic.Lote()
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        self.ruta = None
        self.ui.noLote.textEdited.connect(self.BuscarLote)
        self.ui.fechaVencimiento.dateChanged.connect(self.verificarFechas)
        self.ui.buscarImagen.clicked.connect(self.btnBuscarImagenClicked)
        self.ui.btnGuardar.clicked.connect(self.btnGuardarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        self.ui.btnGuardar.setEnabled(False)

    # función para validar fechas obtenidas
    def verificarFechas(self):
        # se toman valores dados en formato de fechas con el metodo .dateTime().toPyDateTime()
        fechaVencimientoDt = self.ui.fechaVencimiento.dateTime().toPyDateTime()
        # se toma la fecha actual con el metodo datetime.now() y se almacena en (fechaActual)
        fechaActual = datetime.now()
        # si la fecha el validada, habilita el botón guardar
        if fechaVencimientoDt > fechaActual:
            self.ui.btnGuardar.setEnabled(True)
        # de otraforma se inhabilita el botón guardar
        else:
            self.ui.btnGuardar.setEnabled(False)

    # función para buscar un lote según un código dado
    def BuscarLote(self):
        self.lote.noLote = self.ui.noLote.text()
        # si (self.lote.noLote) no esta vacio, se consulta y almacena en (resultado)
        if self.lote.noLote != '':
            resultado = self.logicaLote.consultarLote(self.lote.noLote)
            # si (resultado) esta vacío, se mustrá su información y se dan cambios
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
            # si (resultado) NO esta vacío, se vacian los campos de información y se muestra un mensaje
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
      
    # se crea la función para guardar información registrada al oprimir un boton
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
         # se toman valores dados en formato de fechas con el metodo .dateTime().toPyDateTime()
        fechaVencimientoDt = self.ui.fechaVencimiento.dateTime().toPyDateTime()
        self.lote.fechaVencimiento = fechaVencimientoDt.strftime("%Y-%m-%d")
        # se abre un archivo para almacenar la imagen de la bacuna con el metodo read() y muestra un mensaje
        with open(self.ruta, "rb") as File:
            self.lote.imagen = File.read()
        self.logicaLote.crearLote(self.lote)
        self.ui.mensaje.setText('El lote ha sido creado')
        self.ui.btnGuardar.setEnabled(False)
    
    # función para generar imagen desde el camino administrado
    def btnBuscarImagenClicked(self):
        # se crea la ruta con el metodo QFileDialog.getOpenFileName()
        self.ruta, _ = QFileDialog.getOpenFileName(self, 'Open File Image', r'./imagenes/', 'Image Files (*.jpg *jpeg *webp)')
        # se abre la imagen con el metodo setPixmap()
        self.ui.imagen.setPixmap(QPixmap(self.ruta))
        self.ui.imagen.setScaledContents(True)
    
    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

# Se crea una clase identificada como ConsultarLoteWindow, relacionada a la pantalla para consultar un lote de vacunas            
class ConsultarLoteWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsultarLoteWindow, self).__init__()
        self.ui = Ui_ConsultarLoteIndividual()
        self.ui.setupUi(self)
        self.lote = model.Lote()
        self.logicaLote = logic.Lote()
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        self.ui.btnBuscar.clicked.connect(self.btnBuscarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
        # se mantienen los campos de información vacios
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
    
    # función para buscar un lote según un código dado
    def btnBuscarClicked(self):
        self.lote = model.Lote()
        self.lote.noLote = self.ui.noLote.text()
        # si (self.lote.noLote) no esta vacio, se consulta y almacena en (resultado)
        resultado = self.logicaLote.consultarLote(self.lote.noLote)
        # si (resultado) esta vacío, se mustrá su información y se dan cambios
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
            # se usa el metodo os.stat() para acceder a la información de la imagen de la vacuna 
            try:
                os.stat(directorio)
            # en caso de excepción,  se usa el metodo os.mkdir() para generar el directorio
            except FileNotFoundError:
                os.mkdir(directorio)
            rutaDeGuardado = '{}imagenVacuna.jpg'.format(directorio)
            with open(rutaDeGuardado, "wb") as File:
                File.write(self.lote.imagen)
            # Se abre la imagen abriendo su ruta almacenada en (rutaDeGuardado) con el método .open() y se visualiza con el método .show()
            self.ui.imagen.setPixmap(QPixmap(rutaDeGuardado))
            self.ui.imagen.setScaledContents(True)
            shutil.rmtree(directorio)
        # si (resultado) NO esta vacío, se vacian los campos de información y se muestra un mensaje
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
    
    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

# Se crea una clase identificada como ConsultarLotesWindow, relacionada a la pantalla para consultar todos los lotes de vacunas  
class ConsultarLotesWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsultarLotesWindow, self).__init__()
        self.ui = Ui_ConsultarTodoLote()
        self.ui.setupUi(self)
        self.lote = model.Lote()
        self.logicaLote = logic.Lote()
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        self.ui.btnBuscar.clicked.connect(self.btnCargarDataClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
    
    # función para traer y mostrar los datos guardados en la QTableWidget
    def btnCargarDataClicked(self):
        resultados = self.logicaLote.consultarLotes()
        data = []
        if resultados:
            for lote in resultados:
                data.append((str(lote.noLote), str(lote.fabricante), str(lote.tipoVacuna), str(lote.cantidadRecibida), str(lote.cantidadAsignada), str(lote.cantidadUsada), str(lote.dosisNecesaria), str(lote.temperatura), str(lote.efectividad), str(lote.tiempoProteccion), str(lote.fechaVencimiento)))
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

    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

'''============Modulo de plan============'''

# Se crea la clase identificada como CrearPlanWindow, relacionada a la pantalla para crear un plan de vacunación  
class CrearPlanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CrearPlanWindow, self).__init__()
        self.ui = Ui_CrearPlanVacunacion()
        self.ui.setupUi(self)
        self.plan = model.PlanDeVacunacion()
        self.logicaPlan = logic.PlanDeVacunacion()
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        self.ui.idPlan.textEdited.connect(self.BuscarPlan)
        self.ui.edadMinima.textEdited.connect(self.verificarEdades)
        self.ui.edadMaxima.textEdited.connect(self.verificarEdades)
        self.ui.fechaInicio.dateChanged.connect(self.verificarFechas)
        self.ui.fechaFinal.dateChanged.connect(self.verificarFechas)
        self.ui.btnGuardar.clicked.connect(self.btnGuardarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
     
    # función para verificar un rango de edades a usar para el plan de vacunación
    def verificarEdades(self):
        if self.ui.edadMaxima.text() != '' and self.ui.edadMinima.text() != '':
            retornoEdadMinima = self.logicaPlan.verificarEdad(int(self.ui.edadMinima.text()))
            retornoEdadMaxima = self.logicaPlan.verificarEdad(int(self.ui.edadMaxima.text()))
            # de ser validada el rango, se habilitará el botón de guardado
            if retornoEdadMinima[0] and retornoEdadMaxima[0]: 
                self.ui.mensaje.setText('')
                self.ui.btnGuardar.setEnabled(True)
            # de otra forma, se inhabilitara el botón de guardado
            else: 
                self.ui.mensaje.setText(retornoEdadMaxima[1])
                self.ui.btnGuardar.setEnabled(False)
    
    # función para verificar fechas dadas
    def verificarFechas(self):
        # se toman valores dados en formato de fechas con el metodo .dateTime().toPyDateTime()
        fechaInicioDt = self.ui.fechaInicio.dateTime().toPyDateTime()
        fechaFinalDt = self.ui.fechaFinal.dateTime().toPyDateTime()
        # se toma la fecha actual con el metodo datetime.now() 
        fechaActual = datetime.now()
        # si se valida la fecha, se habilita el botón de guardado
        if (fechaFinalDt >= fechaInicioDt > fechaActual):
            self.ui.btnGuardar.setEnabled(True)
        # de otra manera, se inhabilita el botón de guardado
        else:
            self.ui.btnGuardar.setEnabled(False)

    # función para buscar un plan de vacunación según un código
    def BuscarPlan(self):
        self.plan.idPlan = self.ui.idPlan.text()
        # si (self.plan.idPlan) no esta vacio, se consulta y almacena en (resultado)
        if self.plan.idPlan != '':
            resultado = self.logicaPlan.consultarPlanVacunacion(self.plan.idPlan)
            # si (resultado) esta vacío, se mustrá su información y se dan cambios
            if not resultado:
                self.ui.edadMinima.setEnabled(True)
                self.ui.edadMaxima.setEnabled(True)
                self.ui.fechaInicio.setEnabled(True)
                self.ui.fechaFinal.setEnabled(True)
                self.ui.mensaje.setText('')
            # si (resultado) NO esta vacío, se vacian los campos de información y se muestra un mensaje
            else:
                self.ui.edadMinima.setEnabled(False)
                self.ui.edadMaxima.setEnabled(False)
                self.ui.fechaInicio.setEnabled(False)
                self.ui.fechaFinal.setEnabled(False)
                self.ui.btnGuardar.setEnabled(False)
                self.ui.mensaje.setText('<font color="red">El plan con el numero de plan '+self.plan.idPlan+' ya existe</font>')
    
    # función para guardar información registrada
    def btnGuardarClicked(self):
        # se toman los valores dados y se guardan en self.logicaPlan
        self.plan.idPlan = self.ui.idPlan.text()
        self.plan.edadMinima = self.ui.edadMinima.text()
        self.plan.edadMaxima = self.ui.edadMaxima.text()
        fechaInicioDt = self.ui.fechaInicio.dateTime().toPyDateTime()
        self.plan.fechaInicio = fechaInicioDt.strftime("%Y-%m-%d")
        fechaFinalDt = self.ui.fechaFinal.dateTime().toPyDateTime()
        self.plan.fechaFinal = fechaFinalDt.strftime("%Y-%m-%d")
        # se usa el metodo crearPlanVacunacion() para guardar la información en la base de datos
        self.logicaPlan.crearPlanVacunacion(self.plan)
        self.ui.mensaje.setText('El plan ha sido creado')
        self.ui.btnGuardar.setEnabled(False)
     
    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

# Se crea la clase identificada como ConsultarPlanWindow, relacionada a la pantalla para consultar un plan de vacunación       
class ConsultarPlanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsultarPlanWindow, self).__init__()
        self.ui = Ui_ConsultarPlanIndividual()
        self.ui.setupUi(self)
        self.plan = model.PlanDeVacunacion()
        self.logicaPlan = logic.PlanDeVacunacion()
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        self.ui.btnBuscar.clicked.connect(self.btnBuscarClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
        #se mantienen vacios los campos de información
        self.ui.edadMinima.setText('')
        self.ui.edadMaxima.setText('')
        self.ui.fechaInicio.setText('')
        self.ui.fechaFinal.setText('')
      
    # función para buscar un plan de vacunación según un código
    def btnBuscarClicked(self):
        self.plan = model.PlanDeVacunacion()
        self.plan.idPlan = self.ui.idPlan.text()
        # si (self.plan.idPlan) no esta vacio, se consulta y almacena en (resultado)
        resultado = self.logicaPlan.consultarPlanVacunacion(self.plan.idPlan)
        # si (resultado) esta vacío, se mustrá su información y se dan cambios
        if resultado:
            self.plan = resultado
            self.ui.edadMinima.setText(str(self.plan.edadMinima))
            self.ui.edadMaxima.setText(str(self.plan.edadMaxima))
            self.ui.fechaInicio.setText(str(self.plan.fechaInicio))
            self.ui.fechaFinal.setText(str(self.plan.fechaFinal))
            self.ui.mensaje.setText('')
        # si (resultado) NO esta vacío, se vacian los campos de información y se muestra un mensaje
        else:
            self.ui.edadMinima.setText('')
            self.ui.edadMaxima.setText('')
            self.ui.fechaInicio.setText('')
            self.ui.fechaFinal.setText('')
            self.ui.mensaje.setText('<font color="red">El plan con el numero de plan '+self.plan.idPlan+' no existe</font>')
    
    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

# Se crea la clase identificada como ConsultarPlanesWindow, relacionada a la pantalla para consultar todos los planes de vacunación   
class ConsultarPlanesWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsultarPlanesWindow, self).__init__()
        self.ui = Ui_ConsultarTodoPlan()
        self.ui.setupUi(self)
        self.plan = model.PlanDeVacunacion()
        self.logicaPlan = logic.PlanDeVacunacion()
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        self.ui.btnBuscar.clicked.connect(self.btnCargarDataClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
    
    # función para traer y mostrar los datos guardados en la QTableWidget
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

    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

'''============Modulo de programacion============'''

# Se crea la clase identificada como CrearVacunacionWindow, relacionada a la pantalla para crear una programación de vacunación
class CrearVacunacionWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CrearVacunacionWindow, self).__init__()
        self.ui = Ui_CrearProgramacionVacunacion()
        self.ui.setupUi(self)
        self.programacion = model.ProgramacionDeVacunas()
        self.logicaProgramacion = logic.ProgramacionDeVacunas()
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        self.fechaInicioIngresada = None
        self.ui.fechaInicio.dateChanged.connect(self.verificarFechas)
        self.ui.btnCrear.clicked.connect(self.btnCrearClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
    # función para validar fechas dadas
    def verificarFechas(self):
        # se toman valores dados en formato de fechas con el metodo .dateTime().toPyDateTime()
        fechaInicioIngresadaDt = self.ui.fechaInicio.dateTime().toPyDateTime()
        fechaActual = datetime.now()
        # si es valida, el botón crear se habilita
        if (fechaInicioIngresadaDt > fechaActual):
            self.ui.btnCrear.setEnabled(True)
        # si no es valida, el botón crear se inhabilita
        else:
            self.ui.btnCrear.setEnabled(False)
    
    # función para registrar una nueva programación de vacunación 
    def btnCrearClicked(self):
        fechaIngresadaDt = self.ui.fechaInicio.dateTime().toPyDateTime()
        retorno = self.logicaProgramacion.crearProgramacion(fechaIngresadaDt)
        # se inhabilita el botón crear y muestra un mensaje
        self.ui.mensaje.setText('La programacion de vacunacion ha sido creado')
        self.ui.btnCrear.setEnabled(False)
     
    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

# Se crea la clase identificada como ConsultarVacunacionWindow, relacionada a la pantalla para consultar la programación de vacunación     
class ConsultarVacunacionWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConsultarVacunacionWindow, self).__init__()
        self.ui = Ui_ConsultaProgramacion()
        self.ui.setupUi(self)
        self.programacion = model.ProgramacionDeVacunas()
        self.logicaProgramacion = logic.ProgramacionDeVacunas()
        # se dan las propiedades que funcionan para cada objeto dentro de la pantalla y se asignan funciones
        self.ui.btnBuscar.clicked.connect(self.btnBuscarClicked)
        self.ui.btnConsultaCompleta.clicked.connect(self.btnConsultaClicked)
        self.ui.buttonAtras.clicked.connect(self.goAtras)
        
        self.ui.tableWidget.setRowCount(0)
      
    # función para una buscar la programación de vacunación 
    def btnBuscarClicked(self):
        self.programacion = model.ProgramacionDeVacunas()
        self.programacion.noId = self.ui.noId.text()
        # si (self.programacion.noId) no esta vacio, se almacena en (resultado)
        resultado = self.logicaProgramacion.consultarProgramacionIndividual(self.programacion.noId)
        # si (resultado) no esta vacío, se mustrá su información y se dan cambios
        if resultado:
            # se registran variables para modificar QTableWidget
            persona = resultado[0]
            programacion = resultado[1]
            lote = resultado[2]
            data = ((str(persona.noId), str(persona.nombre), str(persona.apellido), str(persona.direccion), str(persona.telefono), str(persona.correo), str(programacion.fechaProgramada), str(programacion.horaProgramada), str(lote.noLote), str(lote.fabricante)))
            self.ui.tableWidget.setRowCount(1)
            col = 0
            # se crea un bucle para los datos almacenados en data
            for item in data:
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled) #make it not editable
                self.ui.tableWidget.setItem(0, col, cellinfo)
                col += 1
                
            self.ui.mensaje.setText('')
        # si (resultado) esta vacío, se mustrá un mensaje
        else:
            self.ui.mensaje.setText('<font color="red">La cita del paciente con el numero de identificacion '+self.programacion.noId+' no existe</font>')
    
    # función para traer y mostrar los datos guardados en la QTableWidget
    def btnConsultaClicked(self):
        # reune la información respectiva de la base de datos
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
        # los valores obtenido en la base de datos se almacenan en (resultados) con el metodo consultarProgramacionCompleta()
        resultados = self.logicaProgramacion.consultarProgramacionCompleta(datoConsulta)
        data = []
        # si (resultado) no esta vacío, se mustrá su información y se dan cambios
        if resultados:
             # se crea un bucle para los valores en (resultados)
            for plan in resultados:
                persona = plan[0]
                programacion = plan[1]
                lote = plan[2]
                tup = (str(persona.noId), str(persona.nombre), str(persona.apellido), str(persona.direccion), str(persona.telefono), str(persona.correo), str(programacion.fechaProgramada), str(programacion.horaProgramada), str(lote.noLote), str(lote.fabricante))
                data.append(tup)
        self.ui.tableWidget.setRowCount(len(resultados)) 
        row=0
        # se crea un ciclo para los valores dentro de (data)
        for tup in data:
            col=0
            # se crea un ciclo interno para los valores de (tup)
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled) #make it not editable
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1
        # se vacia el mostrador de mensajes
        self.ui.mensaje.setText('')

    # función para regresar a la pantalla principal (MainWindow) por el metodo show()
    def goAtras(self):
        self.anotherWindow = MainWindow()
        self.anotherWindow.show()
        self.close()

# se generan las tablas de la base de datos si no existen ya
logic.crearTablas()
# se inicia la aplicación por el metodo QApplication() y se enceña la ventana principal (MainWindow) con el metodo show()
app = QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
