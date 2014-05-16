from memory import memory
from operator import xor

# player stats
XOR_ADDR = '84a2cc8'
HP_ADDR = '849d870'	
MAX_HP_ADDR = '849d874'
MP_ADDR = '84a2c8c'
MAX_MP_ADDR = '84a2c88'

# player location
NOW_Y = '84a24e0' # +4 bytes
NOW_X = '84a24e4'
NOW_Z = '84a24e8' # NOW_Y + 8 bytes

# client addrs
FLAGS = '84a2cbf'
DIALOG = '85f5190'
MOUNT_ID = '8460f18'

class player:
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

	def get_x(self):
		return int(self.memory.read(NOW_X))

	def get_y(self):
		return int(self.memory.read(NOW_Y))

	def get_z(self):
		return int(self.memory.read(NOW_Z))

	def get_location(self):
		return [self.get_x(), self.get_y(), self.get_z()]

	def get_stats(self):
		# from arrowbot!
		flags = int(self.memory.read(FLAGS))

		is_pz = False
		is_battle = False
		is_hasted = False
		is_paralyzed = False		
		is_manash = False
		is_burning = False
		is_drunk = False
		is_electr = False
		is_poisoned = False

		if flags >= 16384:
			is_pz = True
			flags = flags - 16384
		if flags >= 8182:
			is_pz = True
			flags = flags - 8182
		if flags >= 128:
			is_battle = True
			flags = flags - 128
		if flags >= 64:
			is_hasted = True
			flags = flags - 64
		if flags >= 32:
			is_paralyzed = True
			flags = flags - 32
		if flags >= 16:
			is_manash = True
			flags = flags - 16
		if flags >= 8:
			is_drunk = True
			flags = flags - 8
		if flags >= 4:
			is_electr = True
			flags = flags - 4
		if flags >= 2:
			is_burning = True
			flags = flags - 2
		if flags >= 1:
			is_poisoned = True
			flags = flags - 1
		return [is_pz, is_battle, is_hasted, is_paralyzed, is_manash, is_drunk, is_electr, is_burning, is_poisoned]

	def in_pz(self):
		return self.get_stats()[0]
