from tkinter import *

window = Tk()

window.title("Scale Demo 2")

scale1 = Scale(window, label="Demo1",  
               from_=0, to=10,
               tickinterval=2)
scale1.set(6)
scale1.pack()

scale2 = Scale(window, label="Demo2",  #
               from_=0, to=100,
               resolution=20,  
               tickinterval=20, 
               length=300,
               orient=HORIZONTAL,
               activebackground='green')  # the color of the scale when mouse is on it
scale2.set(60)
scale2.pack()

window.mainloop()