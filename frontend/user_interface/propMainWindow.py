# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'propMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PropMainWindow(object):
    def setupUi(self, PropMainWindow):
        PropMainWindow.setObjectName("PropMainWindow")
        PropMainWindow.setEnabled(True)
        PropMainWindow.resize(812, 431)
        PropMainWindow.setMinimumSize(QtCore.QSize(812, 431))
        PropMainWindow.setMaximumSize(QtCore.QSize(813, 431))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        PropMainWindow.setFont(font)
        PropMainWindow.setMouseTracking(False)
        PropMainWindow.setTabletTracking(False)
        PropMainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        PropMainWindow.setAnimated(True)
        PropMainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(PropMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DocumentacionUsuario = QtWidgets.QPushButton(self.centralwidget)
        self.DocumentacionUsuario.setGeometry(QtCore.QRect(0, 350, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.DocumentacionUsuario.setFont(font)
        self.DocumentacionUsuario.setMouseTracking(True)
        self.DocumentacionUsuario.setStyleSheet("background-color: rgb(242, 243, 244);")
        self.DocumentacionUsuario.setCheckable(False)
        self.DocumentacionUsuario.setObjectName("DocumentacionUsuario")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 50, 811, 51))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(0, 163, 224);\n"
"border-color: rgb(85, 170, 255);\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 110, 301, 251))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(:/icono vacuna/icono vacuna.png);\n"
"border-image: url(:/iconoVacuna/icono vacuna.png);")
        self.label_2.setObjectName("label_2")
        PropMainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(PropMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 812, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuAfiliados = QtWidgets.QMenu(self.menuBar)
        self.menuAfiliados.setObjectName("menuAfiliados")
        self.menuLotes_de_vacunas = QtWidgets.QMenu(self.menuBar)
        self.menuLotes_de_vacunas.setObjectName("menuLotes_de_vacunas")
        self.menuConsultar = QtWidgets.QMenu(self.menuLotes_de_vacunas)
        self.menuConsultar.setMouseTracking(True)
        self.menuConsultar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menuConsultar.setObjectName("menuConsultar")
        self.menuPlan_de_vacunacion = QtWidgets.QMenu(self.menuBar)
        self.menuPlan_de_vacunacion.setObjectName("menuPlan_de_vacunacion")
        self.menuConsultar_2 = QtWidgets.QMenu(self.menuPlan_de_vacunacion)
        self.menuConsultar_2.setObjectName("menuConsultar_2")
        self.menuProgramacion_de_vacunacion = QtWidgets.QMenu(self.menuBar)
        self.menuProgramacion_de_vacunacion.setObjectName("menuProgramacion_de_vacunacion")
        self.menuConsultar_3 = QtWidgets.QMenu(self.menuProgramacion_de_vacunacion)
        self.menuConsultar_3.setObjectName("menuConsultar_3")
        PropMainWindow.setMenuBar(self.menuBar)
        self.actionConsultarUsuario = QtWidgets.QAction(PropMainWindow)
        self.actionConsultarUsuario.setObjectName("actionConsultarUsuario")
        self.actionDesafiliarUsuario = QtWidgets.QAction(PropMainWindow)
        self.actionDesafiliarUsuario.setObjectName("actionDesafiliarUsuario")
        self.actionVacunarUsuario = QtWidgets.QAction(PropMainWindow)
        self.actionVacunarUsuario.setObjectName("actionVacunarUsuario")
        self.actionCrearLote = QtWidgets.QAction(PropMainWindow)
        self.actionCrearLote.setObjectName("actionCrearLote")
        self.actionConsultaCompletaLote = QtWidgets.QAction(PropMainWindow)
        self.actionConsultaCompletaLote.setPriority(QtWidgets.QAction.NormalPriority)
        self.actionConsultaCompletaLote.setObjectName("actionConsultaCompletaLote")
        self.actionConsultaIndividualLote = QtWidgets.QAction(PropMainWindow)
        self.actionConsultaIndividualLote.setObjectName("actionConsultaIndividualLote")
        self.actionCompleta = QtWidgets.QAction(PropMainWindow)
        self.actionCompleta.setObjectName("actionCompleta")
        self.actionCrearPlan = QtWidgets.QAction(PropMainWindow)
        self.actionCrearPlan.setObjectName("actionCrearPlan")
        self.actionConsultaCompletaPlan = QtWidgets.QAction(PropMainWindow)
        self.actionConsultaCompletaPlan.setObjectName("actionConsultaCompletaPlan")
        self.actionConsultaIndividualPlan = QtWidgets.QAction(PropMainWindow)
        self.actionConsultaIndividualPlan.setObjectName("actionConsultaIndividualPlan")
        self.actionCrearProgramacion = QtWidgets.QAction(PropMainWindow)
        self.actionCrearProgramacion.setObjectName("actionCrearProgramacion")
        self.actionConsultaCompletaProgramacion = QtWidgets.QAction(PropMainWindow)
        self.actionConsultaCompletaProgramacion.setObjectName("actionConsultaCompletaProgramacion")
        self.actionConsultaIndividualProgramacion = QtWidgets.QAction(PropMainWindow)
        self.actionConsultaIndividualProgramacion.setObjectName("actionConsultaIndividualProgramacion")
        self.actionCrearUsuario = QtWidgets.QAction(PropMainWindow)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.actionCrearUsuario.setFont(font)
        self.actionCrearUsuario.setObjectName("actionCrearUsuario")
        self.menuAfiliados.addAction(self.actionCrearUsuario)
        self.menuAfiliados.addAction(self.actionConsultarUsuario)
        self.menuAfiliados.addAction(self.actionDesafiliarUsuario)
        self.menuAfiliados.addAction(self.actionVacunarUsuario)
        self.menuConsultar.addAction(self.actionConsultaCompletaLote)
        self.menuConsultar.addAction(self.actionConsultaIndividualLote)
        self.menuLotes_de_vacunas.addAction(self.actionCrearLote)
        self.menuLotes_de_vacunas.addAction(self.menuConsultar.menuAction())
        self.menuConsultar_2.addAction(self.actionConsultaCompletaPlan)
        self.menuConsultar_2.addAction(self.actionConsultaIndividualPlan)
        self.menuPlan_de_vacunacion.addAction(self.actionCrearPlan)
        self.menuPlan_de_vacunacion.addAction(self.menuConsultar_2.menuAction())
        self.menuConsultar_3.addAction(self.actionConsultaCompletaProgramacion)
        self.menuConsultar_3.addAction(self.actionConsultaIndividualProgramacion)
        self.menuProgramacion_de_vacunacion.addAction(self.actionCrearProgramacion)
        self.menuProgramacion_de_vacunacion.addAction(self.menuConsultar_3.menuAction())
        self.menuBar.addAction(self.menuAfiliados.menuAction())
        self.menuBar.addAction(self.menuLotes_de_vacunas.menuAction())
        self.menuBar.addAction(self.menuPlan_de_vacunacion.menuAction())
        self.menuBar.addAction(self.menuProgramacion_de_vacunacion.menuAction())

        self.retranslateUi(PropMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PropMainWindow)

    def retranslateUi(self, PropMainWindow):
        _translate = QtCore.QCoreApplication.translate
        PropMainWindow.setWindowTitle(_translate("PropMainWindow", "P_MainWindow"))
        PropMainWindow.setToolTip(_translate("PropMainWindow", "cosas"))
        self.DocumentacionUsuario.setText(_translate("PropMainWindow", "Ayuda para usuarios"))
        self.label.setText(_translate("PropMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Programa de vacunación</span></p></body></html>"))
        self.label_2.setText(_translate("PropMainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.menuAfiliados.setTitle(_translate("PropMainWindow", "Afiliados"))
        self.menuLotes_de_vacunas.setTitle(_translate("PropMainWindow", "Lotes de vacunas"))
        self.menuConsultar.setTitle(_translate("PropMainWindow", "Consultar"))
        self.menuPlan_de_vacunacion.setTitle(_translate("PropMainWindow", "Plan de vacunación"))
        self.menuConsultar_2.setTitle(_translate("PropMainWindow", "Consultar"))
        self.menuProgramacion_de_vacunacion.setTitle(_translate("PropMainWindow", "Programacion de vacunación"))
        self.menuConsultar_3.setTitle(_translate("PropMainWindow", "Consultar"))
        self.actionConsultarUsuario.setText(_translate("PropMainWindow", "Consultar"))
        self.actionDesafiliarUsuario.setText(_translate("PropMainWindow", "Desafiliar"))
        self.actionVacunarUsuario.setText(_translate("PropMainWindow", "Vacunar"))
        self.actionCrearLote.setText(_translate("PropMainWindow", "Crear"))
        self.actionConsultaCompletaLote.setText(_translate("PropMainWindow", "Consulta completa"))
        self.actionConsultaIndividualLote.setText(_translate("PropMainWindow", "Consulta individual"))
        self.actionCompleta.setText(_translate("PropMainWindow", "Completa"))
        self.actionCrearPlan.setText(_translate("PropMainWindow", "Crear"))
        self.actionConsultaCompletaPlan.setText(_translate("PropMainWindow", "Consulta completa"))
        self.actionConsultaIndividualPlan.setText(_translate("PropMainWindow", "Consulta individual"))
        self.actionCrearProgramacion.setText(_translate("PropMainWindow", "Crear"))
        self.actionConsultaCompletaProgramacion.setText(_translate("PropMainWindow", "Consulta completa"))
        self.actionConsultaIndividualProgramacion.setText(_translate("PropMainWindow", "Consulta individual"))
        self.actionCrearUsuario.setText(_translate("PropMainWindow", "Crear"))
# import imagesForUi_rc
