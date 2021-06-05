from tkinter import *

window = Tk()

window.title("Scale Demo")

scale1 = Scale(window, from_=0, to=10)  # set max and min values, pay attention to 'from_'
scale1.pack()

scale2 = Scale(window, from_=0, to=100, orient=HORIZONTAL)  # Set the horizontal direction, it's vertical by default
scale2.pack()


def print_values():
    print(scale1.get(), scale2.get())


btn = Button(window,
             text="Print Values", 
             command=print_values)
btn.pack()

window.mainloop()