from tkinter import *

window = Tk()

window.title("LabelFrame Demo 4")

group = LabelFrame(window, text="What do you like to eat?", font=('Arial', 16), padx=5, pady=5)
group.pack(padx=10, pady=10)

var = IntVar()
rb1 = Radiobutton(group, text="ice-cream", variable=var, value=1).pack(anchor="w")
rb2 = Radiobutton(group, text="apple", variable=var, value=2).pack(anchor="w")
rb3 = Radiobutton(group, text="wood", variable=var, value=3).pack(anchor="w")

window.mainloop()