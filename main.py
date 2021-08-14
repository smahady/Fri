from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer
import sys
from Sprite import Sprite
from Scene import Scene


		

class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
    # Sprite.__init__(self, thisScene, imageFile, xSize, ySize)
		self.sprite = Sprite(self, "spaceship100.png", 100,93)
		self.spaceship100.y=200
		self.spaceship100.dx=1
	
	def updateGame(self):
		print("My Update")
		self.sprite.update()

	



app = QApplication(sys.argv) #QApplication.__init__(self, sys.argv)
scene = Game()
scene.show()
sys.exit(app.exec_())