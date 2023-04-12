import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

uiForm = "TestButtonSignal.ui"

class MyWindow(QMainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self, None)
        uic.loadUi(uiForm, self)

        self.pushButton.clicked.connect(self.buttonClick_1)
        self.pushButton_2.clicked.connect(self.buttonClick_2)

    def buttonClick_1(self) :
        self.label.setText("Pressed Button 1")

    def buttonClick_2(self) :
        self.label.setText("Pressed Button 2")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWindow()
    form.show()
    app.exec()
        