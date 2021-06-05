from random import *
# import tkinter
from tkinter import *

# make a Tk window called window
window = Tk()

# set window title to "Guess a Number Game"
window.title("Guess a Number Game")

# Set window geometry to 600x400
window.geometry("600x400+5+5")

# Create an IntVar named myNum
myNum = IntVar()

# Create a variable called guesses and set it to 0
guesses = 0

# make a random number
secretNumber = randint(1,100)


#Create a label named myLabel, and set its text to "Please enter a number", and add it to our window 
myLabel = Label(window, text="Please enter a number")

# create myFont
myFont = ("Arial", 22, "normal")

def clear():
	# use the canvas.create_rectangle method to fill the entire canvas white
	myCanvas.create_rectangle(0,0,600,400, fill="white")

def makeGuess():
	# global guesses, and then increment 1
	global guesses
	guesses += 1

	# use the IntVar.get() method with our IntVar, myNum, and assign it to the variable ourNumber
	ourNumber=myNum.get()

	# if ourNumber is larger than secretNumber, use the canvas.create_text() method (at 300,50) to say that the value of ourNumber "was too big". Set the font to myFont. example: "99 was too big"
	if ourNumber > secretNumber:
		clear()
		myCanvas.create_text(300,50, text=str(ourNumber) + " is too big.", font=myFont)
		

	# if ourNumber is smaller than secretNumber, use the canvas.create_text() method (at 300,50) to say that ourNumber "was too small". Set the font to myFont. Example: "1 was too small" > < ==
	if ourNumber < secretNumber:
		clear()
		myCanvas.create_text(300,50, text=str(ourNumber) + " is too small.", font=myFont)


	# if ourNumber is equal to secretNumber, use the text.create() method (at 300,50) to say "You win it was" and ourNumber. Set the font to myFont. Example: "You win it was 56". 
	if ourNumber == secretNumber:
		clear()
		myCanvas.create_text(300,50, text="You won! The number is " + str(ourNumber), font=myFont)

		# Use the widget.config()'s state option to disable the widget in the above line
		myButton.config(state="disabled")




# make an Entry named myEntry. Set its textvariable option to myNum, and add it to the window

myEntry = Entry(window, textvariable=myNum)
myEntry.pack()

#make a button named myButton with the text "Guess", its command set to makeGuess, and add it to the window
myButton = Button(window, text="Guess", command=makeGuess)
myButton.pack()

# Make a canvas called myCanvas. It should have a white background color, a width of 598, and a height of 300.
myCanvas = Canvas(window, width=598, height=300, bg="white")

# use the canvas.create_text() method (at 300,50) to say "Guess a number between 1 and 100". Set the font to myFont. 
myCanvas.create_text(300,50, text="Guess a number between 1 and 100.", font=myFont)


# Add the canvas to the window
myCanvas.pack()


# Start the window's mainloop
window.mainloop()