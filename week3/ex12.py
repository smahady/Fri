from tkinter import *

# Step1: Create a main window named 'window'
window = Tk()
# Step2: Set window title named 'My Window'
window.title("My Window")
# Step3: Set window size and position
window.geometry("50x50+5+5")
# Step4: Create 'Entry' widgets
entry = Entry(window, show=None)
# Step5: Set the main window loop

entry.pack()
window.mainloop()
