from tkinter import *

class APP(Tk):
	def __init__(self):
		super().__init__()
		self.message = Message(self, text="Whoever is reading this message is looking at tk", width=100)
		self.message.pack()	# change here!


window = APP()

window.mainloop()


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Scene(QWidget):
	def __init__(self):
		super().__init__()
		self.label = QLabel(window)
		self.label.setText("Hello world")
		self.label.move()


app = QApplication(sys.argv)

window = QWidget()

window.show()


sys.exit(app.exec_())


# local
# global
# class
# instance
