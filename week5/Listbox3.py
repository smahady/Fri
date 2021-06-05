from tkinter import *

window = Tk()

window.title("Listbox2")

window.geometry("400x300+1000+150")

# create a listbox
lb = Listbox(window,
             selectmode=BROWSE)  # 选择模式:MULTIPLE; BROWSE(single); EXTENDED(allowshift and ctrl).


# create a list
list_items = ["item1", "item2", "item3", "item4"]

# add some choices in the list
for item in list_items:
    lb.insert(END, item)  # in order

# insert to the beginning
lb.insert(ACTIVE, "ACTIVE, inserted to the beginning")

# insert'first' to the position 1
lb.insert(1, "First")

# insert a string list as an element
lb.insert(END, ["Hello world!", "Hello teacher!"])

# insert an integer list as an element
lb.insert(END, [1, 2, 3, 4])

# delete(param1,param2): delete all the elements from param1 to param2. (if there's only param1, delete the element on param1 position) 
lb.delete(0, 1)

# select_set(param1,param2): select all the elements from param1 to param2. (if there's only param1, select the element on param1 posisiton)
lb.select_set(3, 4) 

# select_clear(param1,param2):clear the selections of all the elements from param1 to param2. (if there's only param1, clear the selection of the element on param1 posisiton)
lb.select_clear(3)

# size() returns how many elements does the listbox have
print(lb.size())

# get(param1,param2) returns the list of elements from param1 to param2
print(lb.get(2, 3))

# return the selected positions（not the elements)
print(lb.curselection())

# return if an element is selected
print(lb.selection_includes(3))

lb.pack()

window.mainloop()