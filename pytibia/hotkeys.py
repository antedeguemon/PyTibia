#!/usr/bin/python
from memory import memory

HK_F1 = '85f43e0'
HK_F6 = '85f43f4'
HK_CTRL_F12 = '85f446c'

class Hotkeys:
	def __init__(self, pid):
		self.memory = memory(pid)

	def set(self, item_id):
		self.memory.write(HK_F6, str(item_id))

	def get(self):
		return self.memory.read(HK_F6)