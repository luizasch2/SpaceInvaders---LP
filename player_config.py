import pygame
from settings import *
from bullet import Bullet
from pygame import mixer

class PlayerConfig():
    global screen
    def __init__(self, image_src: str = './img/001-nave-espacial.png', x_position: float = x_pix/2 - 30,
                y_position: float = y_pix - 120):
        self.image = pygame.image.load(image_src)
        self.X = x_position
        self.Y = y_position
    
    def movimento(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.X -= 1*(x_pix*y_pix)/(800*600)
        if keys[pygame.K_RIGHT]:
            self.X += (x_pix*y_pix)/(800*600)
    
    def fire(self, bullet: Bullet):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bullet.change_state('fire')
            bullet.change_position(self.X, self.Y)
            bullet.blit(self.X, self.Y)
            bullet_sound = mixer.Sound('./sounds/laser.wav')
            bullet_sound.play()
            
    def change_position(self, new_x):
        self.X = new_x

    def change_spawn(self, new_x, new_y):
        self.X = new_x
        self.Y = new_y
    
    def change_image(self, image_src: str):
        self.image = pygame.image.load(image_src)
    
    def blit(self, x, y):
        screen.blit(self.image, (x, y))