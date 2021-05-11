import pygame
import multiprocessing

from pygame.constants import K_LEFT
def pohyb_lvl1(Enemy):
    
    pygame.init()
    gameScreen = pygame.display.set_mode()
    clock = pygame.time.Clock()

    bg = pygame.image.load("hra_template.png")
    #font
    WHITEFont = pygame.font.Font("Dirty_War.otf", 50)

    #pohyb enemy
    Rectheight = -100
    Rectwidth = 1367
    
    #ikona okna
    zombie1 = pygame.image.load('zombie_lvl1.png')
    zombie1.convert()
    # turret 1
    turret = pygame.image.load("turret.png")
    turretRECT = turret.get_rect()
    turretRECT.center = (25,45)
    turret.convert()
    
    #list enemy

    E = []
    T = []

    for i in range(Enemy):
              #[x, y, alive, speed, HP, uhol, started]
        E.append([1367, -100, True, 1, 1, 0, False])

    spustenie = 0

    move = True
    run = True

    uhol = 0
    start = 0

    health = 100

    Pturret1 = False
    mouse_position = []
    while run:
        
        clock.tick(120)
        gameScreen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()


        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            if (0 <= pos[0]) and (pos[0] <= 420):
                if (0 <= pos[1]) and (pos[1] <= 216):
                    print("obe platia")
                    Pturret1 = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            Pturret1 = False

        if Pturret1:
            gameScreen.blit(pygame.transform.rotate(turret,0),((mouse_position[0] - 25),(mouse_position[1] - 45)))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                T.append([mouse_position[0],mouse_position[1]])
                Pturret1 = False

        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            print(mouse_position)
        test = 0
        for i in range(len(T)):
            gameScreen.blit(pygame.transform.rotate(turret,0),((T[test][0] - 25),(T[test][1] - 45)))
            test += 1
        test = 0

        #ikony
        gameScreen.blit(pygame.transform.rotate(turret,0),(185,63))



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
                if E[test][1] == 946 and (399 <= E[test][0] <= 1258):
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
                    health -= 1
                    test += 1
                else:
                    test += 1

            test = 0
            start += 1
            if start == 75:
                start = 0
                if len(E) > spustenie:
                    E[spustenie][6] = True
                    spustenie += 1

            #HP

            
            HP_WHITE = WHITEFont.render(("Health: %s" % health) , True, (255,255,255))
            gameScreen.blit(HP_WHITE, (1595, 1000))


        print(T)    
        pygame.display.flip()
    