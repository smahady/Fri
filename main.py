from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer
import sys
from Sprite import Sprite
from Scene import Scene
from enum import Enum
from Block import Block

class States(Enum):
	FALLING = 0
	WALK = 1
	JUMP = 2
	STAND = 3

class Facing():
	RIGHT = 0
	LEFT = 1

class Character(Sprite):
	def __init__(self, thisScene, sprite, x, y):
		super().__init__(thisScene, sprite, x, y)
		self.stateTimer = 0
		self.setBoundAction(Scene.WRAP)
		self.stateTimer = 0		

	def update(self, offsetX = 0, offsetY = 0):
		if self.state == States.FALLING:
			if self.scene.ground.collidesWith(self):
				self.standBehavior()
		elif self.state == States.STAND or self.state == States.WALK:
			if self.scene.keysDown[Scene.K_SPACE]:
				self.jumpBehavior()
			elif self.scene.keysDown[Scene.K_RIGHT] or self.scene.keysDown[Scene.K_LEFT]:
				self.walkBehavior()
			elif self.state == States.WALK:
				if (self.facing == Facing.RIGHT) and (self.scene.keysDown[Scene.K_RIGHT] == None):
					self.standBehavior()
				if (self.facing == Facing.LEFT) and (self.scene.keysDown[Scene.K_LEFT] == None):
					self.standBehavior()
		elif self.state == States.JUMP:
			self.stateTimer = self.stateTimer - 1
			if self.stateTimer < 1:
				self.dy = self.dy * -1
				self.state = States.FALLING
		super().update(offsetX, offsetY)

	def standBehavior(self):
		self.dy = 0
		self.dx = 0
		self.state = States.STAND
		#self.pauseAnimation()	

	# override this in your Character
	def jumpBehavior(self):
		pass

	# override this in your Character
	def walkBehavior(self):
		pass			

# file - ethan_sprite.png
# width - 123
# height - 90
class Ninja(Character):
  def __init__(self, thisScene):
	  super().__init__(thisScene, "ethan_sprite.png", 123, 90)
	  self.state = States.FALLING
	  self.facing = Facing.LEFT
	  self.x = 100
	  self.y = 100
	  self.dy = 5
  def jumpBehavior(self):
      self.dy = -5
      self.state = States.JUMP
      self.stateTimer = 12
  # This should check if self.scene.keysDown[Scene.K_RIGHT]is True. If so self.facing to 0, self.setCurrentCycle to Facing.RIGHT, call the self.playAnimation method. Set the DX to a value between 0 and 10. Set a State to States.WALK
	# If not check if self.scene.keysDown[Scene.K_LEFT] is True. If so self.facing to Facing.LEFT, self.setCurrentCycle to Facing.LEFT, call the self.playAnimation method. Set the DX to a value between 0 and -10. Set a State to States.WALK    
  def walkBehavior(self):
    if self.scene.keysDown[Scene.K_RIGHT]:
		  self.facing = Facing.RIGHT
		  self.setCurrentCycle(Facing.RIGHT)
		  self.playAnimation()
	    self.dx = 5
	    self.state = States.WALK
	  elif self.scene.keysDown[Scene.K_LEFT]:
		  self.facing = Facing.Left
		  self.setCurrentCycle(Facing.Left)
		  self.playAnimation()
	    self.dx = 5
	    self.state = States.WALK




#
class Spaceship(Sprite):
	def __init__(self, thisScene):
		super().__init__(thisScene, "spaceship100.png", 100, 100)
		self.x = 300
		self.y = 100
		self.dx = 6
		self.timer = 60
		self.enemies = []

	def checkBounds(self):

		if self.drawX < 0:
			self.dx = 6
		if self.drawX > 550:
			self.dx = -6
		self.timer -= 1
		if self.timer < 1:
			self.timer = 60
			self.enemySpawn()

		for enemy in self.enemies:
			enemy.update(self.scene.offsetX, self.scene.offsetY)

	def enemySpawn(self):
		pass	


class Ground(Block):
	def __init__(self, thisScene):
		spriteMaker = [["ground.png"] ] *30
		super().__init__(thisScene, spriteMaker, 120, 40)
		self.x = 0
		self.y = 500
		

				


class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
    # Sprite.__init__(self, thisScene, imageFile, xSize, ySize)
		self.sprite = Spaceship(self)
		self.character = Ninja(self)
		self.ground = Ground(self)

		self.start()


		
	def updateGame(self):
		print("My Update")
		self.sprite.update()
		self.character.update()
		self.ground.update()
	



app = QApplication(sys.argv) #QApplication.__init__(self, sys.argv)
scene = Game()
scene.show()
sys.exit(app.exec_())