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
    
    #list enemy

    E = []
    for i in range(Enemy):
              #[x, y, alive, speed, HP, uhol, started]
        E.append([1367, -100, True, 1, 1, 0, False])

    spustenie = 0

    move = True
    run = True

    uhol = 0
    start = 0

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
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][1] += E[test][3]
                        E[test][5] = 0
                        test += 1
                else:
                    test += 1
  

            test = 0    
            for i in range(Enemy):
                if (1153 <= E[test][0] <= 1367) and E[test][1] == 406:
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][0] -= E[test][3]
                        E[test][5] = -90
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if (81 <= E[test][1] <= 406) and E[test][0] == 1153:
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][1] -= E[test][3]
                        E[test][5] = 180
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 83 and (503 <= E[test][0] <= 1153):
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][0] -= E[test][3]
                        E[test][5] = -90
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if (83 <= E[test][1] <= 407) and E[test][0] == 503:
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][1] += E[test][3]
                        E[test][5] = 0
                        test += 1 
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 407 and (503 <= E[test][0] <= 719):
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][0] += E[test][3]
                        E[test][5] = 90
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if (298 <= E[test][1] <= 407) and E[test][0] == 719:
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][1] -= E[test][3]
                        E[test][5] = 180
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 298 and (827 >= E[test][0] >= 719):
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][0] += E[test][3]
                        E[test][5] = 90
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if (298 <= E[test][1] <= 623) and E[test][0] == 827:
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][1] += E[test][3]
                        E[test][5] = 0
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy): 
                if E[test][1] == 623 and (502 <= E[test][0] <= 827):
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][0] -= E[test][3]
                        E[test][5] = -90
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy): 
                if (840 >= E[test][1] >= 623) and E[test][0] == 502:
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][1] += E[test][3]
                        E[test][5] = 0
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 840 and (1043 >= E[test][0] >= 502):
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][0] += E[test][3]
                        E[test][5] = 90
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if (840 >= E[test][1] >= 623) and E[test][0] == 1043:
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][1] -= E[test][3]
                        E[test][5] = 180
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 623 and (1258 >= E[test][0] >= 1043):
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][0] += E[test][3]
                        E[test][5] = 90
                        test += 1
                else:
                    test += 1
            test = 0 
            for i in range(Enemy):
                if (946 >= E[test][1] >= 623) and  E[test][0] == 1258:
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][1] += E[test][3]
                        E[test][5] = 0
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][1] == 946 and (400 <= E[test][0] <= 1258):
                    if E[test][6] == True:
                        gameScreen.blit(pygame.transform.rotate(zombie1,E[test][5]),(E[test][0],E[test][1]))
                        E[test][0] -= E[test][3]
                        E[test][5] = -90
                        test += 1
                else:
                    test += 1
            test = 0
            for i in range(Enemy):
                if E[test][0]  == 400:
                    if E[test][6] == True:
                        E[test][6] == False
                        test += 1
                else:
                    test += 1
            test = 0
            start += 1
            if start == 100:
                start = 0
                if len(E) > spustenie:
                    E[spustenie][6] = True
                    spustenie += 1
            print(E)
        #print(E)
        pygame.display.flip()
    