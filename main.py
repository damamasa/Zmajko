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
    zmaj_h = screen.get_height() / 7
    zmaj_w = screen.get_width() / 12
    zmaj_x = screen.get_width() - (screen.get_width()/2) - (zmaj_w/2)
    zmaj_y = screen.get_height() - (screen.get_height()/6) - (zmaj_h /2)
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


        zmaj = pygame.draw.rect(screen, "red", pygame.Rect(zmaj_x, zmaj_y, zmaj_w, zmaj_h))
        pygame.display.update()
igra()
