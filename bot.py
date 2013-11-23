from player import Player
from tibia import Tibia
from mapa import mapa
import time
from  battle import battle

game = Tibia()
player = Player(game)
battle = battle(game)
#mapa = mapa(game)

location = player.get_location()
print 'START: '
print  location
print
#y_goto = 32818
#print float(location[1]-y_goto)
#mapa.zoom(1)
print battle.monsters()

#mapa.walk(location, [33201, 32818])
#while True:
#	location = player.get_location()
#	if location[0] == 33201:
#		if location[1] == 32818:
#			mapa.walk(location, [33200, 32804])
#	time.sleep(1)
