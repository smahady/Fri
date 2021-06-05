from tkinter import *

window = Tk()

canvas = Canvas(window, width=400, height=200)
canvas.pack()

canvas.create_line((0, 100), (400, 100), width=5, fill="#4169E1")  #  "RoyalBlue"
canvas.create_text(200, 80, text="draw a straight line", font=("Arial", 20))


mainloop()