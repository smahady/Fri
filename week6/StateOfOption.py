from tkinter import *

window = Tk()

window.title("State of Option")

var1 = IntVar()
check1 = Checkbutton(window,
                     text="Disabled",
                     variable=var1,
                     state='disabled')   # normal, active, disabled
# check1.select()  # select/deselect
check1.grid(column=0, row=1, sticky=W)  # sticky=W/E/N/S   (west, east, north, south)
var2 = IntVar()
check2 = Checkbutton(window,
                     text="UnChecked",
                     variable=var2)
check2.deselect()  # select/deselect
check2.grid(column=1, row=1, sticky=W)  

var3 = IntVar()
check3 = Checkbutton(window,
                     text="Enabled",
                     variable=var3)
check3.select()
check3.grid(column=2, row=1, sticky=W)  

window.mainloop()