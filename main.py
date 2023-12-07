import pygame
import random
import time
import os

pygame.init()

os.environ["SDL_VIDEO_CENTERED"]="1"
info=pygame.display.Info()
screen_width, screen_height=info.current_w,info.current_h
screen = pygame.display.set_mode((screen_width-(0.005*screen_width),screen_height-(0.06*screen_height)), pygame.RESIZABLE)
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

    #vrijeme
    vrijeme = 0
    t1 = time.perf_counter()
    #igrac varijable
    zmaj_h = screen.get_height() / 7
    zmaj_w = screen.get_width() / 12
    zmaj_x = screen.get_width() - (screen.get_width()/2) - (zmaj_w/2)
    zmaj_y = screen.get_height() - (screen.get_height()/6) - (zmaj_h /2)
    život = 3
    isHit = False

    #protivnik varijable
    ProtivnikX = []
    ProtivnikY = []
    protivnik_w = zmaj_w/2.5
    protivnik_h = zmaj_h/2.5
    protivnikPomakY = screen.get_width() / 100
    brojProtivnikaNaEkranu = 10
    brojačProtivnika = 0
    brojProtivnika = 100

    #pucanj
    ispaljeno = False

    #nova slika zmaja
    zmaj_slika = pygame.transform.scale(zmaj_slika_og, (zmaj_w, zmaj_h))
    protivnik_slika = pygame.transform.scale(protivnik_og, (protivnik_w, protivnik_h))

    def stvoriProtivnike():
        for i in range(brojProtivnikaNaEkranu):
            noviX = random.randint(0, int(screen.get_width()-protivnik_w)) #stvaranje x pozicije protivnika koja može bit od početka do kraja screena
            if i == 0: #za prvog protivnika uzima se bilo koji x
                ProtivnikX.append(noviX)
            else: #za ostale protivnike se uzima bilo koji x, ali ako je x u blizini prijašnjeg neprijatelja, bira se novi x. Tako neće doći do preklapanja protivnika
                while abs(ProtivnikX[i-1]-noviX) < protivnik_w*2:
                    noviX = random.randint(0, int(screen.get_width()-protivnik_w))
                else:
                    ProtivnikX.append(noviX)
            if i == 0: #uzima se određeni y na kome će se stvoriti 1. neprijatelj
                ProtivnikY.append(-protivnik_h*2)
            else: #ostali neprijatelji uzimaju prošli y i stvaraju se za istu visinu višu od prošloga
                ProtivnikY.append(ProtivnikY[i-1]-protivnik_h*2)

    def vratiProtivnika(i):
        ProtivnikY[i] = 0 -protivnik_h #vraća protivnika natrag gore (isti kod kao i kod spawnanja)
        noviX = random.randint(0, int(screen.get_width()-protivnik_w))
        while abs(ProtivnikX[i-1]-noviX) < protivnik_w*2:
            noviX = random.randint(0, int(screen.get_width()-protivnik_w))
        else:
            ProtivnikX[i] = noviX

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

        zmajPomakX = 0
        zmajPomakY = 0

        #pucanje varijable
        pucanj_w = zmaj_w/4
        pucanj_h = zmaj_h/4
        pucanjPomak = -protivnikPomakY

        def pucanje(x,y):
            pygame.draw.rect(screen, "yellow", pygame.Rect(x, y, pucanj_w, pucanj_h))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            zmajPomakX = -1*(screen.get_width() / 80)
        if keys[pygame.K_d]:
            zmajPomakX = screen.get_width() / 80
        if keys[pygame.K_w]:
            zmajPomakY = -1*(screen.get_height() / 60)
        if keys[pygame.K_s]:
            zmajPomakY = screen.get_height() / 60
        if keys[pygame.K_SPACE]:
            if ispaljeno == False:
                pucanje(zmaj_x+(zmaj_w/2), zmaj_y)
                ispaljeno = True

        #pomak pucnja
        if ispaljeno == True:
            pucanj_y += pucanjPomak
            pucanje(pucanj_x, pucanj_y)
        else:
            pucanj_y = zmaj_y
            pucanj_x = zmaj_x+(zmaj_w/2)

        #ograničenje pucnja
        if pucanj_y < 0:
            ispaljeno = False
            
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

        for i in range(brojProtivnikaNaEkranu): 
            ProtivnikY[i] += protivnikPomakY #micanje protivnika
            protivnik(ProtivnikX[i],ProtivnikY[i], i) #crtanje protivnika
            
            if ProtivnikY[i] > screen.get_height(): #respawnanje protivnika
                brojačProtivnika +=1
                if brojačProtivnika < brojProtivnika: #ograničenje da se ne respawnaju zauvijek
                    vratiProtivnika(i)
                
            if pygame.Rect(ProtivnikX[i], ProtivnikY[i], protivnik_w, protivnik_h).colliderect(pygame.Rect(zmaj_x,zmaj_y,zmaj_w,zmaj_h)) and isHit == False: #collision protivnika
                život -= 1
                isHit = True
                timer1 = vrijeme
            
            if pygame.Rect(ProtivnikX[i], ProtivnikY[i], protivnik_w, protivnik_h).colliderect(pygame.Rect(pucanj_x, pucanj_y, pucanj_w, pucanj_h)):
                ispaljeno = False
                brojačProtivnika +=1
                vratiProtivnika(i)
                

        if isHit == True: #ako pogođen
            if vrijeme - timer1 > 1:
                isHit = False
                protivnikPomakY = screen.get_width() / 100 #vraća brzinu neprijatelja
                zmaj_slika.set_alpha(256) #vraća transparency
            else:
                protivnikPomakY = screen.get_width() / 200 #usporava neprijatelje
                zmaj_slika.set_alpha(120) #stvara sliku transparentnu
                draw_text(f"{round(vrijeme - timer1,2)}s",text_font,(0,0,0),screen.get_width()/2,screen.get_height()/2)

        #crtanje zmaja
        igrac(zmaj_x,zmaj_y)

        #vrijeme
        t2 = time.perf_counter()
        vrijeme =round(t2-t1,2)
        draw_text(f"{vrijeme}s",text_font,(0,0,0),0,0)
        draw_text(f"{život} života",text_font,(0,0,0),0,100)

        pygame.display.update()
igra()
