import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

uiWindow = 'MultiForm.ui'
uiDialog_A = 'MultiForm-A.ui'
uiDialog_B = 'MultiForm-B.ui'

class MyWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        uic.loadUi(uiWindow, self)
        
        self.dialog_a = None
        self.dialog_b = None
        self.pushButton_1.clicked.connect(self.buttonClick_1)
        self.pushButton_2.clicked.connect(self.buttonClick_2)
        
    def buttonClick_1(self) :
        if self.dialog_a is None:
            self.dialog_a = MyDialog_A()
        self.dialog_a.show()
        
    def buttonClick_2(self) :
        if self.dialog_b is None:
            self.dialog_b = MyDialog_B()
        self.dialog_b.show()
        
class MyDialog_A(QDialog):
    def __init__(self) :
        super().__init__()
        uic.loadUi(uiDialog_A, self)
        
        self.qPixmap = QPixmap()
        self.qPixmap.load('paint.png')
        self.qPixmap = self.qPixmap.scaledToWidth(322)
        self.label.setPixmap(self.qPixmap)
        
class MyDialog_B(QDialog) :
    def __init__(self) :
        super().__init__()
        uic.loadUi(uiDialog_B, self)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWindow()
    form.show()
    sys.exit(app.exec_())
        