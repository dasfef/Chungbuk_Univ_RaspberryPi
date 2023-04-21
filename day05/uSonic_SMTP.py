import serial
import smtplib
import tkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from email.mime.text import MIMEText

window = tkinter.Tk()
window.title("Monitor")
window.geometry("200x200+400+400")
window.resizable()

label = tkinter.Label(window, text = "Hello", font = ("Tahoma Bold", 20))
label.pack(side="top")
x = [10, 20, 30, 40, 50]
y = [2, 9, 1, 40, 5]

fig = Figure(figsize = (10, 7))
fig.add_subplot(1, 1, 1).plot(x, y)
canvas = FigureCanvasTkAgg(fig, master = window)
canvas.draw()
canvas.get_tk_widget().pack()


port = "/dev/ttyACM0"
USB_COM = serial.Serial(port, 9600)
if(USB_COM.is_open) :
    USB_COM.close()
USB_COM.open()

# while True:
#     res = USB_COM.readline()
#     result = str(bytes.decode(res))
#     print(result[0:3])
    
window.mainloop()
    

# smtp = smtplib.SMTP('smtp.gmail.com', 587)
# smtp.ehlo()
# smtp.starttls()
# smtp.login('mealhouse3377@gmail.com', 'dueqlswsrdjmwzis')
# 
# msg = MIMEText("contents : ", readSerial())
# msg['Subject'] = "Hello there it's title"
# 
# smtp.sendmail("mealhouse3377@gmail.com", "mealhouse3377@gmail.com", msg.as_string())
# smtp.quit()