# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nonsense/Desktop/AutomataEquivalence/src/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from create_automata import Ui_CreateAutomataWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(299, 92)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 20, 151, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_create_automata_window)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 299, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_create_automata_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateAutomataWindow(str(self.comboBox.currentText()))
        print(str(self.comboBox.currentText()))
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Crear automatas"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Moore"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Moore"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Mealy"))

