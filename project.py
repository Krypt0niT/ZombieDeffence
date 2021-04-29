import pygame
from pohyb_lvl1 import pohyb_lvl1

#full hd
w =  1920
h = 1080

pygame.init()
gameScreen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

#pohyb enemy
Rectheight = -100
Rectwidth = 1367

#terajšie pozadie
bg = pygame.image.load("hra_template.png")

pygame.display.set_caption("ZombieDeffence")

#textura zombie lvl1
zombie1 = pygame.image.load('zombie_lvl1.png')
zombie1.convert()
rect = zombie1.get_rect()
rect.center = (w//2, h//2)

#rychlost
VelEnemy = 1



cesta = True
run = True
while run:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #vytvorenie pozadia pre gameScreen
    gameScreen.blit(bg, (0, 0))
  

    
    if cesta:
        pohyb_lvl1()
        

    pygame.quit()
quit()
