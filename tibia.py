import subprocess
class Tibia:
	def __init__(self, client = 0, pid = 0):
		self.client_pid = None
		if pid != 0:
			self.client_pid = pid
		self.client = client
	def pid(self, pid = None):
		if pid == None:
			return int(subprocess.Popen(['pidof', 'Tibia'], stdout=subprocess.PIPE).communicate()[0].strip().split(' ')[self.client])
		else:
			self.client_pid = pid
			return int(pid)
	def __str__(self):
		if self.client_pid == None:
			return str(self.pid())
		else:
			return str(self.client_pid)
