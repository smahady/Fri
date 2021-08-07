from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer
import sys

# Scene has now INHERITED QWidget
# Scene IS A QWidget
class Scene (QWidget) :
	def __init__(self, x=600, y=400, speed=200):
		super().__init__()
		self.setGeometry(50,50,x,y)
		self.timer=QTimer()
		self.timer.timeout.connect(self.updateTask)
		self.speed = speed

	
	def start(self):
		self.timer.start(self.speed)
		

	def stop(self):
		self.timer.stop()

	def updateTask(self):
		self.update()

	def paintEvent(self, event):
		self.updateGame()

	def updateGame(self):
		pass
		

class Game(Scene):
	def __init__(self):
		super().__init__()
	
	def updateGame(self):
		print("My Update")
	


app = QApplication(sys.argv)
scene = Game()
scene.show()
sys.exit(app.exec_())