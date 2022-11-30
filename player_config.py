import pygame
from settings import *

class PlayerConfig():
    global screen
    def __init__(self, image_src: str = './img/001-nave-espacial.png', x_position: float = x_pix/2 - 30,
                y_position: float = y_pix - 120):
        self.image = pygame.image.load(image_src)
        self.X = x_position
        self.Y = y_position
    
    
    def change_position(self, new_x):
        self.X = new_x
    
    def change_image(self, image_src: str):
        self.image = pygame.image.load(image_src)
    
    def blit(self, x, y):
        screen.blit(self.image, (x, y))