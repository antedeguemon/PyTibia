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
print 'walking from: ' + str(location)
mapa.walk(location, [33201, 32818])
print battle.monsters()

