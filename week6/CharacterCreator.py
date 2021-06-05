# import tkinter
from tkinter import *

# main a window
window = Tk()

# make a StringVar for your Radiobutton
var1 = StringVar()

#Make three IntVar's for your Checkbutton
int1 = IntVar()
int2 = IntVar()
int3 = IntVar()

def createCharacter():
	# print the values from the Radiobuttons, the Checkbuttons, and the Scale to the console
	print(var1.get() + str(int1.get()) + " " + str(int2.get()) + str(int3.get()) + str(sc.get()))

# make three radio buttons with whatever options you like
rb1 = Radiobutton(window, text="option 1", variable=var1, value="option 1")
rb2 = Radiobutton(window, text="option 2", variable=var1, value="option 2")
rb3 = Radiobutton(window, text="option 3", variable=var1, value="option 3")

# make three checkbuttons with whatever options you like
ck1 = Checkbutton(window, text="Check 1", variable=int1)
ck2 = Checkbutton(window, text="Check 2", variable=int2)
ck3 = Checkbutton(window, text="Check 3", variable=int3)

# make a Scale widget
sc = Scale(window, from_=0, to=100)

# Make a button to call createCharacter
bt = Button(window, text="Create Character Output", command=createCharacter)

#Start your mainloop
rb1.pack()
rb2.pack()
rb3.pack()

ck1.pack()
ck2.pack()
ck3.pack()
sc.pack()
bt.pack()

window.mainloop()