#!/usr/bin/python
from window import window
from tibia import Tibia
from time import sleep

ZOOM_OFFSET_Y = [80, 100]
ZOOM_OFFSET_X = 40
MAP_CENTER_X = 112

class gmap:
	def __init__(self, pid):
		self.window = window(pid)
	def zoom(self, num):
		for i in range(3):
			self.window.mouse_click((int(self.window.get_size()[0]) - ZOOM_OFFSET_X), ZOOM_OFFSET_Y[0])
		for i in range(num):
			self.window.mouse_click((int(self.window.get_size()[0]) - ZOOM_OFFSET_X), ZOOM_OFFSET_Y[1])
	def center(self):
		return [(int(self.window.get_size()[0]) - MAP_CENTER_X), 79]

	def walk(self, now, goto):
		y = self.center()[1] - (now[1]-goto[1])
		x = self.center()[0] - (now[0]-goto[0])
		self.window.mouse_click(x, y)