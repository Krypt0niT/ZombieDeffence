import pygame
from hra import hra
import time

pygame.init()
gameScreen = pygame.display.set_mode((1920, 1080))

pygame.display.set_caption("Zombie Deffence")
icon = pygame.image.load("images/zombie/zombie_lvl1_1.png")
pygame.display.set_icon(icon)

kolo = True
run = True
over = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if kolo:

        hra(over)
        break

pygame.quit()
quit()