from tkinter import *
from tkinter import scrolledtext

window = Tk()

window.title("Window Monitor")
window.geometry("700x200+100+100")
window.resizable()

txt = scrolledtext.ScrolledText(window, width = 85, height = 10)
txt.grid(column = 0, row = 0)

window.mainloop()