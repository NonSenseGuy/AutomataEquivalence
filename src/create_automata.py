# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nonsense/Desktop/AutomataEquivalence/src/create_automata.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 381, 17))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 351, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.text_S = QtWidgets.QLineEdit(self.centralwidget)
        self.text_S.setGeometry(QtCore.QRect(10, 120, 351, 25))
        self.text_S.setObjectName("text_S")
        self.text_R = QtWidgets.QLineEdit(self.centralwidget)
        self.text_R.setGeometry(QtCore.QRect(10, 190, 351, 25))
        self.text_R.setObjectName("text_R")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 401, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 401, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 280, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 250, 71, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 361, 17))
        self.label_4.setObjectName("label_4")
        self.automata_n = QtWidgets.QLabel(self.centralwidget)
        self.automata_n.setGeometry(QtCore.QRect(10, 0, 91, 17))
        self.automata_n.setObjectName("automata_n")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ingrese todos los estados separados por coma"))
        self.label_2.setText(_translate("MainWindow", "Ingrese el alfabeto de estimulos separados por coma"))
        self.label_3.setText(_translate("MainWindow", "Ingrese el alfabeto de respuestas separados por coma"))
        self.pushButton.setText(_translate("MainWindow", "Aceptar"))
        self.label_4.setText(_translate("MainWindow", "Ingrese estado inicial"))
        self.automata_n.setText(_translate("MainWindow", "Automata1"))

