from pytibia.tibia import Tibia
from pytibia.player import player
import time

tibia = Tibia()
player = player(tibia)

while True:
	if player.mp() > 40:
			battle.window.send_text('exura')
	time.sleep(10)
