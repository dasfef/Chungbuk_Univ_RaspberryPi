import tkinter
window = tkinter.Tk()

window.title("Window Monitor")
window.geometry("640x200+100+100")
window.resizable()

label = tkinter.Label(window, text = "Hello", font = ("Tahoma Bold", 20))
label.grid(column = 0, row = 0)

def clicked() :
    res = "Welcome to " + txt.get()
    label.configure(text = res)

txt = tkinter.Entry(window, width = 10)
txt.grid(column = 0, row = 1)

btn = tkinter.Button(window, text = "CLICK HERE", command = clicked)
btn.grid(column = 0, row = 2)

window.mainloop()