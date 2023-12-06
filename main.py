import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Zmajevi")

#font i tekst
text_font = pygame.font.SysFont("Arial",50)
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

#slike
zmaj_slika_og = pygame.image.load("slike/zmaj.png")
pozadina = pygame.transform.scale(pygame.image.load("slike/pozadina.jpg"), (screen.get_width(), screen.get_height()))
protivnik_og = pygame.image.load("slike/birds.png")

def igra():
    run = True
    vrijeme = 0

    #igrac varijable
    zmaj_h = screen.get_height() / 7
    zmaj_w = screen.get_width() / 12
    zmaj_x = screen.get_width() - (screen.get_width()/2) - (zmaj_w/2)
    zmaj_y = screen.get_height() - (screen.get_height()/6) - (zmaj_h /2)

    #protivnik varijable
    ProtivnikX = []
    ProtivnikY = []
    protivnik_w = zmaj_w/2.5
    protivnik_h = zmaj_h/2.5
    brojProtivnika = 200

    #nova slika zmaja
    zmaj_slika = pygame.transform.scale(zmaj_slika_og, (zmaj_w, zmaj_h))
    protivnik_slika = pygame.transform.scale(protivnik_og, (protivnik_w, protivnik_h))

    def stvoriProtivnike():
        for i in range(brojProtivnika):
            noviX = random.randint(0, screen.get_width()-protivnik_w) #stvaranje x pozicije protivnika koja može bit od početka do kraja screena
            if i == 0: #za prvog protivnika uzima se bilo koji x
                ProtivnikX.append(noviX)
            else: #za ostale protivnike se uzima bilo koji x, ali ako je x u blizini prijašnjeg neprijatelja, bira se novi x. Tako neće doći do preklapanja protivnika
                while abs(ProtivnikX[i-1]-noviX) < protivnik_w*2:
                    noviX = random.randint(0, screen.get_width()-protivnik_w)
                else:
                    ProtivnikX.append(noviX)
            if i == 0: #uzima se određeni y na kome će se stvoriti 1. neprijatelj
                ProtivnikY.append(-protivnik_h*2)
            else: #ostali neprijatelji uzimaju prošli y i stvaraju se za istu visinu višu od prošloga
                ProtivnikY.append(ProtivnikY[i-1]-protivnik_h*2)

    def igrac(x,y):
        screen.blit(zmaj_slika, (x, y))
    
    def protivnik(x,y, i):
        screen.blit(protivnik_slika, (x, y))
    

    while run:
        clock = pygame.time.Clock()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(pozadina, (0,0))

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
        
        stvoriProtivnike() #stvaranje neprijatelja

        for i in range(brojProtivnika): #micanje i crtanje protivnika
            ProtivnikY[i] += protivnikPomakY
            protivnik(ProtivnikX[i],ProtivnikY[i], i)

            if pygame.Rect(ProtivnikX[i], ProtivnikY[i], protivnik_w, protivnik_h).colliderect(pygame.Rect(zmaj_x,zmaj_y,zmaj_w,zmaj_h)): #collision protivnika
                zmaj_x = 0
                zmaj_y = 0

        #crtanje zmaja
        igrac(zmaj_x,zmaj_y)

        #vrijeme
        t2 = time.perf_counter()
        vrijeme =round(vrijeme + ((t2-t1)*10),2)
        draw_text(f"{vrijeme}s",text_font,(0,0,0),0,0)

        pygame.display.update()
igra()
