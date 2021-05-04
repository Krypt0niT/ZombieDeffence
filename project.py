import pygame
from pohyb_lvl1 import pohyb_lvl1
import time

pygame.init()
gameScreen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Zombie Deffence")
icon = pygame.image.load("zombie_lvl1.png")
pygame.display.set_icon(icon)

#terajšie pozadie
bg = pygame.image.load("hra_template.png")

Enemy = 25
kolo = True
run = True
#rozrobeny text HP
font = pygame.font.Font("freesansbold.ttf", 32)
HPtext = font.render("HP:", True , (255,255,255),(255,0,0))

while run:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #vytvorenie pozadia pre gameScreen
    gameScreen.blit(bg, (0, 0))
    gameScreen.blit(HPtext,(900,900))

    
    if kolo:
        pohyb_lvl1(Enemy)
pygame.quit()
quit()