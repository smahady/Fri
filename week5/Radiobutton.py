from tkinter import *

window = Tk()

window.title("Radiobutton Demo")

window.geometry('400x300+1000+150')

lbl = Label(window, text="Choose your animal!", font=('Arial', 16))
lbl.pack(anchor=W)

var = StringVar()
# determine which radio button is selected by the value of the variable

rb1 = Radiobutton(window, text="Grumpy Cat", variable=var, value="Grumpy")  
rb1.pack(anchor=W)

rb2 = Radiobutton(window, text="Doge", variable=var, value="Doge")
rb2.pack(anchor=W)

rb3 = Radiobutton(window, text="Emu", variable=var, value="Emu")
rb3.pack(anchor=W)

window.mainloop()