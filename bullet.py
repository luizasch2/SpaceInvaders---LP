import pygame
from settings import *

class Bullet():
    global bullet_state, bulletX, bulletY, bullet_sound
    # Bullet: stopped --> não consegue ver na tela
    # Bullet: fire --> atirando (movendo)
    def __init__(self, image_srg: str = './img/001-bullet.png', 
        x_position: float = 0, y_position: float = y_pix - 120, state: str = 'stopped'):
        self.image = pygame.image.load(image_srg)
        self.X = x_position
        self.Y = y_position
        self.state = state
    
    def change_position(self, new_x, new_y):
        self.X = new_x
        self.Y = new_y
    
    def change_image(self, image_src: str):
        self.image = pygame.image.load(image_src)
    
    def change_state(self, new_state):
        self.state = new_state
    
    def blit(self, x, y):
        screen.blit(self.image, (x, y))
    
    def config_enemy_image(self, image_src: str = './img/enemy_bullet.png'):
        self.change_image(image_src)
    
    def fire(self, x, y):
        self.change_state('fire')
        self.blit(x + 16, y + 10)