# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transitions_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MealyAutomata(object):

    def __init__(self, automata, create_automata_window, index):
        super(Ui_MealyAutomata, self).__init__()
        self.automata = automata
        self.create_automata_window = create_automata_window
        self.index = index 


    def setupUi(self, MealyAutomata):
        MealyAutomata.setObjectName("MealyAutomata")
        MealyAutomata.resize(534, 177)
        self.label = QtWidgets.QLabel(MealyAutomata)
        self.label.setGeometry(QtCore.QRect(0, 10, 481, 17))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(MealyAutomata)
        self.lineEdit.setGeometry(QtCore.QRect(0, 30, 481, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(MealyAutomata)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 471, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MealyAutomata)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 331, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MealyAutomata)
        self.label_4.setGeometry(QtCore.QRect(0, 100, 231, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(MealyAutomata)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 130, 331, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(MealyAutomata)
        self.pushButton.setGeometry(QtCore.QRect(390, 130, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)

        self.retranslateUi(MealyAutomata)
        QtCore.QMetaObject.connectSlotsByName(MealyAutomata)



    def retranslateUi(self, MealyAutomata):
        _translate = QtCore.QCoreApplication.translate
        MealyAutomata.setWindowTitle(_translate("MealyAutomata", "Dialog"))
        self.label.setText(_translate("MealyAutomata", "Ingrese todos los estados usados por el automata separados por coma "))
        self.label_2.setText(_translate("MealyAutomata", "Ingrese las transiciones del automata de la siguiente manera "))
        self.label_3.setText(_translate("MealyAutomata", "(estimulo, estado inicial, estado final, respuesta)"))
        self.label_4.setText(_translate("MealyAutomata", "Por ej: (0,A,B,1);(0,B,A,0); .... "))
        self.pushButton.setText(_translate("MealyAutomata", "Aceptar"))
    
    def parse_inputs(self, inp):
        s = inp.split(',')
        return [i.strip() for i in s]

    def parse_tuples(self, t):
        s = t.split(';')
        l = [i.strip() for i in s]
        k = self.parse_inputs(l)
        print(k)
        print("el de arriba es k")

        return k

    def on_click(self):
        self.add_states()
        self.add_transitions()
        self.create_automata_window.automatas[index] = self.automata
        self.close()

    def add_states(self):
        l = self.parse_inputs(self.lineEdit.text())
        for item in l:
            self.automata.add_state(item)
    
    def add_transitions(self):
        l = self.parse_tuples(self.lineEdit_2.text())
        print(l)
        for s,q0,q1,r in l:
            self.automata.add_transition(s,q0,q1,r)
            


