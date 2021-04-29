import pygame
def pohyb_lvl1():

    w = 1920
    h = 1080

    pygame.init()
    gameScreen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()

    bg = pygame.image.load("hra_template.png")

    #pohyb enemy
    Rectheight = -100
    Rectwidth = 1367
    

    zombie1 = pygame.image.load('zombie_lvl1.png')
    zombie1.convert()
    rect = zombie1.get_rect()
    rect.center = (w//2, h//2)

    VelEnemy = 1

    z1,z2,z3,z4,z5,z6,z7,z8,z9 = False,False,False,False,False,False,False,False,False
    z10,z11,z12,z13,z14,z15 = False,False,False,False,False,False


    cesta = True
    run = True
    while run:
        clock.tick(120)
        gameScreen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    

        
        if cesta:
            velkosť = 50
            if Rectwidth == 1367:
                gameScreen.blit(zombie1, (Rectwidth,Rectheight))
                Rectheight += VelEnemy
                
                
            if Rectheight == 406 and Rectwidth == 1367:
                z4 = True
                
            if z4:
                gameScreen.blit(pygame.transform.rotate(zombie1,-90),(Rectwidth,Rectheight))
                Rectwidth -= VelEnemy
                
            if Rectheight == 406 and Rectwidth == 1153:
                z5 = True
            if z5:
                z4 = False
                gameScreen.blit(pygame.transform.rotate(zombie1,180),(Rectwidth,Rectheight))
                Rectheight -= VelEnemy
                
            if Rectheight == 83 and Rectwidth == 1153:
                z1 = True  
                z2 = False
                z5 = False
            if z1:

                gameScreen.blit(pygame.transform.rotate(zombie1,-90),(Rectwidth,Rectheight))
                Rectwidth -= VelEnemy
            if Rectheight == 83 and Rectwidth == 503:
                z2 = True
                z1 = False

            if z2:
                gameScreen.blit(zombie1, (Rectwidth,Rectheight))
                Rectheight += VelEnemy
            if Rectheight == 407 and Rectwidth == 503:
                z2 = False
                z3 = True
                
            if z3:
                gameScreen.blit(pygame.transform.rotate(zombie1,90),(Rectwidth,Rectheight))
                Rectwidth += VelEnemy
            if Rectheight == 407 and Rectwidth == 719:
                z6 = True
                z3 = False  
            if z6:
                gameScreen.blit(pygame.transform.rotate(zombie1,180),(Rectwidth,Rectheight))
                Rectheight -= VelEnemy
            if Rectheight == 298 and Rectwidth == 719:
                z7 = True
                z6 = False
            if z7:
                gameScreen.blit(pygame.transform.rotate(zombie1,90),(Rectwidth,Rectheight))
                Rectwidth += VelEnemy
            if Rectheight == 298 and Rectwidth == 827:
                z8 = True
                z7 = False
            if z8:
                gameScreen.blit(zombie1, (Rectwidth,Rectheight))
                Rectheight += VelEnemy
            if Rectheight == 623 and Rectwidth == 827:
                z9 = True
                z8 = False
            if z9:
                gameScreen.blit(pygame.transform.rotate(zombie1,-90),(Rectwidth,Rectheight))
                Rectwidth -= VelEnemy
            if Rectheight == 623 and Rectwidth == 502:
                z10 = True
                z9 = False
            if z10:
                gameScreen.blit(zombie1, (Rectwidth,Rectheight))
                Rectheight += VelEnemy
            if Rectheight == 840 and Rectwidth == 502:
                z11 = True
                z10 = False
            if z11:
                gameScreen.blit(pygame.transform.rotate(zombie1,90),(Rectwidth,Rectheight))
                Rectwidth += VelEnemy
            if Rectheight == 840 and Rectwidth == 1043:
                z12 = True
                z11 = False
            if z12:
                gameScreen.blit(pygame.transform.rotate(zombie1,180),(Rectwidth,Rectheight))
                Rectheight -= VelEnemy
            if Rectheight == 623 and Rectwidth == 1043:
                z13 = True
                z12 = False
            if z13:
                gameScreen.blit(pygame.transform.rotate(zombie1,90),(Rectwidth,Rectheight))
                Rectwidth += VelEnemy
            if Rectheight == 623 and  Rectwidth == 1258:
                z14 = True
                z13 = False
            if z14:
                gameScreen.blit(zombie1, (Rectwidth,Rectheight))
                Rectheight += VelEnemy
            if Rectheight == 946 and Rectwidth == 1258:
                z15 = True
                z14 = False
            if z15:
                gameScreen.blit(pygame.transform.rotate(zombie1,-90),(Rectwidth,Rectheight))
                Rectwidth -= VelEnemy
            if Rectwidth  == 400:
                cesta = False




        print(Rectwidth,Rectheight)
        pygame.display.flip()

    pygame.quit()
    quit()
