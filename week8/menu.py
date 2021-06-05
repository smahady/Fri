from tkinter import *

window = Tk()

window.title("Menu Practice")

window.geometry('400x300')


def new():
	print("New File Created!")

def menuopen():
	print("Select file to open.")

# define a main menu
menu_all = Menu(window)

# define a child menu 'menu_file' which belongs to the main file 'menu_all'
menu_file = Menu(menu_all, tearoff=0)
# add child option 'flie' in the main file 'menu_all' 
menu_all.add_cascade(label="File", menu=menu_file) 

menu_file.add_command(label="New", command=new)   # add buttons to the child menu
menu_file.add_command(label="Open", command=menuopen)  #add a command here
menu_save = Menu(menu_file, tearoff=0)
menu_save.add_command(label="Save All")
menu_file.add_cascade(label="Save", menu=menu_save)
menu_file.add_separator()  # add a seperator
menu_file.add_command(label="Exit")

#menu_help = Menu(menu_all, tearoff=0)
#menu_all.add_cascade(label='Help', menu=menu_help)  

#menu_help.add_command(label='Help')
#menu_help.add_command(label='About')

window.config(menu=menu_all)  #  config the menu to the main window

window.mainloop()  