from tkinter import *

window = Tk()

window.title("Checkbutton Demo")

lbl = Label(window,
            text="These are multiple choices",
            font=('Arial', 16))
lbl.pack()

cb1 = Checkbutton(window,
                  text="Python",
                  font=('Arial', 16))
cb1.pack()

cb2 = Checkbutton(window,
                  text="JavaScript",
                  font=('Arial', 16))
cb2.pack()

cb3 = Checkbutton(window,
                  text="C++",
                  font=('Arial', 16))
cb3.pack()

window.mainloop()