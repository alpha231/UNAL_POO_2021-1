from PyQt5 import QtCore, QtWidgets, QtGui

from user_interface.propMainWindow import Ui_PropMainWindow  # importa nuestro archivo generado
from user_interface.crearVacunado import Ui_MainWindow 
from user_interface.consultarUsuario import Ui_ConsultarUsuario
from user_interface.crearLote import Ui_CrearLote
import webbrowser
import sys
sys.path.append('backend_POO')
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
        

    


class PropMainWindow(mywindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(PropMainWindow, self).__init__()
        self.ui = Ui_PropMainWindow()
        self.ui.setupUi(self)
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        self.lote = model.Lote()
        self.logicaLote = logic.Lote()
        self.ui.actionCrear_5.triggered.connect(self.abrir_crearVacunado)
        self.ui.actionCrear.triggered.connect(self.abrir_crearLote)
        self.ui.actionConsultar_Afiliado.triggered.connect(self.abrir_consultarAfiliado)
        self.ui.DocumentacionUsuario.clicked.connect(self.ayudaUsuario)
        
        
       
    def abrir_crearVacunado(self):
        self.crearVacunadoWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.crearVacunadoWindow)
        self.crearVacunadoWindow.show()
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
            self.ui.label_30.setText("")
        else:
            self.ui.splitter_3.setEnabled(False)
            self.ui.pushButton_2.setEnabled(False)
            self.ui.vacunado.setEnabled(False)
            self.ui.fechaDesafiliacion.setEnabled(False)
            self.ui.label_30.setText("El usuario digitado ya existe")

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
        self.ui.label_30.setText("Se registró un nuevo usuario")



    def abrir_consultarAfiliado(self):
        self.crearConsultarAfiliadoWindow=QtWidgets.QMainWindow()
        self.ui=Ui_ConsultarUsuario()
        self.ui.setupUi(self.crearConsultarAfiliadoWindow)
        self.crearConsultarAfiliadoWindow.show()
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        self.ui.BuscarNoIdConsultaUsuario.clicked.connect(self.BuscarNoIdConsultaUsuarioClicked)

    def BuscarNoIdConsultaUsuarioClicked(self):
        self.persona.noId = self.ui.noIdConsultaUsuario.text()
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        if not resultado:
            self.ui.label_11.setText("El documento escrito no pertenece a ningun usuario afiliado")
            self.ui.label_1.setText("")
            self.ui.label_2.setText("")
            self.ui.label_3.setText("")
            self.ui.label_4.setText("")
            self.ui.label_5.setText("")
            self.ui.label_6.setText("")
            self.ui.label_7.setText("")
            self.ui.label_8.setText("")
            self.ui.label_9.setText("")
            self.ui.label_10.setText("")
        else:
            self.ui.label_11.setText("")
            self.ui.label_1.setText(self.persona.nombre)
            self.ui.label_2.setText(self.persona.apellido)
            self.ui.label_3.setText(self.persona.direccion)
            self.ui.label_4.setText(self.persona.telefono)
            self.ui.label_5.setText(self.persona.correo)
            self.ui.label_6.setText(self.persona.ciudad)
            self.ui.label_7.setText(self.persona.fechaNacimiento)
            self.ui.label_8.setText(self.persona.fechaAfiliacion)
            self.ui.label_9.setText(self.persona.vacunado)
            self.ui.label_10.setText("Existe, pero no funciona... Aún")


    def abrir_crearLote(self):
        self.crearLoteWindow=QtWidgets.QMainWindow()
        self.ui=Ui_CrearLote()
        self.ui.setupUi(self.crearLoteWindow)
        self.crearLoteWindow.show()

    def ayudaUsuario(self):
        # Se almacena un link correspondiente a la ubicación del pdf
        path = 'https://drive.google.com/file/d/1L8BBeJP-mc_QLmNplzYemZgxe4j1F_Bx/view?usp=sharing'
        # Abrimos el archivo en el navegador siguiendo la variable (path) por el método webbrowser.open_new() de la librería webbrowser
        webbrowser.open_new(path)


       

logic.crearTablas()
app = QtWidgets.QApplication([])
application = PropMainWindow()
application.show()
sys.exit(app.exec())
