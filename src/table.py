from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
 
 
class Window(QWidget):
    def __init__(self, row_count, col_count, automata):
        super().__init__()
        self.rc = row_count
        self.cc = col_count
        self.a = automata 
 
        self.title = "PyQt5 Tables"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 400
 
 
        self.InitWindow()
 
 
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
 
        self.creatingTables()
 
 
        self.show()
 
    def creatingTables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(int(self.rc)+1)
        self.tableWidget.setColumnCount(self.cc)

 
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget)
        self.setLayout(self.vBoxLayout)
 
 
# App = QApplication(sys.argv)
# window = Window()
# sys.exit(App.exec())