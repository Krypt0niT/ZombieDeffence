import pygame
import multiprocessing
def pohyb_lvl1(a):
    
    pygame.init()
    gameScreen = pygame.display.set_mode()
    clock = pygame.time.Clock()

    bg = pygame.image.load("hra_template.png")

    #pohyb enemy
    Rectheight = -100
    Rectwidth = 1367
    
    #ikona okna
    zombie1 = pygame.image.load('zombie_lvl1.png')
    zombie1.convert()
    
    
    #rychlost enemy
    VelEnemy = 1

    z1,z2,z3,z4,z5,z6,z7,z8,z9 = False,False,False,False,False,False,False,False,False
    z10,z11,z12,z13,z14,z15,z16 = False,False,False,False,False,False,False
    #list enemy
    enemies = []
    for i in range(a):
        enemies.append("1")

    

    move = True
    run = True

    uhol = 0

    while run:
        
        clock.tick(120)
        gameScreen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        velkosť = 50
        if move:
            if Rectwidth == 1367:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectheight += VelEnemy
                uhol = 0
                
                
            if Rectheight == 406 and Rectwidth == 1367:
                z1 = True
                
            if z1:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectwidth -= VelEnemy
                uhol = -90
                
            if Rectheight == 406 and Rectwidth == 1153:
                z2 = True
            if z2:
                z1 = False
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectheight -= VelEnemy
                uhol = 180
                
            if Rectheight == 83 and Rectwidth == 1153:
                z3 = True  
                z2 = False
                z1 = False
            if z3:

                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectwidth -= VelEnemy
                uhol = -90
            if Rectheight == 83 and Rectwidth == 503:
                z4 = True
                z3 = False

            if z4:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectheight += VelEnemy
                uhol = 0
            if Rectheight == 407 and Rectwidth == 503:
                z4 = False
                z5 = True
                
            if z5:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectwidth += VelEnemy
                uhol = 90
            if Rectheight == 407 and Rectwidth == 719:
                z6 = True
                z5 = False  
            if z6:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectheight -= VelEnemy
                uhol = 180
            if Rectheight == 298 and Rectwidth == 719:
                z7 = True
                z6 = False
            if z7:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectwidth += VelEnemy
                uhol = 90
            if Rectheight == 298 and Rectwidth == 827:
                z8 = True
                z7 = False
            if z8:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectheight += VelEnemy
                uhol = 0
            if Rectheight == 623 and Rectwidth == 827:
                z9 = True
                z8 = False
            if z9:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectwidth -= VelEnemy
                uhol = -90
            if Rectheight == 623 and Rectwidth == 502:
                z10 = True
                z9 = False
            if z10:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectheight += VelEnemy
                uhol = 0
            if Rectheight == 840 and Rectwidth == 502:
                z11 = True
                z10 = False
            if z11:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectwidth += VelEnemy
                uhol = 90
            if Rectheight == 840 and Rectwidth == 1043:
                z12 = True
                z11 = False
            if z12:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectheight -= VelEnemy
                uhol = 180
            if Rectheight == 623 and Rectwidth == 1043:
                z13 = True
                z12 = False
            if z13:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectwidth += VelEnemy
                uhol = 90
            if Rectheight == 623 and  Rectwidth == 1258:
                z14 = True
                z13 = False
            if z14:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectheight += VelEnemy
                uhol = 0
            if Rectheight == 946 and Rectwidth == 1258:
                z15 = True
                z14 = False
            if z15:
                gameScreen.blit(pygame.transform.rotate(zombie1,uhol),(Rectwidth,Rectheight))
                Rectwidth -= VelEnemy
                uhol = -90
            if Rectwidth  == 400:
                z16 = True
            if z16:
                move = False
                z15 = False
                run = False
                
        print(Rectwidth,Rectheight)
        print(a)
        pygame.display.flip()
    