import time

from Screen import Screen
from Sprite import Sprite
from time import sleep

player = Sprite("player",100,100,25, 25, -3,5)
opponent = Sprite("opponent",50,200, 30, 30, 6,-3)
screen = Screen(400, 400)

while True:
    player.update(screen)
    opponent.update(screen)
    time.sleep(0.5)