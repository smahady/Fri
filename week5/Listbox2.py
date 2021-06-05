from tkinter import *

top = Tk()

def Press():
	var = Lb1.curselection()
	print(var)

button = Button(top, text="Press Me", command=Press)
button.pack()

Lb1 = Listbox(top)
Lb1.insert(0, "Python")
Lb1.insert(1, "Perl")
Lb1.insert(2, "C")
Lb1.insert(3, "PHP")
Lb1.insert(4, "JSP")
Lb1.insert(5, "Ruby")

Lb1.delete(4)

Lb1.pack()
top.mainloop()