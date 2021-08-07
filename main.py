from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

# Scene has now INHERITED QWidget
# Scene IS A QWidget
class Scene (QWidget) :
	def __init__(self, x=600, y=400, speed=200,):
		super().__init__()
		self.setGeometry(50,50,x,y)
	
	def start(self):
		pass
	def stop(self):
		pass

app = QApplication(sys.argv)
scene = Scene()
scene.show()
sys.exit(app.exec_())