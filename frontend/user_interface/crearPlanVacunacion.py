# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crearPlanVacunacion.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CrearPlanVacunacion(object):
    def setupUi(self, CrearPlanVacunacion):
        CrearPlanVacunacion.setObjectName("CrearPlanVacunacion")
        CrearPlanVacunacion.resize(800, 507)
        self.centralwidget = QtWidgets.QWidget(CrearPlanVacunacion)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 35, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.noId = QtWidgets.QLineEdit(self.centralwidget)
        self.noId.setGeometry(QtCore.QRect(399, 95, 231, 35))
        self.noId.setText("")
        self.noId.setObjectName("noId")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 100, 329, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 95, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setEnabled(False)
        self.splitter_3.setGeometry(QtCore.QRect(80, 170, 651, 221))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.nombre = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nombre.setFont(font)
        self.nombre.setObjectName("nombre")
        self.apellido = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.apellido.setFont(font)
        self.apellido.setObjectName("apellido")
        self.fechaVencimiento = QtWidgets.QDateEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fechaVencimiento.setFont(font)
        self.fechaVencimiento.setObjectName("fechaVencimiento")
        self.fechaVencimiento_2 = QtWidgets.QDateEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fechaVencimiento_2.setFont(font)
        self.fechaVencimiento_2.setObjectName("fechaVencimiento_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 420, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 420, 541, 31))
        self.label_6.setObjectName("label_6")
        CrearPlanVacunacion.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(CrearPlanVacunacion)
        QtCore.QMetaObject.connectSlotsByName(CrearPlanVacunacion)

    def retranslateUi(self, CrearPlanVacunacion):
        _translate = QtCore.QCoreApplication.translate
        CrearPlanVacunacion.setWindowTitle(_translate("CrearPlanVacunacion", "Crear plan de vacunación"))
        self.label.setText(_translate("CrearPlanVacunacion", "Para registrar un nuevo lote de vacunas, ingrese la siguiente información."))
        self.label_11.setText(_translate("CrearPlanVacunacion", "Código del nuevo plan"))
        self.pushButton.setText(_translate("CrearPlanVacunacion", "Buscar"))
        self.label_2.setText(_translate("CrearPlanVacunacion", "Edad minima requerida"))
        self.label_3.setText(_translate("CrearPlanVacunacion", "Edad maxima requerida"))
        self.label_4.setText(_translate("CrearPlanVacunacion", "Fecha de inicio"))
        self.label_5.setText(_translate("CrearPlanVacunacion", "Fecha de finalización"))
        self.fechaVencimiento.setDisplayFormat(_translate("CrearPlanVacunacion", "dd/MM/yyyy"))
        self.fechaVencimiento_2.setDisplayFormat(_translate("CrearPlanVacunacion", "dd/MM/yyyy"))
        self.pushButton_2.setText(_translate("CrearPlanVacunacion", "Guardar"))
        self.label_6.setText(_translate("CrearPlanVacunacion", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.menuVolver.setTitle(_translate("CrearPlanVacunacion", "Volver"))
