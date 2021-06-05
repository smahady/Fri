# Step1: import tkinter
from tkinter import *

# Step2: Create a main window named 'window'
window = Tk()

# Step3: Set window title named 'My Window'
window.title("My Window")

# Step4: Set window geometry to 400x300
window.geometry("400x300+5+5")

# Step5: create a StringVar named var1:
var1 = StringVar()

# Step6: create a label to show the string variable (use textvariable as an option for the Label), and use the .pack() method for the Label
label = Label(window, textvariable = var1)

def print_selection():
	# Step15: get the indexes of the selected element
	var = lb.curselection()

	# Step16: use Listbox.get() to get the contents of the selected element
	var3 = lb.get(var)

	#Step 17: Use StringVar.set() to set the value from Step 8 to the label
	var1.set(var3)


# Step7: create and place a button that executes the print_select() function when pressed
button = Button(window, text="print selection", command=print_selection)

#Step8: Make a StringVar() named var2
var2 = StringVar()

#Step9: Add four elements to var2 using its .set() method
var2.set(("Dude","Bro","Bruh","Yo","Oi"))

#Step10: Create a Listbox, set its listvariable to var2
lb = Listbox(window, listvariable=var2)

#Step11: Create a list with 4 elements called myList
myList_items = ["Oh my god!","What the...","Huh?","Shiza!","Whaddaya mean?","Dude!"]

#Step12: using a for loop, add myList to the Listbox (hint: use the .insert method)
for item in myList_items:
	lb.insert(END, item)

#Step13: add the ListBox to the window using the .pack() method
lb.pack()
button.pack()
label.pack()

#Step14: Start the window's main loop
window.mainloop()