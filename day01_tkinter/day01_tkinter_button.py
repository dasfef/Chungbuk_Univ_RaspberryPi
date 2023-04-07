from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Window Monitor")
window.geometry("640x200+100+100")
window.resizable()

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text = "Select", var = chk_state)
chk.grid(column = 0, row = 0)

rdo1 = Radiobutton(window, text = '1', value = 1)
rdo2 = Radiobutton(window, text = '2', value = 2)
rdo3 = Radiobutton(window, text = '3', value = 3)
rdo1.grid(column = 1, row = 0)
rdo2.grid(column = 2, row = 0)
rdo3.grid(column = 3, row = 0)
window.mainloop()