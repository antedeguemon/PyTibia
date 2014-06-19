#!/usr/bin/python
import subprocess 
import binascii
class memory:
	def __init__(self, pid):
		self.pid = pid
	def readInt(self, addr):
		return int(read(addr))

	def read(self, addr):
		return int(subprocess.Popen(['readmem', str(self.pid), (addr)], stdout=subprocess.PIPE).communicate()[0])

	def write(self, addr, value):
		return subprocess.Popen(['writemem', str(self.pid), (addr), str(value)], stdout=subprocess.PIPE).communicate()[0]