
from tkinter import *

window = Tk()

window.title("Rainbow frame")

# reate a set of frames, colored by 7 colors
color = ['#FF0000',
         '#FF8000',
         '#FFFF00',
         '#00FF00',
         '#00FFFF',
         '#0000FF',
         '#8000FF']
for fm in color:
    Frame(height=50, width=400, bg=fm).pack()

window.mainloop()