#!/usr/bin/python
from pytibia.tibia import Tibia
from pytibia.player import player
from pytibia.battle import battle
import time

tibia = Tibia()
player = player(tibia)
battle = battle(tibia)

while True:
	if player.mp() > 40:
		if player.hp() < 200:
			battle.window.send_text('exura gran')
	time.sleep(3)
