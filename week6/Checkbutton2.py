from tkinter import *

window = Tk()

window.title("Checkbutton Demo 2")

window.geometry('400x300')

lbl = Label(window, text="Empty",
            font=('Arial', 16),
            bg='yellow', fg='blue',
            width=24, height=2)
lbl.pack()


# define the trigger function
def print_selection():
    if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0):  # none of them are selected
        lbl.config(text="I do not love these")
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0):  # 1st only
        lbl.config(text="I love only Python")
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0):  # 2nd only
        lbl.config(text="I love only JavaScript")
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1):  # 3rd only
        lbl.config(text="I love only C++")
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 0):  # 1st and 2nd
        lbl.config(text="I love Python and JavaScript")
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 1):  # 1st and 3rd
        lbl.config(text="I love Python and C++")
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 1):  # 2nd and 3rd
        lbl.config(text="I love JavaScript and C++")
    else:
        lbl.config(text='I love these all')  # all of them are selected


# define 3 integer variabbles to store the return value
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

# create 3 checkbuttons
cb1 = Checkbutton(window, text='Python',
                  variable=var1,
                  onvalue=1, offvalue=0,
                  command=print_selection)
cb1.pack()

cb2 = Checkbutton(window, text="JavaScript",
                  variable=var2,
                  onvalue=1, offvalue=0,
                  command=print_selection)
cb2.pack()

cb3 = Checkbutton(window, text="C++",
                  variable=var3,
                  onvalue=1, offvalue=0,
                  command=print_selection)
cb3.pack()

window.mainloop()