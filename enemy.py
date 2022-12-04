import pygame
from settings import *
import random

class Enemy():
    def __init__(self, skin_src: str = './img/002-ghost.png', x_position: float = random.randint(65, x_pix - 65), 
                y_position: float = random.randint(75, 150), skin_hard_src: str =  './img/003-ghost.png',
                vel: float = 0.5, state: str = 'ready'):
        ## iniciais definidos:
        ## enemySkin = pygame.image.load('./img/002-ghost.png')
        ## enemySkin2 = pygame.image.load('./img/003-ghost.png')
        self.image = pygame.image.load(skin_src)
        self.image_hard = pygame.image.load(skin_hard_src)
        self.X = x_position
        self.Y = y_position
        self.state = state
        self.vel = vel
        
    def change_skin(self, skin_src: str):
        self.image = pygame.image.load(skin_src)
    
    def change_skin_hard(self, skin_src: str):
        self.image_hard = pygame.image.load(skin_src)
    
    def change_to_skin_hard(self):
        self.image = self.image_hard
    
    def change_position(self, new_x, new_y):
        self.X = new_x
        self.Y = new_y
    
    def change_vel(self, new_vel):
        self.vel = new_vel
    
    def blit(self, x, y):
        screen.blit(self.image, (x, y))
    


    