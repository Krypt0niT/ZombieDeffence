import pygame
import random

#full hd
w =  1920
h = 1080
pygame.init()
gameScreen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

#pohyb enemy
Rectheight = -100
Rectwidth = 1392

#terajšie pozadie
bg = pygame.image.load("hra_template.png")

pygame.display.set_caption("ZombieDeffence")

zombie1 = pygame.image.load('zombie_lvl1.png')
zombie1.convert()
rect = zombie1.get_rect()
rect.center = w//2, h//2

VelEnemy = 1
z1 = False
z2 = False
z3 = False
z4 = False
z5 = False
z6 = False
z7 = False
z8 = False
z9 = False
z10 = False
z11 = False
z12 = False
z13 = False
z14 = False
z15 = False


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
        velkosť = 50
        if Rectwidth == 1392:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectheight += VelEnemy
            
        if Rectheight == 430 and Rectwidth == 1392:
            z4 = True
        if z4:

            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectwidth -= VelEnemy
            
        if Rectheight == 430 and Rectwidth == 1177:
            z5 = True
        if z5:
            z4 = False
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectheight -= VelEnemy
            
        if Rectheight == 107 and Rectwidth == 1177:
            z1 = True  
            z2 = False
            z5 = False
        if z1:

            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectwidth -= VelEnemy
        if Rectheight == 107 and Rectwidth == 527:
            z2 = True
            z1 = False

        if z2:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectheight += VelEnemy
        if Rectheight == 431 and Rectwidth == 527:
            z2 = False
            z3 = True
            
        if z3:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectwidth += VelEnemy
        if Rectheight == 431 and Rectwidth == 743:
            z6 = True
            z3 = False  
        if z6:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectheight -= VelEnemy
        if Rectheight == 322 and Rectwidth == 743:
            z7 = True
            z6 = False
        if z7:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectwidth += VelEnemy
        if Rectheight == 322 and Rectwidth == 851:
            z8 = True
            z7 = False
        if z8:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectheight += VelEnemy
        if Rectheight == 647 and Rectwidth == 851:
            z9 = True
            z8 = False
        if z9:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectwidth -= VelEnemy
        if Rectheight == 647 and Rectwidth == 526:
            z10 = True
            z9 = False
        if z10:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectheight += VelEnemy
        if Rectheight == 864 and Rectwidth == 526:
            z11 = True
            z10 = False
        if z11:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectwidth += VelEnemy
        if Rectheight == 864 and Rectwidth == 1067:
            z12 = True
            z11 = False
        if z12:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectheight -= VelEnemy
        if Rectheight == 647 and Rectwidth == 1067:
            z13 = True
            z12 = False
        if z13:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectwidth += VelEnemy
        if Rectheight == 647 and  Rectwidth == 1282:
            z14 = True
            z13 = False
        if z14:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectheight += VelEnemy
        if Rectheight == 970 and Rectwidth == 1282:
            z15 = True
            z14 = False
        if z15:
            gameScreen.blit(zombie1, (Rectwidth,Rectheight))
            Rectwidth -= VelEnemy
        if Rectwidth  == 400:
            cesta = False




    print(Rectwidth,Rectheight)
    pygame.display.flip()

pygame.quit()
quit()
