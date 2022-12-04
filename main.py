import pygame
from pygame import mixer
import sys
import random
import math
from settings import *
from enemy import Enemy
from player_config import PlayerConfig
from bullet import Bullet
from move import Move

# inicializa o pygame   
pygame.init()

support_images = support_images_small

background = scene_config()
move = Move()
player = PlayerConfig()
bullet = Bullet()
enemies = [Enemy(random.randint(65, x_pix - 65), random.randint(75, 150)) for _ in range(num_of_enemies)]
for enemy in enemies:
    enemy.bullet = Bullet()
    enemy.bullet.config_enemy_image()

while True:
    screen.blit(background, (0, 0))
    if move.mode == 'MENU':
        background = support_images["menu"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        background = support_images["game"]
                        move.mode = 'GAME'
                if event.key == pygame.K_ESCAPE:
                    move.mode = 'OPT'

    if move.mode == 'OPT':
        background = support_images["opt"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    move.mode = 'MENU'
                if event.key == pygame.K_s:
                    move.mode = 'RES'
                if event.key == pygame.K_c:
                    move.mode = 'CSS'

    if move.mode == 'RES':
        background = support_images["res"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    move.mode = 'OPT'
                if event.key == pygame.K_1:
                    support_images = support_images_big
                    num_of_enemies = 10
                    x_pix, y_pix = 1024, 768
                    change_res(x_pix, y_pix)
                    player.change_spawn(x_pix/2 - 30, y_pix - 120)
                    enemies = [Enemy(random.randint(65, x_pix - 65), random.randint(75, 150)) for _ in range(num_of_enemies)]
                    for enemy in enemies:
                        enemy.bullet = Bullet()
                        enemy.bullet.config_enemy_image()
                    bullet = Bullet()
                if event.key == pygame.K_ESCAPE:
                    num_of_enemies = 6
                    support_images = support_images_small
                    x_pix, y_pix = 800, 600
                    change_res(x_pix, y_pix)
                    player.change_spawn(x_pix/2 - 30, y_pix - 120)
                    enemies = [Enemy(random.randint(65, x_pix - 65), random.randint(75, 150)) for _ in range(num_of_enemies)]
                    for enemy in enemies:
                        enemy.bullet = Bullet()
                        enemy.bullet.config_enemy_image()
                    bullet = Bullet()

    if move.mode == 'CSS':
        background = support_images["css"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    move.mode = 'MENU'
                if event.key == pygame.K_1:
                    move.mode = 'NAVE'
                if event.key == pygame.K_2:
                    move.mode = 'MONSTER'
                if event.key == pygame.K_3:
                    move.mode = 'BALA'
                if event.key == pygame.K_ESCAPE:
                    player.change_image('./img/001-nave-espacial.png')
                    for enemy in enemies:
                        enemy.change_skin('./img/002-ghost.png')
                        enemy.change_skin_hard('./img/003-ghost.png')
                    bullet.change_image('./img/001-bullet.png')

    if move.mode == 'NAVE':
        background = support_images["nave"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    move.mode = 'CSS'
                if event.key == pygame.K_1:
                    player.change_image('./img/aircraft.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_2:
                    player.change_image('./img/rocket.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_3:
                    player.change_image('./img/ufo.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_4:
                    player.change_image('./img/tardis.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_5:
                    player.change_image('./img/K9.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_ESCAPE:
                    player.change_image('./img/001-nave-espacial.png')
                    move.mode = 'CSS'
    
    if move.mode == 'MONSTER':
        background = support_images["monster"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    move.mode = 'CSS'
                if event.key == pygame.K_1:
                    for enemy in enemies:
                        enemy.change_skin('./img/000-ghost.png')
                        enemy.change_skin_hard('./img/001-ghost.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_2:
                    for enemy in enemies:
                        enemy.change_skin('./img/004-ghost.png')
                        enemy.change_skin_hard('./img/005-ghost.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_3:
                    for enemy in enemies:
                        enemy.change_skin('./img/ufo-1.png')
                        enemy.change_skin_hard('./img/ufo-2.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_4:
                    for enemy in enemies:
                        enemy.change_skin('./img/dalek.png')
                        enemy.change_skin_hard('./img/dalek-2.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_5:
                    for enemy in enemies:
                        enemy.change_skin('./img/cyberman.png')
                        enemy.change_skin_hard('./img/cyberman-2.png')
                    move.mode = 'CSS'
                if event.key == pygame.K_ESCAPE:
                    for enemy in enemies:
                        enemy.change_skin('./img/002-ghost.png')
                        enemy.change_skin_hard('./img/003-ghost.png')
                    move.mode = 'CSS'

    if move.mode == 'BALA':
        background = support_images["bala"]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    move.mode = 'CSS'
                if event.key == pygame.K_1:
                    move.mode = 'CSS'
                    bullet.change_image('./img/003-bullet.png')
                if event.key == pygame.K_2:
                    move.mode = 'CSS'
                    bullet.change_image('./img/002-bullet.png')
                if event.key == pygame.K_3:
                    move.mode = 'CSS'
                    bullet.change_image('./img/004-bullet.png')
                if event.key == pygame.K_4:
                    move.mode = 'CSS'
                    bullet.change_image('./img/laser.png')
                if event.key == pygame.K_5:
                    move.mode = 'CSS'
                    bullet.change_image('./img/laser2.png')
                if event.key == pygame.K_ESCAPE:
                    move.mode = 'CSS'
                    bullet.change_image('./img/001-bullet.png')

    if move.mode == 'GAME':
        backgrond = support_images["game"]
        playerX_change = 0

        player.movimento()
        player.change_position(player.X + playerX_change)
        if background != support_images["gameover"]:
            if bullet.state == 'stopped':
                player.fire(bullet=bullet)


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    move.restart()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and playerX_change != (x_pix*y_pix)/(800*600):
                    playerX_change = 0
                if event.key == pygame.K_RIGHT and playerX_change != -1*(x_pix*y_pix)/(800*600):
                    playerX_change = 0

    
        # garante q não saia da tela:
        if player.X <= 0:
            player.change_position(0)

        elif player.X >= x_pix - 64:
            player.change_position(x_pix - 64)

        i = 0
        for enemy in enemies:
            i += 1
            if enemy.X <= 0 or enemy.X >= x_pix - 64:
                enemy.change_vel(- enemy.vel)
            enemy.change_position(enemy.X + enemy.vel, enemy.Y)
            
            # colisão
            collision = move.isCollision(enemy, bullet)

            # #bala do inimigo
            if i%3 == 0:
                if enemy.bullet.Y >= y_pix:
                    enemy.bullet.Y = enemy.Y
                    enemy.bullet.X = enemy.X
                if enemy.bullet.Y <= y_pix:
                    enemy.bullet.change_position(enemy.bullet.X, enemy.bullet.Y + (x_pix*y_pix)/(800*600)/2)
                enemy.bullet.blit(enemy.bullet.X, enemy.bullet.Y)

            
            if collision:
                collision_sound = mixer.Sound('./sounds/explosion.wav')
                collision_sound.play()
                bullet.change_position(new_x = bullet.X, new_y = y_pix - 120)
                bullet.change_state('stopped')
                move.add_score()
                enemy.change_position(random.randint(65, x_pix - 65), random.randint(50, 150))


            ep = move.coliep(enemy.X, enemy.Y, player.X, player.Y)
            bp = move.coliep(enemy.bullet.X, enemy.bullet.Y, player.X, player.Y)
 

            if ep or bp:
                player.change_position(x_pix)
                for ind_enemy in enemies:
                    ind_enemy.change_position(x_pix, y_pix)
                background = support_images["gameover"]
                gameover_sound = pygame.mixer.Sound('./sounds/gameover.wav')
                gameover_sound.play()
             
            # enemy(enemyX[i], enemyY[i])

        # movimento da bala
        if bullet.Y <= 0:
            bullet.change_position(new_x = bullet.X, new_y = y_pix - 120)
            bullet.change_state('stopped')

        if bullet.state == 'fire':
            bullet.fire(bullet.X, bullet.Y)
            bullet.change_position(bullet.X, bullet.Y - 3)

        player.blit(player.X, player.Y)
        for enemy in enemies:
            enemy.blit(enemy.X, enemy.Y)
        # texto score
        font = pygame.font.SysFont('calibri', 24)
        text = font.render(f'SCORE: {move.score}', True, 'blue', 'black')
        textRect = text.get_rect()
        textRect.center = (45, 12)
        screen.blit(text, textRect)

        # dificuldades
        if move.score == 10:
            for enemy in enemies:
                enemy.change_to_skin_hard()
                enemy.change_vel(1)

    pygame.display.update()
