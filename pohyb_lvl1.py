import pygame
import multiprocessing
import random
import math


from pygame.constants import K_LEFT
def pohyb_lvl1(Enemy):
    

    
    pygame.init()
    gameScreen = pygame.display.set_mode()
    clock = pygame.time.Clock()

    bg = pygame.image.load("hra_template.png")
    #font
    WHITEFont = pygame.font.Font("Dirty_War.otf", 50)
    whitefont = pygame.font.Font("Dirty_War.otf", 20)
    #pohyb enemy
    Rectheight = -100
    Rectwidth = 1367
    
    #ikona okna
    zombie1_1 = pygame.image.load('images/zombie/zombie_lvl1_1.png')
    zombie1_1.convert()
    zombie1_2 = pygame.image.load('images/zombie/zombie_lvl1_2.png')
    zombie1_2.convert()
    zombie1_3 = pygame.image.load('images/zombie/zombie_lvl1_3.png')
    zombie1_3.convert()
    zombie1_4 = pygame.image.load('images/zombie/zombie_lvl1_4.png')
    zombie1_4.convert()
    zombie1_5 = pygame.image.load('images/zombie/zombie_lvl1_5.png')
    zombie1_5.convert()





    # turret 11
    turret11 = pygame.image.load("images/turrets/turret11.png")
    turret11RECT = turret11.get_rect()
    turret11RECT.center = (25,45)
    turret11.convert()
    #turret 21
    turret21 = pygame.image.load("images/turrets/turret21.png")
    turret21RECT = turret21.get_rect()
    turret21RECT.center = (25,45)
    turret21.convert()
    #turret 31
    turret31 = pygame.image.load("images/turrets/turret31.png")
    turret31RECT = turret31.get_rect()
    turret31RECT.center = (25,45)
    turret31.convert()
    #turret 41
    turret41 = pygame.image.load("images/turrets/turret41.png")
    turret41RECT = turret41.get_rect()
    turret41RECT.center = (25,45)
    turret41.convert()
    #turret 12
    turret12 = pygame.image.load("images/turrets/turret12.png")
    turret12RECT = turret12.get_rect()
    turret12RECT.center = (25,45)
    turret12.convert()
    #turret 22
    turret22 = pygame.image.load("images/turrets/turret22.png")
    turret22RECT = turret22.get_rect()
    turret22RECT.center = (25,45)
    turret22.convert()
    #turret 32
    turret32 = pygame.image.load("images/turrets/turret32.png")
    turret32RECT = turret32.get_rect()
    turret32RECT.center = (25,45)
    turret32.convert()
    #turret 42
    turret42 = pygame.image.load("images/turrets/turret42.png")
    turret42RECT = turret42.get_rect()
    turret42RECT.center = (25,45)
    turret42.convert()
    #turret 13
    turret13 = pygame.image.load("images/turrets/turret13.png")
    turret13RECT = turret13.get_rect()
    turret13RECT.center = (25,45)
    turret13.convert()
    #turret 23
    turret23 = pygame.image.load("images/turrets/turret23.png")
    turret23RECT = turret23.get_rect()
    turret23RECT.center = (25,45)
    turret23.convert()
    #turret 33
    turret33 = pygame.image.load("images/turrets/turret33.png")
    turret33RECT = turret33.get_rect()
    turret33RECT.center = (25,45)
    turret33.convert()
    #turret 43
    turret43 = pygame.image.load("images/turrets/turret43.png")
    turret43RECT = turret43.get_rect()
    turret43RECT.center = (25,45)
    turret43.convert()

    #list enemy

    E = []
    T = []

    randomZ = 0

    for i in range(Enemy):
        randomZ = random.randint(1,5)
              #[x, y, alive, speed, MaxHP, uhol, started, type, HP]
        if randomZ == 1:
            E.append([1367, -100, True, 1, 2, 0, False, zombie1_1, 2])
        if randomZ == 2:
            E.append([1367, -100, True, 1, 2, 0, False, zombie1_2, 1])
        if randomZ == 3:
            E.append([1367, -100, True, 1, 2, 0, False, zombie1_3, 1.5])
        if randomZ == 4:
            E.append([1367, -100, True, 1, 2, 0, False, zombie1_4, 2])
        if randomZ == 5:
            E.append([1367, -100, True, 1, 2, 0, False, zombie1_5, 2])

    spustenie = 0

    move = True
    run = True

    uhol = 0
    start = 0

    health = 100
    money = 100000

    cenaT11 = 100
    cenaT21 = 250
    cenaT31 = 400
    cenaT41 = 1000

    cenaT12 = 300
    cenaT22 = 500
    cenaT32 = 750
    cenaT42 = 1000

    cenaT13 = 1000
    cenaT23 = 1500
    cenaT33 = 2000
    cenaT43 = 2500
 


    Pturret11 = False
    mouse_position = []

    #turret place location
    TPL = [(445,1338,20,50),(445,473,50,925),(474,794,484,591),(582,1120,162,269),(582,687,270,375),(771,819,353,484),(582,1010,650,808),(474,1227,910,925),
        (1119,1227,700,909),(900,1010,270,649),(1011,1120,270,591),(1230,1338,51,375),(1447,1474,25,1055),(1121,1446,484,591),(1286,1446,592,1054),
        (445,1285,974,1054)]

    
        #trasa
    EnemyTrack = [(-100,406,1367,0),(406,1153,1367,-90),(81,406,1153,180),(83,503,1153,-90),(83,407,503,0),
        (407,503,719,90),(298,407,719,180),(298,827,719,90),(298,623,827,0),(623,502,827,-90),(840,623,502,0),
        (840,1043,502,90),(840,623,1043,180),(623,1258,1043,90),(946,623,1258,0),(946,399,1258,-90)]

    textcenaT11 = WHITEFont.render("100" , True, (255,255,255))
    textcenaT21 = WHITEFont.render("250" , True, (255,255,255))
    textcenaT31 = WHITEFont.render("400" , True, (255,255,255))
    textcenaT41 = WHITEFont.render("1000" , True, (255,255,255))
    textcenaT12 = WHITEFont.render("300" , True, (255,255,255))
    textcenaT22 = WHITEFont.render("500" , True, (255,255,255))
    textcenaT32 = WHITEFont.render("750" , True, (255,255,255))
    textcenaT42 = WHITEFont.render("1000" , True, (255,255,255))

    textcenaT13 = WHITEFont.render("1500" , True, (255,255,255))
    textcenaT23 = WHITEFont.render("1500" , True, (255,255,255))
    textcenaT33 = WHITEFont.render("1000" , True, (255,255,255))
    textcenaT43 = WHITEFont.render("1000" , True, (255,255,255))
    maxtext = WHITEFont.render("MAX" , True, (255,255,255))

    Trange = pygame.image.load("images/other/range.png")
    TrangeRECT = Trange.get_rect()
    TrangeRECT.center = (150,150)
    Trange.convert()

    #farby
    liteGreen = (0,255,0)


    playbutton = pygame.image.load("images/other/play.png")

    while run:
        
        clock.tick(120)
        gameScreen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        #playbutton
        gameScreen.blit(playbutton,(1508,656))

        


        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            if (0 <= pos[0]) and (pos[0] <= 420):
                if (0 <= pos[1]) and (pos[1] <= 216):
                    if money >= cenaT11:

                        Pturret11 = True
                    #else:
        for i in range(len(T)):
            if T[i][2] == True:
                gameScreen.blit(pygame.transform.rotate(Trange,0),((T[i][0]-150),(T[i][1]-150)))
                if T[i][3] == 11:
                    gameScreen.blit(pygame.transform.rotate(turret21,0),(1700,63))
                    gameScreen.blit(textcenaT21, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret12,0),(1700,279))
                    gameScreen.blit(textcenaT12, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 21:
                    gameScreen.blit(pygame.transform.rotate(turret31,0),(1700,63))
                    gameScreen.blit(textcenaT31, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret22,0),(1700,279))
                    gameScreen.blit(textcenaT22, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 31:
                    gameScreen.blit(pygame.transform.rotate(turret41,0),(1700,63))
                    gameScreen.blit(textcenaT41, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret32,0),(1700,279))
                    gameScreen.blit(textcenaT32, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 41:
                    gameScreen.blit(pygame.transform.rotate(turret41,0),(1700,63))
                    gameScreen.blit(maxtext, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret42,0),(1700,279))
                    gameScreen.blit(textcenaT42, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 12:
                    gameScreen.blit(pygame.transform.rotate(turret22,0),(1700,63))
                    gameScreen.blit(textcenaT22, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret13,0),(1700,279))
                    gameScreen.blit(textcenaT13, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 22:
                    gameScreen.blit(pygame.transform.rotate(turret32,0),(1700,63))
                    gameScreen.blit(textcenaT32, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret13,0),(1700,279))
                    gameScreen.blit(textcenaT13, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 32:
                    gameScreen.blit(pygame.transform.rotate(turret42,0),(1700,63))
                    gameScreen.blit(textcenaT42, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret33,0),(1700,279))
                    gameScreen.blit(textcenaT33, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 22:
                    gameScreen.blit(pygame.transform.rotate(turret32,0),(1700,63))
                    gameScreen.blit(textcenaT32, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret23,0),(1700,279))
                    gameScreen.blit(textcenaT23, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 42:
                    gameScreen.blit(pygame.transform.rotate(turret42,0),(1700,63))
                    gameScreen.blit(maxtext, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret43,0),(1700,279))
                    gameScreen.blit(textcenaT43, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 13:
                    gameScreen.blit(pygame.transform.rotate(turret23,0),(1700,63))
                    gameScreen.blit(textcenaT23, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret13,0),(1700,279))
                    gameScreen.blit(maxtext, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 23:
                    gameScreen.blit(pygame.transform.rotate(turret33,0),(1700,63))
                    gameScreen.blit(textcenaT33, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret23,0),(1700,279))
                    gameScreen.blit(maxtext, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 33:
                    gameScreen.blit(pygame.transform.rotate(turret43,0),(1700,63))
                    gameScreen.blit(textcenaT43, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret33,0),(1700,279))
                    gameScreen.blit(maxtext, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if T[i][3] == 43:
                    gameScreen.blit(pygame.transform.rotate(turret43,0),(1700,63))
                    gameScreen.blit(maxtext, (1800, 150))
                    gameScreen.blit(pygame.transform.rotate(turret33,0),(1700,279))
                    gameScreen.blit(maxtext, (1800, 366))
                    gameScreen.blit(whitefont.render(("AttackSpeed: %s" % T[i][4]) , True, (255,255,255)), (T[i][0], T[i][1] + 35))
                    gameScreen.blit(whitefont.render(("Damage: %s" % T[i][5]) , True, (255,255,255)), (T[i][0], T[i][1] + 70))
                if (T[i][0]+25) >= mouse_position[0] >= (T[i][0]-25) and (T[i][1]+25) >= mouse_position[1] >= (T[i][1]-25):
                    if event.type == pygame.MOUSEBUTTONUP:
                        T[i][2] = True
                else:
                    if event.type == pygame.MOUSEBUTTONUP:   
                        T[i][2] = False

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if (1500 <= pos[0]) and (pos[0] <= 1920) and (0 <= pos[1]) and (pos[1] <= 216):
                        if T[i][3] == 11:
                            if money >= cenaT21:
                                T[i][3] = 21
                                T[i][5] = 2
                                money -= cenaT21
                        elif T[i][3] == 21:
                            if money >= cenaT31:
                                T[i][3] = 31
                                T[i][5] = 3
                                money -= cenaT31
                        elif T[i][3] == 31:
                            if money >= cenaT41:
                                T[i][3] = 41
                                T[i][5] = 3
                                money -= cenaT41
                        elif T[i][3] == 12:
                            if money >= cenaT22:
                                T[i][3] = 22
                                T[i][5] = 2
                                money -= cenaT22
                        elif T[i][3] == 22:
                            if money >= cenaT32:
                                T[i][3] = 32
                                T[i][5] = 3
                                money -= cenaT32
                        elif T[i][3] == 32:
                            if money >= cenaT42:
                                T[i][3] = 42
                                T[i][5] = 4
                                money -= cenaT42
                        elif T[i][3] == 23:
                            if money >= cenaT32:
                                T[i][3] = 33
                                T[i][5] = 3
                                money -= cenaT32
                        elif T[i][3] == 33:
                            if money >= cenaT43:
                                T[i][3] = 43
                                T[i][5] = 4
                                money -= cenaT43
                        elif T[i][3] == 13:
                            if money >= cenaT23:
                                T[i][3] = 23
                                T[i][5] = 2
                                money -= cenaT23
                                
                    elif (1500 <= pos[0]) and (pos[0] <= 1920) and (217 <= pos[1]) and (pos[1] <= 432):
                        if T[i][3] == 11:
                            if money >= cenaT12:
                                T[i][3] = 12
                                T[i][4] = 1.5
                                money -= cenaT12
                        elif T[i][3] == 21:
                            if money >= cenaT22:
                                T[i][3] = 22
                                T[i][4] = 1.5
                                money -= cenaT22
                        elif T[i][3] == 31:
                            if money >= cenaT32:
                                T[i][3] = 32
                                T[i][4] = 1.5
                                money -= cenaT32
                        
                        elif T[i][3] == 12:
                            if money >= cenaT13:
                                T[i][3] = 13
                                T[i][4] = 1.7
                                money -= cenaT13
                        elif T[i][3] == 22:
                            if money >= cenaT23:
                                T[i][3] = 23
                                T[i][4] = 1.7
                                money -= cenaT23
                        elif T[i][3] == 32:
                            if money >= cenaT33:
                                T[i][3] = 33
                                T[i][4] = 1.7
                                money -= cenaT23
                        elif T[i][3] == 42:
                            if money >= cenaT43:
                                T[i][3] = 43
                                T[i][4] = 1.7
                                money -= cenaT43
                        elif T[i][3] == 41:
                            if money >= cenaT42:
                                T[i][3] = 42
                                T[i][4] = 1.5
                                money -= cenaT42
                        
                        
                        
                                
                        

        for i in range(len(T)):
            if (T[i][0]+25) >= mouse_position[0] >= (T[i][0]-25) and (T[i][1]+25) >= mouse_position[1] >= (T[i][1]-25):
                if event.type == pygame.MOUSEBUTTONUP:
                    T[i][2] = True
            else:
                if event.type == pygame.MOUSEBUTTONUP:   
                    T[i][2] = False



        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            Pturret11 = False
        #položenie turrety 11
        

        if Pturret11:
            gameScreen.blit(pygame.transform.rotate(turret11,0),((mouse_position[0] - 25),(mouse_position[1] - 45)))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:


                for i in range(16):
                    if (TPL[i][0] <= mouse_position[0] <= TPL[i][1]):
                        if(TPL[i][2] <= mouse_position[1] <= TPL[i][3]):
                            T.append([mouse_position[0], mouse_position[1], False, 11, 1, 1, 999, False, 0])
                            #                x      ,       y       , selected, type, speed, dmg, locked enemy, locked, UHOL
                            Pturret11 = False
                            money -= cenaT11

        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()


        for i in range(len(T)):
            if T[i][3] == 11:
                gameScreen.blit(pygame.transform.rotate(turret11,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))
            if T[i][3] == 21:
                gameScreen.blit(pygame.transform.rotate(turret21,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))
            if T[i][3] == 31:
                gameScreen.blit(pygame.transform.rotate(turret31,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))
            if T[i][3] == 41:
                gameScreen.blit(pygame.transform.rotate(turret41,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))
            if T[i][3] == 42:
                gameScreen.blit(pygame.transform.rotate(turret42,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))
            if T[i][3] == 12:
                gameScreen.blit(pygame.transform.rotate(turret12,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))
            if T[i][3] == 22:
                gameScreen.blit(pygame.transform.rotate(turret22,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))
            if T[i][3] == 32:
                gameScreen.blit(pygame.transform.rotate(turret32,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))
            if T[i][3] == 13:
                gameScreen.blit(pygame.transform.rotate(turret13,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))
            if T[i][3] == 23:
                gameScreen.blit(pygame.transform.rotate(turret23,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))
            if T[i][3] == 33:
                gameScreen.blit(pygame.transform.rotate(turret33,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))
            if T[i][3] == 43:
                gameScreen.blit(pygame.transform.rotate(turret43,T[i][8]),((T[i][0] - 25),(T[i][1] - 45)))


       
        
        
        test = 0
        if move:

            for i in range(Enemy):
                if (EnemyTrack[test][0] <= E[i][1] <= EnemyTrack[test][1]) and E[i][0] == EnemyTrack[test][2]:
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][1] += E[i][3]
                        E[i][5] = EnemyTrack[test][3]
                for j in range(len(T)):


                        if (T[j][0]-150) <= E[i][0] <= (T[j][0]+150) and (T[j][1]-150) <= E[i][1] <= (T[j][1]+150):
                               if T[j][7] == False:
                                    T[j][6] = i
                                    T[j][7] = True
                                    #if T[j][6] 
                        if T[j][7] == True:
                            ex , ey = E[T[j][6]][0] ,E[T[j][6]][1]
                            dx , dy = ex - ((T[j][0])), ey -((T[j][1]))
                            T[j][8] = math.degrees(math.atan2(-dy,dx)) -90
                            


                            if (T[j][0]-150) <= E[T[j][6]][0] <= (T[j][0]+150) and (T[j][1]-150) <= E[T[j][6]][1] <= (T[j][1]+150):
                                print("")
                            else:
                                T[j][7] = False
                                T[j][6] = 999
                dorovnavanie = 20
                HP = 40
                #v PX
                if E[i][2] == True:
                    if E[i][5] == 180 or E[i][5] == 0:
                        if E[i][8] != E[i][4]:
                            print("hitted")
                            cHP = E[i][4]/E[i][8]
                            pygame.draw.rect(gameScreen, liteGreen, pygame.Rect((E[i][0] + 4,E[i][1] - dorovnavanie),(HP/cHP,10)),)
                        else:
                            pygame.draw.rect(gameScreen, liteGreen, pygame.Rect((E[i][0] + 4,E[i][1] - dorovnavanie),(HP,10)),)
                        pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect((E[i][0] + 4,E[i][1] - dorovnavanie),(HP,10)), 2)
                    cHP = 1
                    if E[i][5] == 90 or E[i][5] == -90:
                        if E[i][8] != E[i][4]:
                            print("hitted")
                            cHP = E[i][4]/E[i][8]
                            pygame.draw.rect(gameScreen, liteGreen, pygame.Rect((E[i][0],E[i][1] - dorovnavanie),(HP/cHP,10)),)
                        else:
                            pygame.draw.rect(gameScreen, liteGreen, pygame.Rect((E[i][0],E[i][1] - dorovnavanie),(HP,10)),)
                        pygame.draw.rect(gameScreen, (0,0,0), pygame.Rect((E[i][0],E[i][1] - dorovnavanie),(HP,10)), 2)
                    cHP = 1




            test += 1
            for i in range(Enemy):
                if E[i][1] == EnemyTrack[test][0] and (EnemyTrack[test][1] <= E[i][0] <= EnemyTrack[test][2]):
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][0] -= E[i][3]
                        E[i][5] = EnemyTrack[test][3]
                            



            for i in range(Enemy):
                if (81 <= E[i][1] <= 406) and E[i][0] == 1153:
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][1] -= E[i][3]
                        E[i][5] = 180

            for i in range(Enemy):
                if E[i][1] == 83 and (503 <= E[i][0] <= 1153):
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][0] -= E[i][3]
                        E[i][5] = -90

            for i in range(Enemy):
                if (83 <= E[i][1] <= 407) and E[i][0] == 503:
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][1] += E[i][3]
                        E[i][5] = 0

            for i in range(Enemy):
                if E[i][1] == 407 and (503 <= E[i][0] <= 719):
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][0] += E[i][3]
                        E[i][5] = 90

            for i in range(Enemy):
                if (298 <= E[i][1] <= 407) and E[i][0] == 719:
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][1] -= E[i][3]
                        E[i][5] = 180

            for i in range(Enemy):
                if E[i][1] == 298 and (827 >= E[i][0] >= 719):
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][0] += E[i][3]
                        E[i][5] = 90

            for i in range(Enemy):
                if (298 <= E[i][1] <= 623) and E[i][0] == 827:
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][1] += E[i][3]
                        E[i][5] = 0

            for i in range(Enemy): 
                if E[i][1] == 623 and (502 <= E[i][0] <= 827):
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][0] -= E[i][3]
                        E[i][5] = -90

            for i in range(Enemy): 
                if (840 >= E[i][1] >= 623) and E[i][0] == 502:
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][1] += E[i][3]
                        E[i][5] = 0

            for i in range(Enemy):
                if E[i][1] == 840 and (1043 >= E[i][0] >= 502):
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][0] += E[i][3]
                        E[i][5] = 90

            for i in range(Enemy):
                if (840 >= E[i][1] >= 623) and E[i][0] == 1043:
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][1] -= E[i][3]
                        E[i][5] = 180

            for i in range(Enemy):
                if E[i][1] == 623 and (1258 >= E[i][0] >= 1043):
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][0] += E[i][3]
                        E[i][5] = 90

            for i in range(Enemy):
                if (946 >= E[i][1] >= 623) and  E[i][0] == 1258:
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][1] += E[i][3]
                        E[i][5] = 0

            for i in range(Enemy):
                if E[i][1] == 946 and (399 <= E[i][0] <= 1258):
                    if E[i][6] == True:
                        gameScreen.blit(pygame.transform.rotate(E[i][7],E[i][5]),(E[i][0],E[i][1]))
                        E[i][0] -= E[i][3]
                        E[i][5] = -90

            for i in range(Enemy):
                if E[i][0]  == 400:
                    health -= 1
                    E[i][2] = False



            start += 1
            if start == 75:
                start = 0
                if len(E) > spustenie:
                    E[spustenie][6] = True
                    spustenie += 1

            #HP
            #ikony
            gameScreen.blit(pygame.transform.rotate(turret11,0),(185,63))
            
            #HP_WHITE = WHITEFont.render(("Health: %s" % health) , True, (255,255,255))
            textHelth = WHITEFont.render(("%s" % health) , True, (255,255,255))
            textMoney = WHITEFont.render(("%s" % money) , True, (255,255,255))


            gameScreen.blit(textHelth, (1600, 1000))
            gameScreen.blit(textMoney, (1600, 900))
            gameScreen.blit(textcenaT11, (300, 150))


        pygame.display.flip()