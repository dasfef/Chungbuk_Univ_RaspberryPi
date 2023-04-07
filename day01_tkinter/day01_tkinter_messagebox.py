from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Window Monitor")
window.geometry("640x220+100+100")
window.resizable()

def Clicked() :
    messagebox.showinfo("Button", "Clicked")
    
btn = Button(window, text = "Click Here", command = Clicked)
btn.grid(column = 0, row = 0)

window.mainloop()