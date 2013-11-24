from pytibia.tibia import Tibia
from pytibia.battle import battle
from pytibia.player import player
from pytibia.mapa import mapa
import time

tibia = Tibia()
player = player(tibia)
battle = battle(tibia)
mapa = mapa(tibia)

waypoint = [[32370, 32213, 8], [32362, 32214, 8], [32350, 32214, 8], [32340, 32215, 8], [32331, 32215, 8], [32328, 32222, 8], [32328, 32227, 8], [32339, 32227, 8], [32339, 32238, 8], [32339, 32252, 8], [32356, 32251, 8], [32367, 32245, 8], [32369, 32239, 8], [32368, 32224, 8], [32368, 32214, 8]]

y = 0
walking = True

while True:
	if player.mp() > 40:
		if player.hp() < 200:
			battle.window.send_text('exura')
	monsters = battle.monsters()
	for x in range(0, len(monsters)):
	        if monsters[x] == 'rotworm' or monsters[x] == 'rat':
        	        battle.attack(x)
			walking = False
			break
		else:
			walking = True
	if walking == True:
		location = player.get_location()
		if location[0] == waypoint[y][0] and location[1] == waypoint[y][1]:
			y = y + 1
		if location == last_location:
			y = y + 1
		mapa.walk(location, waypoint[y])
		last_location = location
	time.sleep(3)
