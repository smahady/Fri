from tkinter import *

window = Tk()
window.title("Radiobutton Demo 3")
# window.geometry('400x300+1000+150')

lbl = Label(window, text="Choose a programming language:",
            width=30,
            justify=LEFT,   # for multiple lines of text
           )  
lbl.pack(anchor=W)  # anchor：way to adjust

languages = [
    ("Python", 1),
    ("C++", 2),
    ("C", 3),
    ("Java", 4),
    ("JavaScript", 5)
]

var = IntVar()
var.set(0)  #set which button is selected by default (1-5) 0 means none of them selected


def my_choice():
    print(var.get())


for language, val in languages:
    rb = Radiobutton(window,
                     text=language,
                     indicator=0, #special control parameter, 0 means the components appear in the form of buttons
                     width=30,
                     value=val,  
                     padx=10,  
                     variable=var,  
                     command=my_choice)
    rb.pack(anchor=W)

mainloop()