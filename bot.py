from player import Player
from tibia import Tibia
from hotkeys import Hotkeys

game = Tibia()
player = Player(game)
hotkeys = Hotkeys(game)
hotkeys.set(3028)
