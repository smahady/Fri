from tkinter import *

# # Step1: Create a main window named 'window'
window = Tk()

# Step2: Set window title named 'My Window'
window.title('My Window')

# Step3: Set window size and position
window.geometry('400x300+1000+150')

# Step4: Create a 'Text' widgets

text = Text(window, font=('Arial', 16), height=3)
text.insert('end', 'b')
text.pack()



# Step5: Set the main window loop
window.mainloop()