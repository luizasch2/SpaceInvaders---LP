import pygame
import random

enemySkin = pygame.image.load('./img/002-ghost.png')
enemySkin2 = pygame.image.load('./img/003-ghost.png')

class Enemy():
    def __init__(self,enemyX, enemyY, enemyX_change, enemyY_change, enemyImg = enemySkin):
        self.image = enemyImg
        self.enemyX = []
        self.enemyY = []
        self.enemyX_change = []
        self.enemyY_change = []
    
    def change_skin(self, skin_src: str):
        self.image = pygame.image.load(skin_src)
    
    def change_skin_hard(self, skin_src: str):
        self.image_hard = pygame.image.load(skin_src)

    def lista_inimigos(self):
        for i in range(6):
            self.enemyX.append(random.randint(0, 735))
            self.enemyY.append(random.randint(50, 150))
            self.enemyX_change.append(4)
            self.enemyY_change.append(40)


    
        