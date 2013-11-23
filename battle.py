from window import window
from PIL import Image
import pygame
import time


BATTLE_OCR_START = '60,60,60;57,57,57;163,163,163;147,147,147;59,59,59;67,67,67;173,173,146;182,172,99;158,135,39;69,65,56;61,61,61;45,45,45;'
BATTLE_OCR_END = '24,24,24;57,58,58;75,76,76;55,55,55;53,54,53;41,41,41;40,40,40;120,120,120;'
BORDER_SIZE = 1
MIN_BATTLE_SIZE = 64  
BATTLE_BORDER = 11

class battle:
	def __init__(self, pid):
		self.window = window(pid)
	def monsters(self):
		WINDOW_STATUS = 1
		self.window.get_battle()
		im = Image.open('tmp.png').convert('RGB')
		size = self.window.get_size()
		print self.window.is_maximized()
		if int(self.window.is_maximized()) < 1:
			WINDOW_STATUS = 0
		
		battle_start_x = int(size[0])-(164-(BORDER_SIZE*WINDOW_STATUS))	
		battle_end_x = int(size[0])-(164-(BORDER_SIZE*WINDOW_STATUS))
		battle_start_y = 0
		battle_end_y = 0

		checksum = ''
		for y in range(0, int(size[1])):
			color = im.getpixel(((int(size[0])-(164-(BORDER_SIZE*WINDOW_STATUS))), y))
			checksum = checksum + str(color[0]) + ',' + str(color[1]) + ',' + str(color[2]) + ';'
		
		if BATTLE_OCR_START in checksum:
			battle_start = checksum.split(BATTLE_OCR_START)
			battle_start_y = len(battle_start[0].split(';'))
			if BATTLE_OCR_END in battle_start[1]:
				block_size = len(battle_start[1].split(BATTLE_OCR_END)[0].split(';'))
				battle_end_y = block_size + battle_start_y
			try:
				if block_size < MIN_BATTLE_SIZE:
					block_size = (MIN_BATTLE_SIZE+5) - block_size 
					self.window.mouse_down(battle_end_x, battle_end_y+5, battle_end_x, battle_end_y+block_size)
					self.monsters()
				else:
					self.window.get_monsters(block_size - BATTLE_BORDER, size[0], battle_start_y + BATTLE_BORDER)

			except UnboundLocalError:
				# minimized battle
				self.window.mouse_click(battle_start_x, battle_start_y)
				self.window.mouse_click(battle_start_x, battle_start_y)
				self.monsters()
		else:
			self.window.mouse_click(int(size[0])-131, 350)
			self.monsters()
