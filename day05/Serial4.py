import serial
from tkinter import *

port = "/dev/ttyACM0"
USB_COM = serial.Serial(port, 9600)
if(USB_COM.is_open) :
    USB_COM.close()
USB_COM.open()

window = Tk()
window.title("Serial Monitor")

scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill = Y)

log = Text(window, width = 30, height = 30, takefocus = 0)
log.pack()

log.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = log.yview)

serBuffer = ""

def readSerial():
    res = USB_COM.readline()
    log.insert('0.0', res)
    window.after(10, readSerial)
    
window.after(1000, readSerial)
window.mainloop()