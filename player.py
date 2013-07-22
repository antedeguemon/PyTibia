from memory import memory
from operator import xor

XOR_ADDR = '84a2cc8'
HP_ADDR = '849d870'	
MAX_HP_ADDR = '849d874'
MP_ADDR = '84a2c8c'
MAX_MP_ADDR = '84a2c88'

class Player:
	def __init__(self, pid):
		self.memory = memory(pid)

	def hp(self):
		return int(xor(self.memory.read(HP_ADDR), self.memory.read(XOR_ADDR)))

	def hp_max(self):
		return int(xor(self.memory.read(MAX_HP_ADDR), self.memory.read(XOR_ADDR)))

	def mp(self):
		return int(xor(self.memory.read(MP_ADDR), self.memory.read(XOR_ADDR)))

	def mp_max(self):
		return int(xor(self.memory.read(MAX_MP_ADDR), self.memory.read(XOR_ADDR)))