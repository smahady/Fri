from Scene import Scene
from Sprite import Sprite
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
		self.spaceship = Sprite(self, "spaceship100.png", 100, 93)
		self.spaceship.y = 100
		self.spaceship.boundAction = Scene.BOUNCE
		self.spaceship.dx = 1
		
	def updateGame(self):
		#print("My Update")
		self.spaceship.update()

myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())