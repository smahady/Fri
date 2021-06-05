from tkinter import *

window = Tk()

window.title("Canvas Demo 2")

canvas_width = 200
canvas_height = 100

cv = Canvas(window,
            width=canvas_width, height=canvas_height)
cv.pack()

cv.create_rectangle(50, 20, 150, 80, fill="#4169E1")
cv.create_rectangle(65, 35, 135, 65, fill="yellow")
cv.create_line(0, 0, 50, 20, fill="#4169E1", width=3)
cv.create_line(0, 100, 50, 80, fill="#4169E1", width=3)
cv.create_line(150,20, 200, 0, fill="#4169E1", width=3)
cv.create_line(150, 80, 200, 100, fill="#4169E1", width=3)

window.mainloop()