
import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()

pygame.display.set_caption("ZombieDeffence")
background = pygame.image.load("hra_template.png")


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    pygame.display.flip()

pygame.quit()
quit()
