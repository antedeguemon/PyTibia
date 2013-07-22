import subprocess
class Tibia:
	def __init__(self, client = 0):
		self.client = client
	def pid(self):
		return int(subprocess.Popen(['pidof', 'Tibia'], stdout=subprocess.PIPE).communicate()[0].strip().split(' ')[self.client])
	def __str__(self):
		return str(self.pid())