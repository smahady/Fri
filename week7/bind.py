# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
from tkinter import *
from tkinter.ttk import *
 
# creates tkinter window or root window
root = Tk()
root.geometry('200x100')
 
# function to be called when mouse enters in a frame
def enter(event):
    print('Mouse enter at x = % d, y = % d'%(event.x, event.y))
 
# function to be called when when mouse exits the frame
def exit_(event):
    print('Mouse leave at x = % d, y = % d'%(event.x, event.y))
 
def button(event):
		print('Button at x = % d, y = % d'%(event.x, event.y))

def motion(event):
	print('Mouse motion x = % d, y = % d'%(event.x, event.y))

# frame with fixed geomerty
frame1 = Frame(root, height = 100, width = 200)
 
# these lines are showing the
# working of bind function
# it is universal widget method
#frame1.bind('<Enter>', enter)
#frame1.bind('<Leave>', exit_)
#frame1.bind('<Button>', button)
frame1.bind('<Motion>', motion) 

frame1.pack()
 
root.mainloop()