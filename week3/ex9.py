from tkinter import *

window = Tk()

window.title("Label and Button")

window.geometry('400x300')

lbl = Label(window, text="You click me!", font=('Arial', 20), fg='white', bg='blue', height=2, width=16)
lbl.pack()

i = 0  # define a variable to count


def click_me():
    global i  # get global variable i
    i = i + 1
    print("You clicked me " + str(i) + " times!")


btn = Button(window, text='Click Me', height=2, width=12, command=click_me)
btn.pack()

window.mainloop()