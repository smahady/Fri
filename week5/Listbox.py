from tkinter import *

# Step1: Create a main window named 'window'
window = Tk()

# Step2: Set window title named 'My Window'
window.title('Listbox')

# Step3: Set window size and position
window.geometry('400x300+1000+150')

list_items = ['item1', 'item2', 'item3', 'item4']

# Step5: Create a variable as the value of the listbox
var = StringVar()
var.set(list_items)  # Set value for variable 'var'

# Step4: Create a 'Listbox' widgets
lb = Listbox(window, listvariable=var, selectmode=SINGLE)

lb.pack()

# Step5: Set the main window loop
window.mainloop()