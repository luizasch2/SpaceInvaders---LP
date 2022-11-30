import pygame

x_pix = 800
y_pix = 600
screen = pygame.display.set_mode((x_pix, y_pix))

if x_pix == 800 and y_pix == 600:
    num_of_enemies = 6
elif x_pix == 1024 and y_pix == 768:
    num_of_enemies = 10

def scene_config(title = "Space Invaders", image = './img/MENU.png', sound = './sounds/background.wav'):
    global screen, x_pix, y_pix, score
    x_pix = 800
    y_pix = 600
    ## title
    pygame.display.set_caption(title)
    ## background image
    background = pygame.image.load(image)
    # background sound
    background_sound = pygame.mixer.Sound(sound)
    ## para o som tocar em loop:
    background_sound.play(-1)
    # RGB
    screen.fill((0, 0, 0))
    # Plano de fundo
    screen.blit(background, (0, 0))
    return background

def change_res(x, y):
    global x_pix, y_pix, screen
    x_pix, y_pix = x, y
    screen = pygame.display.set_mode((x_pix, y_pix))

support_images_big = {
    "menu": pygame.image.load('./img/MENU1.png'),
    "opt": pygame.image.load('./img/opt1.jpg'),
    "res": pygame.image.load('./img/res1.jpg'),
    "css": pygame.image.load('./img/css1.jpg'),
    "nave": pygame.image.load('./img/nave1.jpg'),
    "monster": pygame.image.load('./img/monster1.jpg'),
    "bala": pygame.image.load('./img/bala1.jpg'),
    "game": pygame.image.load('./img/game1.jpg'),
    "gameover":  pygame.image.load('./img/game.over1-ic.png')
}

support_images_small = {
    "menu": pygame.image.load('./img/MENU.png'),
    "opt": pygame.image.load('./img/opt.jpg'),
    "res": pygame.image.load('./img/res.jpg'),
    "css": pygame.image.load('./img/css.jpg'),
    "nave": pygame.image.load('./img/nave.jpg'),
    "monster": pygame.image.load('./img/monster.jpg'),
    "bala": pygame.image.load('./img/bala.jpg'),
    "game": pygame.image.load('./img/space-trip-colorful-digital-art.jpg'),
    "gameover":  pygame.image.load('./img/game.over-ic.png')
}

support_images = support_images_small


