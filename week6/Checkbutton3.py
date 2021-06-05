from tkinter import *

window = Tk()

window.title("Bind response function")

window.geometry('400x300')


on_click = False  


def callCheckbutton():
    global on_click

    if not on_click:
        on_click = True
        var.set("You have selected Python!")
    else:
        on_click = False
        var.set("Python")


var = StringVar()
var.set("Python")

cb = Checkbutton(window,
                 textvariable=var,
                 command=callCheckbutton)
cb.pack()

window.mainloop()