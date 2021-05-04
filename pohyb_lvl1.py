import pygame
import multiprocessing
def pohyb_lvl1(Enemy):
    
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

    E = []
    for i in range(Enemy):
              #[x, y, alive, speed, HP, uhol]
        E.append([1367, -100, True, 1, 1, 0])

    

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

       
        if move:


            test = 0
            for i in range(Enemy):
                
                if E[test][0] == 1367:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] += E[test][3]
                    E[test][5] = 0
                    test += 1
            test = 0    
            for j in range(Enemy):
                if E[test][1] == 406 and E[test][0] == 1367:
                    z1 = True
                    test += 1
            test = 0    
            for k in range(Enemy):
                if z1:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] -= E[test][3]
                    E[test][5] = -90
                    test += 1
            test = 0
            for l in range(Enemy):
                if E[test][1] == 406 and E[test][0] == 1153:
                    z2 = True
                    test += 1
            test = 0
            for m in range(Enemy):
                if z2:
                    z1 = False
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] -= E[test][3]
                    E[test][5] = 180
                    test += 1
            test = 0
            for n in range(Enemy):    
                if E[test][1] == 83 and E[test][0] == 1153:
                    z3 = True  
                    z2 = False
                    z1 = False
                    test += 1
            test = 0
            for o in range(Enemy):
                if z3:

                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] -= E[test][3]
                    E[test][5] = -90
                    test += 1
            test = 0
            for p in range(Enemy):
                if E[test][1] == 83 and E[test][0] == 503:
                    z4 = True
                    z3 = False
                    test += 1
            test = 0
            for p in range(Enemy):
                if z4:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] += E[test][3]
                    E[test][5] = 0
                    test += 1 
            test = 0
            for i in range(Enemy):
                if E[test][1] == 407 and E[test][0] == 503:
                    z4 = False
                    z5 = True
                    test += 1
            test = 0
            for j in range(Enemy):
                if z5:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] += E[test][3]
                    E[test][5] = 90
                    test += 1
            test = 0
            for k in range(Enemy):
                if E[test][1] == 407 and E[test][0] == 719:
                    z6 = True
                    z5 = False
                    test += 1
            test = 0  
            for l in range(Enemy):
                if z6:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] -= E[test][3]
                    E[test][5] = 180
                    test += 1
            test = 0
            for m in range(Enemy):
                if E[test][1] == 298 and E[test][0] == 719:
                    z7 = True
                    z6 = False
                    test += 1
            test = 0
            for n in range (Enemy):
                if z7:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] += E[test][3]
                    E[test][5] = 90
                    test += 1
            test = 0
            for o in range(Enemy):
                if E[test][1] == 298 and E[test][0] == 827:
                    z8 = True
                    z7 = False
                    test += 1
            test = 0
            for p in range(Enemy):
                if z8:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] += E[test][3]
                    E[test][5] = 0
                    test += 1
            test = 0
            for i in range(Enemy): 
                if E[test][1] == 623 and E[test][0] == 827:
                    z9 = True
                    z8 = False
                    test += 1
            test = 0
            for j in range(Enemy):
                if z9:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] -= E[test][3]
                    E[test][5] = -90
                    test += 1
            test = 0
            for k in range(Enemy): 
                if E[test][1] == 623 and E[test][0] == 502:
                    z10 = True
                    z9 = False
                    test += 1
            test = 0
            for l in range(Enemy):
                if z10:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] += E[test][3]
                    E[test][5] = 0
                    test += 1
            test = 0
            for m in range(Enemy):
                if E[test][1] == 840 and E[test][0] == 502:
                    z11 = True
                    z10 = False
                    test += 1
            test = 0
            for n in range(Enemy):
                if z11:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] += E[test][3]
                    E[test][5] = 90
                    test += 1
            test = 0
            for o in range(Enemy):
                if E[test][1] == 840 and E[test][0] == 1043:
                    z12 = True
                    z11 = False
                    test += 1 
            test = 0
            for p in range(Enemy): 
                if z12:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] -= E[test][3]
                    E[test][5] = 180
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 623 and E[test][0] == 1043:
                    z13 = True
                    z12 = False
                    test += 1
            test = 0
            for j in range(Enemy):
                if z13:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] += E[test][3]
                    E[test][5] = 90
                    test += 1
            test = 0 
            for k in range(Enemy):
                if E[test][1] == 623 and  E[test][0] == 1258:
                    z14 = True
                    z13 = False
                    test += 1
            test = 0
            for l in range(Enemy):
                if z14:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] += E[test][3]
                    E[test][5] = 0
                    test += 1
            test = 0
            for m in range(Enemy):
                if E[test][1] == 946 and E[test][0] == 1258:
                    z15 = True
                    z14 = False 
                    test += 1
            test = 0
            for n in range(Enemy):
                if z15:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] -= E[test][3]
                    E[test][5] = -90
                    test += 1
            test = 0
            for o in range(Enemy):
                if E[test][0]  == 400:
                    z16 = True
                    test += 1
            test = 0
            for p in range(Enemy): 
                if z16:
                    move = False
                    z15 = False
                    run = False
                    test += 1
            test = 0
                
        #print(E)
        pygame.display.flip()
    