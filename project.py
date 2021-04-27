import pygame
import random

pygame.init()
gameScreen = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()

#terajšie pozadie
bg = pygame.image.load("hra_template.png")

pygame.display.set_caption("ZombieDeffence")


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #vytvorenie pozadia pre gameScreen
    gameScreen.blit(bg, (0, 0))


    pygame.display.flip()

pygame.quit()
quit()
