import subprocess
import re

class window:
	def __init__(self, pid):
		self.pid = pid
		self.window = subprocess.Popen(['xdotool', 'search', '--name', 'Tibia Linux'], stdout=subprocess.PIPE).communicate()[0].replace("\n", '')
		subprocess.Popen(['xdotool', 'windowmove', self.window, '0', '0'], stdout=subprocess.PIPE).communicate()
		self.title = self.get_title()

	def get_size(self):
		pids = subprocess.Popen(['wmctrl', '-l', '-p', '-G'], stdout=subprocess.PIPE).communicate()[0].split("\n")
		for pid in pids:
			if 'Tibia Linux' in pid:
				size =  pid.split("N/A")[0].split(' 37')[1].strip().split(' ')
				
				return [size[0], size[(len(size)-1)]]
				pass
	
        def is_maximized(self):
                pids = subprocess.Popen(['wmctrl', '-l', '-p', '-G'], stdout=subprocess.PIPE).communicate()[0].split("\n")
                for pid in pids:
                        if 'Tibia Linux' in pid:
                                status = pid.split("N/A")[0].split(' 37')[0].strip().split(' ')
                                return status[(len(status)-1)]
                                pass


	def mouse_click(self, x, y):
		# mousemove restore
		subprocess.Popen(['xdotool', 'mousemove', str(x), str(y), 'click', '--window', self.window, '1', 'mousemove', 'restore'], stdout=subprocess.PIPE).communicate()
	
        def mouse_down(self, x, y, x_resize, y_resize):
                subprocess.Popen(['xdotool', 'mousemove', str(x), str(y), 'mousedown', '--window', self.window, '1', 'mousemove', str(x_resize), str(y_resize), 'mouseup', '--window', self.window, '1'], stdout=subprocess.PIPE).communicate()
	
	def get_title(self):
		pids = subprocess.Popen(['wmctrl', '-l', '-p', '-G'], stdout=subprocess.PIPE).communicate()[0].split("\n")
		for pid in pids:
			if 'Tibia Linux' in pid:
				title = pid.strip().split('N/A')
				title = title[(len(title)-1)].strip()
				pass
		return title

	def get_battle(self):
		return subprocess.Popen(['import', '-frame', '-window', self.title, 'tmp.png'], stdout=subprocess.PIPE).communicate()

	def get_monsters(self, block_size, x, y):
		return subprocess.Popen(['import', '-frame', '-window', self.title, '-crop','150x'+str(block_size)+'+' +str(int(x)-170)+ '+' + str(y), 'tmp.png'], stdout=subprocess.PIPE).communicate()

