class Animal:
	def __init__(self):
		print("Hello!")
	
	def move(self):
		print("I moved!")

class peacock(Animal):
	def __init__(self):
		super().__init__()
		self.myAttribute = 6


myPeacock = peacock()

myPeacock.move()

myPeacock.myProperty = 5

# .move(myPeacock)