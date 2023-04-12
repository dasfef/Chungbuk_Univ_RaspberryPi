import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

uiDialog = 'ButtonPassword.ui'

class MyDialog(QDialog) :
    def __init__(self) :
        QDialog.__init__(self, None)
        uic.loadUi(uiDialog, self)

        self.pushButton_1.clicked.connect(self.buttonClick_1)
        self.pushButton_2.clicked.connect(self.buttonClick_2)
        self.pushButton_3.clicked.connect(self.buttonClick_3)
        self.pushButton_4.clicked.connect(self.buttonClick_4)
        self.pushButton_5.clicked.connect(self.buttonClick_5)
        self.pushButton_6.clicked.connect(self.buttonClick_6)
        self.pushButton_7.clicked.connect(self.buttonClick_7)
        self.pushButton_8.clicked.connect(self.buttonClick_8)
        self.pushButton_9.clicked.connect(self.buttonClick_9)
        self.pushButton_10.clicked.connect(self.buttonClick_10)
        self.pushButton_BS.clicked.connect(self.buttonClick_BS)
        self.pushButton_CLR.clicked.connect(self.buttonClick_CLR)
        self.pushButton_SUB.clicked.connect(self.buttonClick_SUB)

        self.msg = QMessageBox()

    def buttonClick_1(self) :
        self.lineEdit.setText(self.lineEdit.text() + '1')
    def buttonClick_2(self) :
        self.lineEdit.setText(self.lineEdit.text() + '2')
    def buttonClick_3(self) :
        self.lineEdit.setText(self.lineEdit.text() + '3')
    def buttonClick_4(self) :
        self.lineEdit.setText(self.lineEdit.text() + '4')
    def buttonClick_5(self) :
        self.lineEdit.setText(self.lineEdit.text() + '5')
    def buttonClick_6(self) :
        self.lineEdit.setText(self.lineEdit.text() + '6')
    def buttonClick_7(self) :
        self.lineEdit.setText(self.lineEdit.text() + '7')
    def buttonClick_8(self) :
        self.lineEdit.setText(self.lineEdit.text() + '8')
    def buttonClick_9(self) :
        self.lineEdit.setText(self.lineEdit.text() + '9')
    def buttonClick_10(self) :
        self.lineEdit.setText(self.lineEdit.text() + '10')
    def buttonClick_BS(self) :
        self.lineEdit.setFocus()
        self.lineEdit.backspace()
        #print(self.lineEdit.text())
    def buttonClick_CLR(self) :
        self.lineEdit.setText("")
    def buttonClick_SUB(self) :
        pw = self.lineEdit.text()
        self.lineEdit.setText("")

        self.msg.setWindowTitle("Welcome")
        if pw == '1234':
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Welcome")
        else :
            self.msg.setIcon(QMessageBox.Question)
            self.msg.setText("Wrong Password")

        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyDialog()
    form.show()
    app.exec()
    