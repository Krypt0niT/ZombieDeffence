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
                
                if E[test][0] == 1367 and (-100 <= E[test][1] <= 406):
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] += E[test][3]
                    E[test][5] = 0
                    test += 1
  

            test = 0    
            for i in range(Enemy):
                if (1153 <= E[test][0] <= 1367) and E[test][1] == 406:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] -= E[test][3]
                    E[test][5] = -90
                    test += 1
            test = 0
            for i in range(Enemy):
                if (81 <= E[test][1] <= 406) and E[test][0] == 1153:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] -= E[test][3]
                    E[test][5] = 180
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 83 and (503 <= E[test][0] <= 1153):
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] -= E[test][3]
                    E[test][5] = -90
                    test += 1
            test = 0
            for i in range(Enemy):
                if (83 <= E[test][1] <= 407) and E[test][0] == 503:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] += E[test][3]
                    E[test][5] = 0
                    test += 1 
            test = 0
            for i in range(Enemy):
                if E[test][1] == 407 and (503 <= E[test][0] <= 719):
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] += E[test][3]
                    E[test][5] = 90
                    test += 1
            test = 0
            for i in range(Enemy):
                if (298 <= E[test][1] <= 407) and E[test][0] == 719:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] -= E[test][3]
                    E[test][5] = 180
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 298 and (827 >= E[test][0] >= 719):
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] += E[test][3]
                    E[test][5] = 90
                    test += 1
            test = 0
            for i in range(Enemy):
                if (298 <= E[test][1] <= 623) and E[test][0] == 827:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] += E[test][3]
                    E[test][5] = 0
                    test += 1
            test = 0
            for i in range(Enemy): 
                if E[test][1] == 623 and (502 <= E[test][0] <= 827):
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] -= E[test][3]
                    E[test][5] = -90
                    test += 1
            test = 0
            for i in range(Enemy): 
                if (840 >= E[test][1] >= 623) and E[test][0] == 502:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] += E[test][3]
                    E[test][5] = 0
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 840 and (1043 >= E[test][0] >= 502):
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] += E[test][3]
                    E[test][5] = 90
                    test += 1
            test = 0
            for i in range(Enemy):
                if (840 >= E[test][1] >= 623) and E[test][0] == 1043:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] -= E[test][3]
                    E[test][5] = 180
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 623 and (1258 >= E[test][0] >= 1043):
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] += E[test][3]
                    E[test][5] = 90
                    test += 1
            test = 0 
            for i in range(Enemy):
                if (946 >= E[test][1] >= 623) and  E[test][0] == 1258:
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][1] += E[test][3]
                    E[test][5] = 0
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 946 and (400 <= E[test][0] <= 1258):
                    gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                    E[test][0] -= E[test][3]
                    E[test][5] = -90
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][0]  == 400:
                    move = False
                    run = False
                    test += 1
            test = 0
                
        #print(E)
        pygame.display.flip()
    
