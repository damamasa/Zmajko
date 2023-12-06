import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Zmajevi")

a = pygame.Surface((screen.get_width(),screen.get_height()))
a.fill("blue")

def igra():
    run = True
    vrijeme = 0

    #igrac varijable
    zmaj_h = screen.get_height() / 7
    zmaj_w = screen.get_width() / 12
    zmaj_x = screen.get_width() - (screen.get_width()/2) - (zmaj_w/2)
    zmaj_y = screen.get_height() - (screen.get_height()/6) - (zmaj_h /2)

    #protivnik varijable
    listaProtivnikaX = []
    listaProtivnikaY = []
    brojProtivnika = 100 #za sad

    for i in range(brojProtivnika):
        protivnikX = random.randint(0, screen.get_width()-zmaj_w/2)
        if i == 0:
            listaProtivnikaX.append(protivnikX)
        else:
            while abs(listaProtivnikaX[i-1]-protivnikX) < zmaj_w:
                protivnikX = random.randint(0, screen.get_width()-(zmaj_w/2))
            else:
                listaProtivnikaX.append(protivnikX)
        if i == 0:
            listaProtivnikaY.append(-zmaj_h)
        else:
            listaProtivnikaY.append(listaProtivnikaY[i-1]-zmaj_h)

    def igrac(x,y):
        pygame.draw.rect(screen, "red", pygame.Rect(zmaj_x, zmaj_y, zmaj_w, zmaj_h))
    
    def protivnik(x,y, i):
        pygame.draw.rect(screen, "green", pygame.Rect(listaProtivnikaX[i], listaProtivnikaY[i], zmaj_w/2, zmaj_h/2))
    

    while run:
        clock = pygame.time.Clock()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(a,(0,0))

        #vrijeme
        t1 = time.perf_counter()

        zmajPomakX = 0
        zmajPomakY = 0

        protivnikPomakY = screen.get_width() / 100

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            zmajPomakX = -1*(screen.get_width() / 80)
        if keys[pygame.K_d]:
            zmajPomakX = screen.get_width() / 80
        if keys[pygame.K_w]:
            zmajPomakY = -1*(screen.get_height() / 60)
        if keys[pygame.K_s]:
            zmajPomakY = screen.get_height() / 60

        #pomak igrača
        zmaj_x += zmajPomakX
        zmaj_y += zmajPomakY

        #ograničenja
        if zmaj_x < 0:
            zmaj_x = 0
        if zmaj_x + zmaj_w> screen.get_width():
            zmaj_x = screen.get_width() - zmaj_w
        if zmaj_y < 0:
            zmaj_y = 0
        if zmaj_y + zmaj_h> screen.get_height():
            zmaj_y = screen.get_height() - zmaj_h
        
        #vrijeme
        t2 = time.perf_counter()
        vrijeme = vrijeme + (t2-t1)*1000

        #stvaranje neprijatelja
        for i in range(brojProtivnika):
            listaProtivnikaY[i] += protivnikPomakY
            protivnikX = random.randint(0, screen.get_width()-zmaj_w/2)
            protivnik(listaProtivnikaX[i],listaProtivnikaY[i], i)

            if pygame.Rect(listaProtivnikaX[i], listaProtivnikaY[i], zmaj_w/2, zmaj_h/2).colliderect(pygame.Rect(zmaj_x,zmaj_y,zmaj_w,zmaj_h)):
                zmaj_x = 0
                zmaj_y = 0
        #crtanje zmaja
        igrac(zmaj_x,zmaj_y)

        pygame.display.update()
igra()
