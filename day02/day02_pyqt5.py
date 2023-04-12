import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

uiDialog = 'untitled.ui'

class MyDialog(QDialog):
    def __init__(self) :
        QDialog.__init__(self, None)
        uic.loadUi(uiDialog, self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyDialog()
    form.show()
    app.exec()
        