import pygame
from settings import *
import math
from player_config import PlayerConfig
from bullet import Bullet
from enemy import Enemy 

class Move():
    def __init__(self, mode: str = 'MENU'):
        self.mode = mode
        self.score = 0
    
    def isCollision(self, enemy, bullet):
        distance = math.sqrt((enemy.X - bullet.X) ** 2 + (enemy.Y - bullet.Y) ** 2)
        if distance < 30:
            return True
        else:
            return False

    def coliep(self, x, y, z, k):
        d = math.sqrt((x - z) ** 2 + (y - k) ** 2)
        if d < 27:
            return True
        else:
            return False
    
    def add_score(self):
        self.score += 1
    
    def restart(self):
        self.mode = 'MENU'
        self.score = 0
        return PlayerConfig(), Enemy(), Bullet()
    
    def change_mode(self, new_mode: str):
        ## MENU, OPT, RES, CSS, NAVE, MONSTER, BALA, GAMEOVER, GAME
        self.mode = new_mode