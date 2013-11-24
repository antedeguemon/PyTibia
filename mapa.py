from window import window
from tibia import Tibia
from time import sleep
ZOOM_OFFSET_Y = [80, 100]
ZOOM_OFFSET_X = 40
MAP_CENTER_X = 112

class mapa:
	def __init__(self, pid):
		self.window = window(pid)
	def zoom(self, num):
		# zoom addr is fucking hard to get, so...
		for i in range(3):
			self.window.mouse_click((int(self.window.get_size()[0]) - ZOOM_OFFSET_X), ZOOM_OFFSET_Y[0])
		for i in range(num):
			self.window.mouse_click((int(self.window.get_size()[0]) - ZOOM_OFFSET_X), ZOOM_OFFSET_Y[1])
		#sleep(1)
	def center(self):
		return [(int(self.window.get_size()[0]) - MAP_CENTER_X), 79]

	def walk(self, now, goto):
		x = (now[0]-goto[0])
		y = (now[1]-goto[1])
		y = self.center()[1] - y
		x = self.center()[0] - x
		self.window.mouse_click(x, y)