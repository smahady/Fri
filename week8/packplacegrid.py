from tkinter import *

window = Tk()
window.geometry('400x400')

def hellp() :
	print("hellp")

button1 = Button(window, text = "Click Me!", command=hellp)
button1.place(x=10, y=10)

label1 = Label(window, text = "Dude!!!")
label1.place(x=30, y=30)

button2 = Button(window, text = "Click Me!", command=hellp)
button2.place(x=50, y=50)

label2 = Label(window, text = "Dude!!!")
label2.place(x=70, y=70)

window.mainloop()