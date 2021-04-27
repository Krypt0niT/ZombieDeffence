import pygame
import random

pygame.init()
gameScreen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

#terajšie pozadie
bg = pygame.image.load("hra_template.png")

pygame.display.set_caption("ZombieDeffence")

Rectheight = -100
Rectwidth = 1392
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
        velkosť = 20
        if Rectwidth == 1392:

            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectheight += VelEnemy
            
        if Rectheight == 430 and Rectwidth == 1392:
            z4 = True
        if z4:

            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectwidth -= VelEnemy
            
        if Rectheight == 430 and Rectwidth == 1177:
            z5 = True
        if z5:
            z4 = False
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectheight -= VelEnemy
            
        if Rectheight == 107 and Rectwidth == 1177:
            z1 = True  
            z2 = False
            z5 = False
        if z1:

            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectwidth -= VelEnemy
        if Rectheight == 107 and Rectwidth == 527:
            z2 = True
            z1 = False

        if z2:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectheight += VelEnemy
        if Rectheight == 431 and Rectwidth == 527:
            z2 = False
            z3 = True
            
        if z3:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectwidth += VelEnemy
        if Rectheight == 431 and Rectwidth == 743:
            z6 = True
            z3 = False  
        if z6:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectheight -= VelEnemy
        if Rectheight == 322 and Rectwidth == 743:
            z7 = True
            z6 = False
        if z7:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectwidth += VelEnemy
        if Rectheight == 322 and Rectwidth == 851:
            z8 = True
            z7 = False
        if z8:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectheight += VelEnemy
        if Rectheight == 647 and Rectwidth == 851:
            z9 = True
            z8 = False
        if z9:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectwidth -= VelEnemy
        if Rectheight == 647 and Rectwidth == 526:
            z10 = True
            z9 = False
        if z10:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectheight += VelEnemy
        if Rectheight == 864 and Rectwidth == 526:
            z11 = True
            z10 = False
        if z11:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectwidth += VelEnemy
        if Rectheight == 864 and Rectwidth == 1067:
            z12 = True
            z11 = False
        if z12:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectheight -= VelEnemy
        if Rectheight == 647 and Rectwidth == 1067:
            z13 = True
            z12 = False
        if z13:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectwidth += VelEnemy
        if Rectheight == 647 and  Rectwidth == 1282:
            z14 = True
            z13 = False
        if z14:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectheight += VelEnemy
        if Rectheight == 970 and Rectwidth == 1282:
            z15 = True
            z14 = False
        if z15:
            pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect(Rectwidth, Rectheight, velkosť, velkosť))
            Rectwidth -= VelEnemy
        if Rectwidth  == 400:
            cesta = False




    print(Rectwidth,Rectheight)
    pygame.display.flip()

pygame.quit()
quit()
