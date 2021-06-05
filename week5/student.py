#import Tkinter
from tkinter import *
#Create a window named 'window'
window = Tk()
#Set your window title to 'Animal Window'
window.title("animal window")
# Set the window geometry to 400x300
window.geometry("400x300+5+5")

#Create a StringVar named animal
animal = StringVar()

#Create a StringVar called var
var = StringVar()

#Create a label to show our Selected option and add it to the window with .pack(), set the textvariable to animal
label = Label(window, textvariable=animal)#v

def print_selection():
	# using the StringVar.set() method set the label to "You have selected " + animal name 
	animal.set("You have seleted " + var.get())
    
		
#Create a button that calls print_selection when pressed, and pack it
biuton = Button(window, text="Print your choice", command=print_selection)#v

#Create a Radiobutton widget. It should have the text "Doge", variable as var, and value as "Doge"
doge = Radiobutton(window, text="Doge", variable=var, value="Doge")

#Create a Radiobutton widget. It should have the text "Grumpy Cat", variable as var, and value as "Grumpy"
grumpyCat = Radiobutton(window, text="Grumpy Cat", variable=var, value="Grumpy")

#Create a Radiobutton widget. It should have the text "Nyan Cat", variable as var, and value as "Nyan"
nyanCat = Radiobutton(window, text="Nyan Cat", variable=var, value="Nyan")

label.pack()
biuton.pack()

doge.pack()
grumpyCat.pack()
nyanCat.pack()

#Start the mainloop
window.mainloop()