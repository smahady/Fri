# Create a String type variable [var] and use it to receieve the content from hit_me function. 
var = StringVar()
var.set("Empty")

lbl = Label(window,
            textvariable=var,
            font=('Arial', 20),
            fg='white', bg='blue',
            height=2, width=16)
lbl.pack()


#define a function for the command of Button
on_click = False


def click_me():
    global on_click

    if not on_click:
        on_click = True
        var.set('You click me now!')
    else:
        on_click = False
        var.set('Empty')


btn = Button(window, text='Click Me', height=2, width=12, command=click_me)
btn.pack()

window.mainloop()