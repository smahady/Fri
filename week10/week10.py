import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Scene(QWidget):
	def __init__(self):
		super().__init__()


app = QApplication(sys.argv)

window = QWidget()
label = QLabel(window)
label.setText("Hello world")
window.show()
label.move(100,100)

sys.exit(app.exec_())



class Animal:
	classVariable = 1
	def __init__(self):
		print("Initializing!")
		self.x = 0
		self.y = 0
	def bark(self):
		print("Woof")
		print(self.x)

class Doge(Animal):

	def bark(self):
		print("Bark!")
		print(self.x)		


doge = Doge()
frank = Doge()
frank.x = 100
doge.bark()
frank.bark()

class Fiveseven:
	def __init__(self):
		print("Initializing!")
	def hi(self):
		print("hi")

class People(Fiveseven):
	def hi(self):
		print("hello")

fiveseven = Fiveseven()
dude = Fiveseven()
dude.x=100
fiveseven.hi()
dude.hi()
print(dude.x)