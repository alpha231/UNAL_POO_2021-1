# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desafiliarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_desafiliarUsuario(object):
    def setupUi(self, desafiliarUsuario):
        desafiliarUsuario.setObjectName("desafiliarUsuario")
        desafiliarUsuario.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(desafiliarUsuario)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 440, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setGeometry(QtCore.QRect(80, 80, 550, 35))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_11 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.noId = QtWidgets.QLineEdit(self.splitter_4)
        self.noId.setObjectName("noId")
        self.mensaje = QtWidgets.QLabel(self.centralwidget)
        self.mensaje.setGeometry(QtCore.QRect(160, 500, 550, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mensaje.setFont(font)
        self.mensaje.setObjectName("mensaje")
        self.buttonAtras = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAtras.setGeometry(QtCore.QRect(40, 500, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonAtras.setFont(font)
        self.buttonAtras.setObjectName("buttonAtras")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 130, 506, 353))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.gridLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(100)
        self.formLayout_2.setVerticalSpacing(5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.nombre = QtWidgets.QLabel(self.gridLayoutWidget)
        self.nombre.setMinimumSize(QtCore.QSize(200, 30))
        self.nombre.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nombre.setFont(font)
        self.nombre.setText("")
        self.nombre.setObjectName("nombre")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nombre)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.apellido = QtWidgets.QLabel(self.gridLayoutWidget)
        self.apellido.setMinimumSize(QtCore.QSize(200, 30))
        self.apellido.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.apellido.setFont(font)
        self.apellido.setText("")
        self.apellido.setObjectName("apellido")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.apellido)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.telefono = QtWidgets.QLabel(self.gridLayoutWidget)
        self.telefono.setMinimumSize(QtCore.QSize(200, 30))
        self.telefono.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.telefono.setFont(font)
        self.telefono.setText("")
        self.telefono.setObjectName("telefono")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.telefono)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.correo = QtWidgets.QLabel(self.gridLayoutWidget)
        self.correo.setMinimumSize(QtCore.QSize(200, 30))
        self.correo.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.correo.setFont(font)
        self.correo.setText("")
        self.correo.setObjectName("correo")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.correo)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.ciudad = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ciudad.setMinimumSize(QtCore.QSize(200, 30))
        self.ciudad.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ciudad.setFont(font)
        self.ciudad.setText("")
        self.ciudad.setObjectName("ciudad")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.ciudad)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.fechaNacimiento = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fechaNacimiento.setMinimumSize(QtCore.QSize(200, 30))
        self.fechaNacimiento.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fechaNacimiento.setFont(font)
        self.fechaNacimiento.setText("")
        self.fechaNacimiento.setObjectName("fechaNacimiento")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.fechaNacimiento)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.fechaAfiliacion = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fechaAfiliacion.setMinimumSize(QtCore.QSize(200, 30))
        self.fechaAfiliacion.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fechaAfiliacion.setFont(font)
        self.fechaAfiliacion.setText("")
        self.fechaAfiliacion.setObjectName("fechaAfiliacion")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.fechaAfiliacion)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.direccion = QtWidgets.QLabel(self.gridLayoutWidget)
        self.direccion.setMinimumSize(QtCore.QSize(200, 30))
        self.direccion.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.direccion.setFont(font)
        self.direccion.setText("")
        self.direccion.setObjectName("direccion")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.direccion)
        self.vacunado = QtWidgets.QLabel(self.gridLayoutWidget)
        self.vacunado.setMinimumSize(QtCore.QSize(200, 30))
        self.vacunado.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vacunado.setFont(font)
        self.vacunado.setText("")
        self.vacunado.setObjectName("vacunado")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.vacunado)
        self.fechaDesafiliacion = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.fechaDesafiliacion.setMinimumSize(QtCore.QSize(200, 30))
        self.fechaDesafiliacion.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fechaDesafiliacion.setFont(font)
        self.fechaDesafiliacion.setObjectName("fechaDesafiliacion")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.fechaDesafiliacion)
        desafiliarUsuario.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(desafiliarUsuario)
        self.statusbar.setObjectName("statusbar")
        desafiliarUsuario.setStatusBar(self.statusbar)

        self.retranslateUi(desafiliarUsuario)
        QtCore.QMetaObject.connectSlotsByName(desafiliarUsuario)

    def retranslateUi(self, desafiliarUsuario):
        _translate = QtCore.QCoreApplication.translate
        desafiliarUsuario.setWindowTitle(_translate("desafiliarUsuario", "Desafiliar Usuario"))
        self.pushButton_2.setText(_translate("desafiliarUsuario", "Guardar"))
        self.label_11.setText(_translate("desafiliarUsuario", "Documento de identidad"))
        self.mensaje.setText(_translate("desafiliarUsuario", "<html><head/><body><p align=\"center\"><span style=\" color:#aa0000;\"><br/></span></p></body></html>"))
        self.buttonAtras.setText(_translate("desafiliarUsuario", "Atras"))
        self.label_23.setText(_translate("desafiliarUsuario", "Nombre"))
        self.label_24.setText(_translate("desafiliarUsuario", "Apellido"))
        self.label_25.setText(_translate("desafiliarUsuario", "Direccion"))
        self.label_26.setText(_translate("desafiliarUsuario", "Telefono"))
        self.label_27.setText(_translate("desafiliarUsuario", "Correo"))
        self.label_28.setText(_translate("desafiliarUsuario", "Ciudad"))
        self.label_29.setText(_translate("desafiliarUsuario", "Fecha de nacimiento"))
        self.label_30.setText(_translate("desafiliarUsuario", "Fecha de afiliacion"))
        self.label_31.setText(_translate("desafiliarUsuario", "Vacunado"))
        self.label_32.setText(_translate("desafiliarUsuario", "Fecha desafiliacion"))
        self.fechaDesafiliacion.setDisplayFormat(_translate("desafiliarUsuario", "dd/MM/yyyy"))
