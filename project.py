import pygame
from pohyb_lvl1 import pohyb_lvl1
import time

pygame.init()
gameScreen = pygame.display.set_mode((1920, 1080))

pygame.display.set_caption("Zombie Deffence")
icon = pygame.image.load("images/zombie/zombie_lvl1_1.png")
pygame.display.set_icon(icon)


Enemy = 2
kolo = True
run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if kolo:
        pohyb_lvl1()
pygame.quit()
quit()