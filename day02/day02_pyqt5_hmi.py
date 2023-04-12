import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

uiWidget = 'HMI.ui'

class MyWindow(QWidget) :
    def __init__(self) :
        super().__init__()
        uic.loadUi(uiWidget, self)
        
        self.progressBar.setStyleSheet('QProgressBar::chunk{background-color:red;}')
        
        self.dial.sliderReleased.connect(self.dial_Released)
        self.horizontalSlider.valueChanged.connect(self.slide_changed)
        
        self.timer = QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.time_tick)
        self.timer.start()
        
    def slide_changed(self) :
        self.progressBar.setValue(self.horizontalSlider.value())
        
    def dial_Released(self) :
        self.label.setText(str(self.dial.value()))
        
    def time_tick(self) :
        sender = self.sender()
        currentTime = QTime.currentTime().toString('HH:mm:ss')
        
        if id(sender) == id(self.timer) :
            self.lcdNumber.display(currentTime)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWindow()
    form.show()
    sys.exit(app.exec_())