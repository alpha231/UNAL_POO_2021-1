# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultaLoteIndividual.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsultarLoteIndividual(object):
    def setupUi(self, ConsultarLoteIndividual):
        ConsultarLoteIndividual.setObjectName("ConsultarLoteIndividual")
        ConsultarLoteIndividual.setEnabled(True)
        ConsultarLoteIndividual.resize(800, 670)
        self.centralwidget = QtWidgets.QWidget(ConsultarLoteIndividual)
        self.centralwidget.setObjectName("centralwidget")
        self.BuscarNoIdConsultaUsuario = QtWidgets.QPushButton(self.centralwidget)
        self.BuscarNoIdConsultaUsuario.setEnabled(True)
        self.BuscarNoIdConsultaUsuario.setGeometry(QtCore.QRect(630, 20, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BuscarNoIdConsultaUsuario.setFont(font)
        self.BuscarNoIdConsultaUsuario.setObjectName("BuscarNoIdConsultaUsuario")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 60, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setGeometry(QtCore.QRect(80, 20, 550, 35))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_24 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.noIdConsultaUsuario = QtWidgets.QLineEdit(self.splitter_4)
        self.noIdConsultaUsuario.setEnabled(True)
        self.noIdConsultaUsuario.setFrame(True)
        self.noIdConsultaUsuario.setObjectName("noIdConsultaUsuario")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(80, 80, 641, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_1.setFont(font)
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 10, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 8, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 9, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setGeometry(QtCore.QRect(560, 530, 41, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(500, 530, 41, 17))
        self.checkBox.setObjectName("checkBox")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(80, 520, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(80, 570, 611, 31))
        self.label_25.setObjectName("label_25")
        ConsultarLoteIndividual.setCentralWidget(self.centralwidget)


        self.retranslateUi(ConsultarLoteIndividual)
        QtCore.QMetaObject.connectSlotsByName(ConsultarLoteIndividual)

    def retranslateUi(self, ConsultarLoteIndividual):
        _translate = QtCore.QCoreApplication.translate
        ConsultarLoteIndividual.setWindowTitle(_translate("ConsultarLoteIndividual", "Consultar lote individual"))
        self.BuscarNoIdConsultaUsuario.setText(_translate("ConsultarLoteIndividual", "Buscar"))
        self.label_24.setText(_translate("ConsultarLoteIndividual", "Ingrese el número de lote que desea consultar"))
        self.label_12.setText(_translate("ConsultarLoteIndividual", "No. de Lote"))
        self.label_15.setText(_translate("ConsultarLoteIndividual", "Cantidad de vacunas recibidas"))
        self.label_19.setText(_translate("ConsultarLoteIndividual", "Temperatura de almacenamiento"))
        self.label_17.setText(_translate("ConsultarLoteIndividual", "Cantidad de vacunas usadas"))
        self.label_22.setText(_translate("ConsultarLoteIndividual", "Fecha de vencimiento"))
        self.label_16.setText(_translate("ConsultarLoteIndividual", "Cantidad de vacunas asignadas"))
        self.label_13.setText(_translate("ConsultarLoteIndividual", "Fabricante"))
        self.label_14.setText(_translate("ConsultarLoteIndividual", "Tipo de vacuna"))
        self.label_18.setText(_translate("ConsultarLoteIndividual", "Dosis necesarias"))
        self.label_20.setText(_translate("ConsultarLoteIndividual", "Efectividad"))
        self.label_21.setText(_translate("ConsultarLoteIndividual", "Tiempo de protección"))
        self.checkBox_2.setText(_translate("ConsultarLoteIndividual", "NO"))
        self.checkBox.setText(_translate("ConsultarLoteIndividual", "SI"))
        self.label_23.setText(_translate("ConsultarLoteIndividual", "<html><head/><body><p align=\"center\">¿Desea abrir la imagen?</p></body></html>"))
        self.label_25.setText(_translate("ConsultarLoteIndividual", "<html><head/><body><p align=\"center\"><span style=\" color:#aa0000;\"><br/></span></p></body></html>"))
        self.menuVolver.setTitle(_translate("ConsultarLoteIndividual", "Volver"))
