from player import player
from tibia import Tibia
from mapa import mapa
import time
from  battle import battle

game = Tibia(0, 26834)
player = player(game)
battle = battle(game)
mapa = mapa(game)

monsters = battle.monsters()
for x in range(0, len(monsters)):
	if monsters[x] == 'rotworm' or monsters[x] == 'rat':
		battle.attack(x)

location = player.get_location()
#mapa.walk(location, [32351, 32216])
#	if location[0] == 33201:
#		if location[1] == 32818:
#			mapa.walk(location, [33200, 32804])
#	time.sleep(1)
