import pygame
import random
import time
import os
import sys

class Button_Slika():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		surface.blit(self.image, (self.rect.x, self.rect.y))
		return action

class Button:
    def __init__(self, text_input, text_size, text_color, rectangle_width_and_height, rectangle_color, rectangle_hovering_color, position):
        self.text_input = text_input
        #rectangle ispod teksta
        self.rectangle = pygame.Rect((position[0]-(rectangle_width_and_height[0]/2), position[1]-(rectangle_width_and_height[1]/2)), rectangle_width_and_height)
        self.rectangle_color, self.rectangle_hovering_color = rectangle_color, rectangle_hovering_color
        #tekst u gumbu
        self.font = pygame.font.Font(None, text_size)
        self.text_surface = self.font.render(text_input, False, text_color)
        self.text_rectangle = self.text_surface.get_rect(center = self.rectangle.center)
    def update(self, screen):
        pygame.draw.rect(screen, self.rectangle_color, self.rectangle)
        screen.blit(self.text_surface, self.text_rectangle)
    def checkForCollision(self, mouse_position):
        if mouse_position[0] in range(self.rectangle.left, self.rectangle.right) and mouse_position[1] in range(self.rectangle.top, self.rectangle.bottom):
            return True
        return False
    def changeButtonColor(self):
        self.rectangle_color = self.rectangle_hovering_color
    def changeTextInput(self, new_text):
        self.text_input = new_text
        self.text_surface = self.font.render(self.text_input, False, (255, 255, 255))
        self.text_rectangle = self.text_surface.get_rect(center=self.rectangle.center)

def draw_text(text,font,text_col,x,y):
        img = font.render(text,True,text_col)
        screen.blit(img,(x,y))

def main():
    global screen, text_font, text_font2, text_font3, run, postignuce, ime, koji_user, text_font4
    pygame.init()

    #font i tekst
    text_font = pygame.font.SysFont("Arial",50, True)
    text_font2 = pygame.font.SysFont("Arial",80, True)
    text_font3 = pygame.font.SysFont("Arial",60, True)
    text_font4 = pygame.font.SysFont("Arial",40, True)
    screen = None
    postignuce = ["ne", "ne", "ne", "ne", "ne", "ne"]
    ime = ""
    koji_user = ""

    os.environ["SDL_VIDEO_CENTERED"]="1"
    info=pygame.display.Info()
    screen_width, screen_height=info.current_w,info.current_h
    screen = pygame.display.set_mode((screen_width-int(0.005*screen_width),screen_height-int(0.06*screen_height)), pygame.FULLSCREEN)
    pygame.display.set_caption("Zmajevi")

    run = False
    while not run:
        run = main_menu()

def brisanje_usera():
    global ime, level_state,postignuce,uništeniProtivnici
    ime =""
    level_state = "Level 1-1"
    postignuce = ["ne", "ne", "ne", "ne", "ne", "ne"]
    uništeniProtivnici = "0"
    spremi_igru()

def user_birac():
    global screen, text_font3, pozadina_slika, koji_user, ime, level_state,igraci
    pozadina_slika = pygame.image.load("users_bg.png")
    pozadina = pygame.Surface((screen.get_width(), screen.get_height()))
    pozadina.fill("Black")
    pozadina.set_alpha(100)
    screen.blit(pozadina, (0,0))
    screen.blit(pygame.transform.scale(pozadina_slika, (screen.get_width()*0.9, screen.get_height()*0.9)), (screen.get_width()/2-screen.get_width()*0.45, screen.get_height()/2-screen.get_height()*0.45))
    draw_text("Odaberi račun!",text_font3,"white",screen.get_width()*0.4,screen.get_height()*0.09)

    with open("igraci.txt", "r") as datoteka:
        a = datoteka.read()
    igraci = a.split("\n")
    for i, clan in enumerate(igraci):
        igraci[i] = clan.split("/")
    if koji_user != "":
        spremi_igru()

    text = ["","","","","",""]
    run = True
    while run == True:
        for i in range(6):
            if igraci[i][1] == "":
                text[i]= "[stvori račun]"
            else:
                text[i] = f"{igraci[i][1]} - {igraci[i][2]}"
        USER1_BUTTON = Button(text[0], 70, "Light Grey", (screen.get_width()*0.4, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.4, screen.get_height()*0.25))
        USER1_DELETE = Button(f"X", 70, "Red", (screen.get_width()*0.1, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.7, screen.get_height()*0.25))
        USER2_BUTTON = Button(text[1], 70, "Light Grey", (screen.get_width()*0.4, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.4, screen.get_height()*0.37))
        USER2_DELETE = Button(f"X", 70, "Red", (screen.get_width()*0.1, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.7, screen.get_height()*0.37))
        USER3_BUTTON = Button(text[2], 70, "Light Grey", (screen.get_width()*0.4, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.4, screen.get_height()*0.49))
        USER3_DELETE = Button(f"X", 70, "Red", (screen.get_width()*0.1, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.7, screen.get_height()*0.49))
        USER4_BUTTON = Button(text[3], 70, "Light Grey", (screen.get_width()*0.4, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.4, screen.get_height()*0.61))
        USER4_DELETE = Button(f"X", 70, "Red", (screen.get_width()*0.1, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.7, screen.get_height()*0.61))
        USER5_BUTTON = Button(text[4], 70, "Light Grey", (screen.get_width()*0.4, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.4, screen.get_height()*0.73))
        USER5_DELETE = Button(f"X", 70, "Red", (screen.get_width()*0.1, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.7, screen.get_height()*0.73))
        USER6_BUTTON = Button(text[5], 70, "Light Grey", (screen.get_width()*0.4, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.4, screen.get_height()*0.85))
        USER6_DELETE = Button(f"X", 70, "Red", (screen.get_width()*0.1, screen.get_height()/9), "#0f3236", "#50908c", (screen.get_width()*0.7, screen.get_height()*0.85))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for gumb in [USER1_BUTTON, USER2_BUTTON, USER3_BUTTON, USER4_BUTTON, USER5_BUTTON, USER6_BUTTON,USER1_DELETE,USER2_DELETE,USER3_DELETE,USER4_DELETE,USER5_DELETE,USER6_DELETE]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spremi_igru()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if USER1_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    koji_user = "1"
                    load_igru()
                if USER1_DELETE.checkForCollision(MENU_MOUSE_POS):
                    koji_user ="1"
                    brisanje_usera()
                    USER1_BUTTON.changeTextInput(f"{igraci[0][1]}({igraci[0][2]})")
                if USER2_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    koji_user = "2"
                    load_igru()
                if USER2_DELETE.checkForCollision(MENU_MOUSE_POS):
                    koji_user ="2"
                    brisanje_usera()
                    USER2_BUTTON.changeTextInput(f"{igraci[1][1]}({igraci[1][2]})")
                if USER3_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    koji_user = "3"
                    load_igru()
                if USER3_DELETE.checkForCollision(MENU_MOUSE_POS):
                    koji_user ="3"
                    brisanje_usera()
                    USER3_BUTTON.changeTextInput(f"{igraci[2][1]}({igraci[2][2]})")
                if USER4_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    koji_user = "4"
                    load_igru()
                if USER4_DELETE.checkForCollision(MENU_MOUSE_POS):
                    koji_user ="4"
                    brisanje_usera()
                    USER4_BUTTON.changeTextInput(f"{igraci[3][1]}({igraci[3][2]})")
                if USER5_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    koji_user = "5"
                    load_igru()
                if USER5_DELETE.checkForCollision(MENU_MOUSE_POS):
                    koji_user ="5"
                    brisanje_usera()
                    USER5_BUTTON.changeTextInput(f"{igraci[4][1]}({igraci[4][2]})")
                if USER6_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    koji_user = "6"
                    load_igru()
                if USER6_DELETE.checkForCollision(MENU_MOUSE_POS):
                    koji_user ="6"
                    brisanje_usera()
                    USER6_BUTTON.changeTextInput(f"{igraci[5][1]}({igraci[5][2]})")

        pygame.display.update()

def player_name():
    global screen, ime, level_state, postignuce, igraci, uništeniProtivnici
    ime = ""
    font = pygame.font.Font(None, 60)
    text_box1 = pygame.Rect(screen.get_width()*0.45, screen.get_height()*0.5, screen.get_width()*0.1, screen.get_height()*0.05)
    pozadina = pygame.Surface((screen.get_width(), screen.get_height()))
    pozadina.fill("Black")
    pozadina.set_alpha(100)
    screen.blit(pozadina, (0,0))
    screen.blit(pygame.transform.scale(pozadina_slika, (screen.get_width()*0.7, screen.get_height()*0.7)), (screen.get_width()/2-screen.get_width()*0.35, screen.get_height()/2-screen.get_height()*0.35))
    run = True
    while run == True:
        screen.blit(pozadina_slika,(0,0)) 
        pygame.draw.rect(screen,"black", text_box1, 3)
        surf1 = font.render(ime,True,'white')
        screen.blit(surf1, (text_box1.x + 5, text_box1.y + 5))
        text_box1.w = max(200, surf1.get_width()+10)
        draw_text("Unesi ime:",font,"white",screen.get_width()/2.25,screen.get_height()/2.5)
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        POTVRDA_BUTTON = Button(f"Potvrdi", 50, "white", (screen.get_width()/8, screen.get_height()/8), "#0f3236", "#50908c", (screen.get_width()/2, screen.get_height()/1.5))
        for gumb in [POTVRDA_BUTTON]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spremi_igru()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if POTVRDA_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    if len(ime) > 0 and len(ime) < 10:
                        with open("igraci.txt", "r") as datoteka:
                            a = datoteka.read()
                        igraci = a.split("\n")
                        for i, clan in enumerate(igraci):
                            igraci[i] = clan.split("/")
                        igraci[int(koji_user)-1][1] = ime
                        level_state = igraci[int(koji_user)-1][2]
                        postignuce[0] = igraci[int(koji_user)-1][3]
                        postignuce[1] = igraci[int(koji_user)-1][4]
                        postignuce[2] = igraci[int(koji_user)-1][5]
                        postignuce[3] = igraci[int(koji_user)-1][6]
                        postignuce[4] = igraci[int(koji_user)-1][7]
                        postignuce[5] = igraci[int(koji_user)-1][8]
                        uništeniProtivnici = int(igraci[int(koji_user)-1][9])
                        run = False
                        main_menu()
                    else:
                        draw_text("Upiši ime duljine 1-9 slova",text_font3,"black",screen.get_width()/3,screen.get_height()*0.8)
                        pygame.display.update()
                        time.sleep(1.5)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    ime = ime[:-1]
                else:
                    ime += event.unicode
        pygame.display.update()

def postignuca():
    global screen, text_font,postignuce, text_font4
    bg = pygame.transform.scale(pygame.image.load("users_bg.png"), (screen.get_width()*0.9, screen.get_height()*0.9))

    tekst=[["Neprobojni štit","Preživi neprekidni napad neprijatelja bez gubitaka zdravlja."], ["Branič Svemira", "Uništi 100 protivničkih trupa."], ["Gospodar Svjetova","Prođi sve svjetove i postani nepobjedivi letač."],["HoHoHo", "Prođi božićni level."], ["Apsolutni Pobjednik", "Prođi nemogući svijet."], ["Zmajkova Legenda", "Otključaj sva postignuća da postaneš legenda poput Zmajka."]]
    run = True
    while run:
        screen.blit(bg, (screen.get_width()*0.05, screen.get_height()*0.05))
        for i in range(len(postignuce)):
            if postignuce[i] == "da":
                draw_text(tekst[i][0],text_font3,"green",screen.get_width()/10,screen.get_height()*0.05+(i*screen.get_height()/6.5))
                draw_text(tekst[i][1],text_font4,"green",screen.get_width()/10,screen.get_height()*0.11+(i*screen.get_height()/6.5))
            else:
                draw_text(tekst[i][0],text_font3,"red",screen.get_width()/10,screen.get_height()*0.05+(i*screen.get_height()/6.5))
                draw_text(tekst[i][1],text_font4,"red",screen.get_width()/10,screen.get_height()*0.11+(i*screen.get_height()/6.5))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MAIN_GUMB = Button("Vrati se", 70, "Black", (220, 120), "Light Grey", "Red", (screen.get_width()*0.85, screen.get_height()*0.85))
        draw_text(f"Ostvareno: {postignuce.count('da')} / {len(postignuce)}",text_font,"black",screen.get_width()*0.72,screen.get_height()*0.08)
        for gumb in [MAIN_GUMB]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit() 
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_p or event.key == pygame.K_ESCAPE):
                run = False
                main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_GUMB.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    main_menu()

        pygame.display.update()

def spremi_igru():
    global igraci, koji_user, ime,level_state, output, uništeniProtivnici, postignuce
    igraci[int(koji_user)-1] = [koji_user,ime,level_state,postignuce[0],postignuce[1],postignuce[2],postignuce[3],postignuce[4],postignuce[5],str(uništeniProtivnici)]
    output = ""
    for i in range(len(igraci)):
        for l in range(len(igraci[i])):
            output += igraci[i][l]+"/"
        output = output[0:len(output)-1]
        output += "\n"
    with open("igraci.txt","w") as datoteka:
        datoteka.write(output)

def load_igru():
    global koji_user, ime, level_state,postignuce,igraci, uništeniProtivnici
    if igraci[int(koji_user)-1][1] == "":
        player_name()
    else:
        level_state = igraci[int(koji_user)-1][2]
        postignuce[0] = igraci[int(koji_user)-1][3]
        postignuce[1] = igraci[int(koji_user)-1][4]
        postignuce[2] = igraci[int(koji_user)-1][5]
        postignuce[3] = igraci[int(koji_user)-1][6]
        postignuce[4] = igraci[int(koji_user)-1][7]
        postignuce[5] = igraci[int(koji_user)-1][8]
        uništeniProtivnici = int(igraci[int(koji_user)-1][9])
        ime = igraci[int(koji_user)-1][1]
        main_menu()

def main_menu():
    global screen, text_font3, text_font2, skinovi, skin_brojac, igraci, impossible_state, odabrani_level, replay_state, bozic_state
    zmajko_pozadina = pygame.transform.scale(pygame.image.load("p.jpg"), (screen.get_width(), screen.get_height()))
    skin1 = pygame.transform.scale(pygame.image.load("zmaj.png"), (screen.get_width()*0.2265, screen.get_height()*0.365))
    skin2 = pygame.transform.scale(pygame.image.load("zmaj2-leti.png"), (screen.get_width()*0.2265, screen.get_height()*0.365))
    skin3 = pygame.transform.scale(pygame.image.load("zmaj3.png"), (screen.get_width()*0.2265, screen.get_height()*0.365))
    skin_brojac = 0
    skinovi = [skin1, skin2, skin3]
    arrow = pygame.transform.rotate(pygame.image.load("arrow.png"),90)
    strijelica1 = Button_Slika(screen.get_width()/8.52,screen.get_height()*0.85,arrow, 0.1)
    strijelica2 = Button_Slika(screen.get_width()/4,screen.get_height()*0.85,pygame.transform.flip(arrow, True, False), 0.1)
    impossible_state = False
    bozic_state = False
    run = True
    
    while run == True:
        screen.blit(zmajko_pozadina, (0,0))    
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #gumbovi na desnoj strani
        IGRAJ_GUMB = Button("Kampanja", 70, "gold", (screen.get_width()/3.5, screen.get_height()/11.5), "#0f3236", "#50908c", (screen.get_width()*0.8, screen.get_height()*0.31))
        LEVEL_GUMB = Button("Nemoguć level", 70, "White", (screen.get_width()/3.5, screen.get_height()/11.5), "#0f3236", "#50908c", (screen.get_width()*0.8, screen.get_height()*0.42))
        BOZIC_GUMB = Button("Božićni level", 70, "White", (screen.get_width()/3.5, screen.get_height()/11.5), "#0f3236", "#50908c", (screen.get_width()*0.8, screen.get_height()*0.53))
        TUTORIAL_BUTTON = Button("Kako igrati?", 70, "White", (screen.get_width()/3.5, screen.get_height()/11.5), "#0f3236", "#50908c", (screen.get_width()*0.8, screen.get_height()*0.64))
        ACHIEVEMENTS_GUMB = Button("Postignuća", 70, "White", (screen.get_width()/3.5, screen.get_height()/11.5), "#0f3236", "#50908c", (screen.get_width()*0.8, screen.get_height()*0.75))
        QUIT_BUTTON = Button("Izađi", 70, "White", (screen.get_width()/3.5, screen.get_height()/11.5), "#0f3236", "#50908c", (screen.get_width()*0.8, screen.get_height()*0.86))
        USERS_BUTTON = Button("Promijeni igrača", 50, "Red", (screen.get_width()/5.5, screen.get_height()/20), "#0f3236", "darksalmon", (screen.get_width()*0.2, screen.get_height()/2.8))
        for gumb in [IGRAJ_GUMB, QUIT_BUTTON, LEVEL_GUMB, ACHIEVEMENTS_GUMB, USERS_BUTTON, BOZIC_GUMB, TUTORIAL_BUTTON]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)
        
        #skinovi
        screen.blit(skinovi[skin_brojac], (screen.get_width()*0.077, screen.get_height()*0.5))
        if strijelica1.draw(screen):
            skin_brojac -=1
        if strijelica2.draw(screen):
            skin_brojac +=1
        if skin_brojac >= len(skinovi): #da se vrti odabir u krug
            skin_brojac = 0
        elif skin_brojac < 0:
            skin_brojac = len(skinovi)-1

        #ime igrača i user profile
        if ime == "":
            user_birac()
        else:
            draw_text(f"{ime}",text_font3,(0,0,0),screen.get_width()/7,screen.get_height()/6)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spremi_igru()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if IGRAJ_GUMB.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    level_menu()
                if USERS_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    user_birac()
                if QUIT_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    spremi_igru()
                    pygame.quit()
                    sys.exit()
                if ACHIEVEMENTS_GUMB.checkForCollision(MENU_MOUSE_POS):
                    postignuca()
                if LEVEL_GUMB.checkForCollision(MENU_MOUSE_POS):
                    impossible_state = True
                    odabrani_level = "NEĆEŠ PREŽIVJETI"
                    replay_state = False
                    impossibleLevel()
                if BOZIC_GUMB.checkForCollision(MENU_MOUSE_POS):
                    bozic_state = True
                    odabrani_level = "Sretan Božić!"
                    replay_state = False
                    bozicLevel()
                if TUTORIAL_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    tutorial()

        pygame.display.update()

def tutorial():
    global screen, text_font, pozadina_slika
    pozadina_slika = pygame.image.load("users_bg.png")
    pozadina = pygame.Surface((screen.get_width(), screen.get_height()))
    pozadina.fill("Black")
    pozadina.set_alpha(100)
    screen.blit(pozadina, (0,0))
    screen.blit(pygame.transform.scale(pozadina_slika, (screen.get_width()*0.9, screen.get_height()*0.9)), (screen.get_width()/2-screen.get_width()*0.45, screen.get_height()/2-screen.get_height()*0.45))
    draw_text("Kako igrati",text_font,"white",screen.get_width()/2.35,screen.get_height()/8)
    tutorial_tekst = ["W - gore", "A - lijevo", "S - dolje", "D - desno", "SPACE - pucanje", "Lijevi klik/Desni klik - mijenjanje powerupova", "P/ESC - pauza"]
    for i in range(len(tutorial_tekst)):
        draw_text(tutorial_tekst[i],text_font,"white",screen.get_width()/5,screen.get_height()*(0.2+(0.1*i)))
    run = True
    while run == True:
        NASTAVI_BUTTON = Button("Vrati se ->", 70, "white", (screen.get_width()/4, screen.get_height()/10), "#0f3236", "#50908c", (screen.get_width()*0.8, screen.get_height()*0.85))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for gumb in [NASTAVI_BUTTON]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spremi_igru()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NASTAVI_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def pause_menu():
    global run, screen, text_font, tp1, tp2, tp
    tp1 = time.perf_counter()
    paused = True
    pozadina = pygame.Surface((screen.get_width(), screen.get_height()))
    pozadina.fill("Black")
    pozadina.set_alpha(100)
    screen.blit(pozadina, (0,0))
    while paused:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        pauzirano_logo = pygame.transform.scale(pygame.image.load("pauzirano_logo.png"), (screen.get_width()/3, screen.get_height()/5))
        PLAY_BUTTON = Button("Igraj ponovno", 70, "black", (screen.get_width()*0.25, screen.get_height()*0.14), "Light Grey", "Green", (screen.get_width()/2, screen.get_height()/2))
        MAIN_BUTTON = Button("Glavni izbornik", 70, "black", (screen.get_width()*0.25, screen.get_height()*0.14), "Light Grey", "dimgray", (screen.get_width()/2, screen.get_height()/1.5))
        QUIT_BUTTON = Button("Izađi", 70, "black", (screen.get_width()*0.25, screen.get_height()*0.14), "Light Grey", "Red", (screen.get_width()/2, screen.get_height()/1.2))

        screen.blit(pauzirano_logo, (screen.get_width()/3,screen.get_height()/10))

        for gumb in [PLAY_BUTTON, QUIT_BUTTON, MAIN_BUTTON]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spremi_igru()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    tp2 = time.perf_counter()
                    tp += (tp2-tp1)
                    paused = False
                if QUIT_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    spremi_igru()
                    pygame.quit()
                    sys.exit()
                if MAIN_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    paused = False
                    main_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    tp2 = time.perf_counter()
                    tp += (tp2-tp1)
                    paused = False

        pygame.display.update()

def game_over(): 
    global screen, text_font
    pozadina = pygame.Surface((screen.get_width(), screen.get_height()))
    pozadina.fill("Black")
    pozadina.set_alpha(100)
    screen.blit(pozadina, (0,0))
    run = True
    while run == True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BUTTON = Button("Igraj ponovno", 70, "black", (screen.get_width()*0.25, screen.get_height()*0.14), "Light Grey", "Green", (screen.get_width()/2, screen.get_height()/2))
        MAIN_BUTTON = Button("Glavni izbornik", 70, "black", (screen.get_width()*0.25, screen.get_height()*0.14), "Light Grey", "dimgray", (screen.get_width()/2, screen.get_height()/1.5))
        QUIT_BUTTON = Button("Izađi", 70, "black", (screen.get_width()*0.25, screen.get_height()*0.14), "Light Grey", "Red", (screen.get_width()/2, screen.get_height()/1.2))
        
        kraj_logo = pygame.transform.scale(pygame.image.load("kraj_logo.png"), (screen.get_width()/3, screen.get_height()/5))
        screen.blit(kraj_logo, (screen.get_width()/3,screen.get_height()/10))

        for gumb in [PLAY_BUTTON,MAIN_BUTTON, QUIT_BUTTON]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spremi_igru()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    igra()
                if QUIT_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    spremi_igru()
                    pygame.quit()
                    sys.exit()
                if MAIN_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    main_menu()

        pygame.display.update()

def promijeni_level():
    global level_state, brojPtica, brzinaStvaranja, final_vrijeme, avioni_state, meteori_state, vjetar_state, brojAviona, brojMeteora, brojVjetra, vanzemaljac_state, brojVanzemaljca, pozadina, replay_state, odabrani_level
    if (level_state == "Level 1-1" and replay_state == False) or (odabrani_level == "Level 1-1" and replay_state == True): #leveli igrice
        pozadina = pygame.transform.scale(pygame.image.load("world1_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 20
        brzinaStvaranja = 2.5
        final_vrijeme = 20
        avioni_state=False
        meteori_state = False
        vjetar_state = False
        vanzemaljac_state = False
    elif (level_state == "Level 1-2" and replay_state == False) or (odabrani_level == "Level 1-2" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("world1_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 20
        brzinaStvaranja = 1.5
        final_vrijeme = 20
        avioni_state=False
        meteori_state = False
        vjetar_state = False
        vanzemaljac_state = False
    elif (level_state == "Level 2-1" and replay_state == False) or (odabrani_level == "Level 2-1" and replay_state == True):   
        pozadina = pygame.transform.scale(pygame.image.load("world2_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 20
        brzinaStvaranja = 2
        final_vrijeme = 20
        avioni_state=True
        meteori_state = False
        vjetar_state = False
        vanzemaljac_state = False
        brojAviona = 3
    elif (level_state == "Level 2-2" and replay_state == False) or (odabrani_level == "Level 2-2" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("world2_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 20
        brzinaStvaranja = 1.5
        final_vrijeme = 20
        avioni_state=True
        meteori_state = False
        vjetar_state = False
        vanzemaljac_state = False
        brojAviona = 5
    elif (level_state == "Level 3-1" and replay_state == False) or (odabrani_level == "Level 3-1" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("world3_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 10
        brzinaStvaranja = 2.5
        final_vrijeme = 20
        avioni_state=True
        meteori_state = True
        vjetar_state = False
        vanzemaljac_state = False
        brojAviona = 3
        brojMeteora = 3
    elif (level_state == "Level 3-2" and replay_state == False) or (odabrani_level == "Level 3-2" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("world3_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 15
        brzinaStvaranja = 2.5
        final_vrijeme = 20
        avioni_state=True
        meteori_state = True
        vjetar_state = False
        vanzemaljac_state = False
        brojAviona = 4
        brojMeteora = 5
    elif (level_state == "Level 4-1" and replay_state == False) or (odabrani_level == "Level 4-1" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("world4_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 10
        brzinaStvaranja = 2
        final_vrijeme = 20
        avioni_state=True
        meteori_state = True
        vjetar_state = True
        vanzemaljac_state = False
        brojAviona = 3
        brojMeteora = 4
        brojVjetra = 1
    elif (level_state == "Level 4-2" and replay_state == False) or (odabrani_level == "Level 4-2" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("world4_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 10
        brzinaStvaranja = 2
        final_vrijeme = 20
        avioni_state=True
        meteori_state = True
        vjetar_state = True
        vanzemaljac_state = False
        brojAviona = 3
        brojMeteora = 5
        brojVjetra = 2
    elif (level_state == "Level 5-1" and replay_state == False) or (odabrani_level == "Level 5-1" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("world5_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 20
        brzinaStvaranja = 1.5
        final_vrijeme = 20
        avioni_state=False
        meteori_state = False
        vjetar_state = True
        vanzemaljac_state = True
        brojAviona = 5
        brojMeteora = 5
        brojVjetra = 1
        brojVanzemaljca = 3
    elif (level_state == "Level 5-2" and replay_state == False) or (odabrani_level == "Level 5-2" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("world5_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 20
        brzinaStvaranja = 1.5
        final_vrijeme = 20
        avioni_state=True
        meteori_state = True
        vjetar_state = True
        vanzemaljac_state = True
        brojAviona = 5
        brojMeteora = 5
        brojVjetra = 1
        brojVanzemaljca = 5

def impossibleLevel():
    global brojPtica, brzinaStvaranja, final_vrijeme, avioni_state, meteori_state, vjetar_state, brojAviona, brojMeteora, brojVjetra, vanzemaljac_state, brojVanzemaljca, pozadina, impossible_state
    pozadina = pygame.transform.scale(pygame.image.load("world5_bg.jpg"), (screen.get_width(), screen.get_height()))
    brojPtica = 20
    brzinaStvaranja = 1.5
    final_vrijeme = 20
    avioni_state=True
    meteori_state = True
    vjetar_state = True
    vanzemaljac_state = True
    brojAviona = 5
    brojMeteora = 5
    brojVjetra = 1
    brojVanzemaljca = 5
    igra()

def bozicLevel():
    global brojPtica, brzinaStvaranja, final_vrijeme, avioni_state, meteori_state, vjetar_state, brojAviona, brojMeteora, brojVjetra, vanzemaljac_state, brojVanzemaljca, pozadina, impossible_state
    pozadina = pygame.transform.scale(pygame.image.load("world5_bg.jpg"), (screen.get_width(), screen.get_height()))
    brojPtica = 15
    brzinaStvaranja = 1.5
    final_vrijeme = 20
    avioni_state=True
    meteori_state = True
    vjetar_state = True
    vanzemaljac_state = True
    brojAviona = 3
    brojMeteora = 3
    brojVjetra = 1
    brojVanzemaljca = 2
    igra()

def level_menu():
    global screen, text_font, text_font2, level_state, replay_state, odabrani_level
    pozadina_y = int(level_state[-3])
    arrow = pygame.image.load("arrow.png")
    run = True
    odabrani_level = level_state
    replay_state = False
    while run == True:
        if pozadina_y == 1: #pozicija leveli slike po svijetovima
            leveli_pozadina = pygame.transform.scale(pygame.image.load("level_wrd1.jpg"), (screen.get_width(), screen.get_height()))
            LEVEL1_GUMB = Button("1-1", 70, "black", (screen.get_width()*0.078, screen.get_height()*0.128), "Light Grey", "Green", (screen.get_width()*0.312, screen.get_height()*0.73))
            LEVEL2_GUMB = Button("1-2", 70, "black", (screen.get_width()*0.078, screen.get_height()*0.128), "Light Grey", "Green", (screen.get_width()*0.6825, screen.get_height()*0.345))
        elif pozadina_y == 2:
            leveli_pozadina = pygame.transform.scale(pygame.image.load("level_wrd2.jpg"), (screen.get_width(), screen.get_height()))
            LEVEL1_GUMB = Button("2-1", 70, "black", (screen.get_width()*0.078, screen.get_height()*0.128), "Light Grey", "Green", (screen.get_width()*0.68, screen.get_height()*0.665))
            LEVEL2_GUMB = Button("2-2", 70, "black", (screen.get_width()*0.078, screen.get_height()*0.128), "Light Grey", "Green", (screen.get_width()*0.312, screen.get_height()*0.285))
        elif pozadina_y == 3:
            leveli_pozadina = pygame.transform.scale(pygame.image.load("level_wrd3.jpg"), (screen.get_width(), screen.get_height()))
            LEVEL1_GUMB = Button("3-1", 70, "black", (screen.get_width()*0.078, screen.get_height()*0.128), "Light Grey", "Green", (screen.get_width()*0.312, screen.get_height()*0.73))
            LEVEL2_GUMB = Button("3-2", 70, "black", (screen.get_width()*0.078, screen.get_height()*0.128), "Light Grey", "Green", (screen.get_width()*0.6825, screen.get_height()*0.345))
        elif pozadina_y == 4:
            leveli_pozadina = pygame.transform.scale(pygame.image.load("level_wrd4.jpg"), (screen.get_width(), screen.get_height()))
            LEVEL1_GUMB = Button("4-1", 70, "black", (screen.get_width()*0.078, screen.get_height()*0.128), "Light Grey", "Green", (screen.get_width()*0.6825, screen.get_height()*0.73))
            LEVEL2_GUMB = Button("4-2", 70, "black", (screen.get_width()*0.078, screen.get_height()*0.128), "Light Grey", "Green", (screen.get_width()*0.312, screen.get_height()*0.345))
        elif pozadina_y == 5:
            leveli_pozadina = pygame.transform.scale(pygame.image.load("level_wrd5.jpg"), (screen.get_width(), screen.get_height()))
            LEVEL1_GUMB = Button("5-1", 70, "black", (screen.get_width()*0.078, screen.get_height()*0.128), "Light Grey", "Green", (screen.get_width()*0.32, screen.get_height()*0.655))
            LEVEL2_GUMB = Button("5-2", 70, "black", (screen.get_width()*0.078, screen.get_height()*0.128), "Light Grey", "Green", (screen.get_width()*0.69, screen.get_height()*0.28))
        screen.blit(leveli_pozadina, (0,0))
        gore_arrow = Button_Slika(screen.get_width()*0.45,screen.get_height()*0.05,arrow, 0.3)
        dolje_arrow = Button_Slika(screen.get_width()*0.45,screen.get_height()*0.85,pygame.transform.flip(arrow, False, True), 0.3)
        if pozadina_y != 5:
            if gore_arrow.draw(screen) and pozadina_y < 5:
                pozadina_y +=1
                time.sleep(0.2)
        if pozadina_y != 1:
            if dolje_arrow.draw(screen) and pozadina_y > 1:
                pozadina_y -=1
                time.sleep(0.2)

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        IGRAJ_GUMB = Button("Nastavi", 70, "White", (screen.get_width()*0.15, screen.get_height()*0.12), "#0f3236", "#50908c", (screen.get_width()*0.9, screen.get_height()*0.9))
        MAIN_GUMB = Button("Vrati se", 70, "White", (screen.get_width()*0.15, screen.get_height()*0.12), "#0f3236", "#50908c", (screen.get_width()*0.1, screen.get_height()*0.9))
        if pozadina_y == 1 or pozadina_y == 2:
            draw_text(odabrani_level,text_font2,"black",screen.get_width()*0.81,screen.get_height()*0.73)
        else:
            draw_text(odabrani_level,text_font2,"Light Grey",screen.get_width()*0.81,screen.get_height()*0.73)

        for gumb in [IGRAJ_GUMB, MAIN_GUMB, LEVEL1_GUMB, LEVEL2_GUMB]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)
               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spremi_igru()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if IGRAJ_GUMB.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    promijeni_level()
                    igra()
                if MAIN_GUMB.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    main_menu()
                if LEVEL1_GUMB.checkForCollision(MENU_MOUSE_POS):
                    if LEVEL1_GUMB.text_input[0] <= level_state[-3]:
                        if LEVEL1_GUMB.text_input[-1] <= level_state[-1]:
                            odabrani_level = "Level "+LEVEL1_GUMB.text_input
                            replay_state = True
                        else:
                            draw_text(f"Otključaj level prije.",text_font,(0,0,0),screen.get_width()/3,screen.get_height()/3)
                            pygame.display.update()
                            time.sleep(2) 
                    else:
                        draw_text(f"Otključaj level prije.",text_font,(0,0,0),screen.get_width()/3,screen.get_height()/3)
                        pygame.display.update()
                        time.sleep(2) 
                if LEVEL2_GUMB.checkForCollision(MENU_MOUSE_POS):
                    if LEVEL2_GUMB.text_input[0] < level_state[-3]:
                        odabrani_level = "Level "+LEVEL2_GUMB.text_input
                        replay_state = True
                    elif LEVEL2_GUMB.text_input[0] == level_state[-3]:
                        if LEVEL2_GUMB.text_input[-1] < level_state[-1]:
                            odabrani_level = "Level "+LEVEL2_GUMB.text_input
                            replay_state = True
                        elif LEVEL2_GUMB.text_input[-1] == level_state[-1]:
                            odabrani_level = "Level "+LEVEL2_GUMB.text_input
                            replay_state = False
                        else:
                            draw_text(f"Otključaj level prije.",text_font,(0,0,0),screen.get_width()/3,screen.get_height()/3)
                            pygame.display.update()
                            time.sleep(1.5)
                    else:
                        draw_text(f"Otključaj level prije.",text_font,(0,0,0),screen.get_width()/3,screen.get_height()/3)
                        pygame.display.update()
                        time.sleep(1.5)

        pygame.display.update()

def igra():
    global run, tp, screen, text_font, brojPtica, brzinaStvaranja, final_vrijeme, avioni_state, meteori_state, vjetar_state, brojMeteora, brojVjetra, pozadina, skin_brojac, skinovi, level_state,uništeniProtivnici, postignuce,impossible_state,bozic_state
    #slike
    zmaj_slika_og = skinovi[skin_brojac] #slika zmaja po skinu
    protivnik_og = pygame.image.load("birds.png")
    sidebar = pygame.transform.scale(pygame.image.load("sidebar.png"), (screen.get_width()*0.1651, screen.get_height()))
    sidebar1 = pygame.transform.scale(pygame.image.load("sidebar1.png"), (screen.get_width()*0.1651, screen.get_height()))
    sidebar2 = pygame.transform.scale(pygame.image.load("sidebar2.png"), (screen.get_width()*0.1651, screen.get_height()))
    sidebar3 = pygame.transform.scale(pygame.image.load("sidebar3.png"), (screen.get_width()*0.1651, screen.get_height()))
    sidebar4 = pygame.transform.scale(pygame.image.load("sidebar4.png"), (screen.get_width()*0.1651, screen.get_height()))
    zmaj_menu = pygame.transform.scale(zmaj_slika_og, (screen.get_width()*0.045, screen.get_height()*0.085))
    srce = pygame.transform.scale(pygame.image.load("srce.png"), (screen.get_width()*0.045, screen.get_height()*0.07))
    fireball_og = pygame.image.load("fireball.png")
    fireball_menu = pygame.transform.scale(fireball_og, (screen.get_width()*0.055, screen.get_height()*0.095))
    avion_og = pygame.image.load("avion.png")
    meteor_og = pygame.image.load("meteor.png")
    vjetar_og = pygame.image.load("vjetar.png")
    vanzemaljac_og = pygame.image.load("alien.png")
    vanzemaljac_pucanj_og = pygame.image.load("purple.png")
    powerup2_og = pygame.image.load("blue.png")
    powerup2_menu = pygame.transform.scale(powerup2_og, (screen.get_width()*0.055, screen.get_height()*0.095))
    powerup3_og = pygame.image.load("powerup3.png")
    powerup3_menu = pygame.transform.scale(powerup3_og, (screen.get_width()*0.050, screen.get_height()*0.095))
    powerup4_menu = pygame.transform.scale(pygame.image.load("3balls.png"), (screen.get_width()*0.065, screen.get_height()*0.1))
    nema_sign = pygame.transform.scale(pygame.image.load("nema.png"), (screen.get_width()*0.06, screen.get_height()*0.1))
    nema_sign.set_alpha(150)

    #aktivacija powerupova određeni po svijetu
    if level_state[-3] == "1": #koji svijet
        powerups = 0
        power_birac = -1
    if level_state[-3] == "2": 
        powerups = 1
        power_birac = 0
    elif level_state[-3] == "3":
        powerups = 2
        power_birac = 1
    elif level_state[-3] == "4":
        powerups = 3
        power_birac = 2
    elif level_state[-3] == "5":
        powerups = 4
        power_birac = 3

    #vrijeme
    vrijeme = 0
    t1 = time.perf_counter()
    tp = 0
    #igrac varijable
    zmaj_h = screen.get_height() / 7
    zmaj_w = screen.get_width() / 12
    zmaj_x = screen.get_width() - (screen.get_width()/2) - (zmaj_w/2)
    zmaj_y = screen.get_height() - (screen.get_height()/6) - (zmaj_h /2)
    život = 2
    isHit = False

    #protivnik PTICA varijable
    ProtivnikX = []
    ProtivnikY = []
    ProtivnikW = []
    ProtivnikH = []
    ProtivnikSlika = []
    protivnikPomakY = []

    #protivnik AVION varijable
    AvionX = []
    AvionY = []
    AvionW = []
    AvionH = []
    AvionSlika = []
    AvionPomakX = []

    #protivnik METEOR varijable
    MeteorX = []
    MeteorY = []
    MeteorW = []
    MeteorH = []
    MeteorSlika = []
    MeteorPomakX = []
    MeteorPomakY = []

    #protivnik VJETAR varijable
    VjetarX = []
    VjetarY = []
    VjetarW = []
    VjetarH = []
    VjetarSlika = []
    VjetarPomakX = []

    #protivnik VANZEMALJAC varijable
    VanzemaljacX = []
    VanzemaljacY = []
    VanzemaljacW = []
    VanzemaljacH = []
    VanzemaljacSlika = []
    VanzemaljacPomakX = []
    VanzemaljacPomakY = []

    #vanzemaljac pucanje
    VanzemaljacPucanjX = []
    VanzemaljacPucanjY = []
    VanzemaljacPucanjPomakY = []
    vanzemaljac_pucanje = []

    #pucanj
    ispaljeno1 = False
    ispaljeno2 = False
    ispaljeno3 = False
    ispaljeno4 = False
    timer_cooldown1 = -100 
    timer_cooldown2 = -100
    timer_cooldown3 = -100
    timer_cooldown4 = -100
    cooldown1 = 3
    cooldown2 = 5
    cooldown3 = 15
    cooldown4 = 7
    power4_x = [0,0,0]
    power4_y = [0,0,0]

    #PRVI POWERUP
    power1_w = zmaj_w/4
    power1_h = zmaj_h/4
    pucanjPomak = -1*(screen.get_height() / 60)

    #DRUGI POWERUP
    power2_w = zmaj_w/2
    power2_h = zmaj_h/2
    pucanjPomak = -1*(screen.get_height() / 60)

    #TRECI POWERUP
    power3_w = zmaj_w*1.25
    power3_h = zmaj_h*1.5
    pucanjPomak = -1*(screen.get_height() / 60)

    #CETVRTI POWERUP
    power4_w = zmaj_w/3.5
    power4_h = zmaj_h/3.5

    #nova slika zmaja
    zmaj_slika = pygame.transform.scale(zmaj_slika_og, (zmaj_w, zmaj_h))

    def stvoriProtivnike(): 
        for i in range(brojPtica): #stvaranje ptica
            #noviW i noviH
            noviWiH = zmaj_w/random.uniform(zmaj_w/2.5, zmaj_w/2)
            ProtivnikW.append(zmaj_w/noviWiH)
            ProtivnikH.append(zmaj_h/noviWiH)
            #noviX
            noviX = random.uniform(ProtivnikW[i], int(screen.get_width()*0.834895-ProtivnikW[i])) #stvaranje x pozicije protivnika koja može bit od početka do kraja screena
            if i == 0: #za prvog protivnika uzima se bilo koji x
                ProtivnikX.append(noviX)
            else: #za ostale protivnike se uzima bilo koji x, ali ako je x u blizini prijašnjeg neprijatelja, bira se novi x. Tako neće doći do preklapanja protivnika
                while abs(ProtivnikX[i-1]-noviX) < ProtivnikW[i]:
                    noviX = random.uniform(ProtivnikW[i], int(screen.get_width()*0.834895-ProtivnikW[i]))
                else:
                    ProtivnikX.append(noviX)
            #noviY
            if i == 0: #uzima se određeni y na kome će se stvoriti 1. neprijatelj
                ProtivnikY.append(-ProtivnikH[i])
            else: #ostali neprijatelji uzimaju prošli y i stvaraju se za istu visinu višu od prošloga
                ProtivnikY.append(ProtivnikY[i-1]-ProtivnikH[i]*brzinaStvaranja)
            #slika Protivnika
            slikaProtivnika = pygame.transform.scale(protivnik_og, (ProtivnikW[i], ProtivnikH[i]))
            if random.random() <= 0.5:
                ProtivnikSlika.append(pygame.transform.flip(slikaProtivnika,True,False))
            else:
                ProtivnikSlika.append(slikaProtivnika)
            #brzina Protivnika
            protivnikPomakY.append(random.uniform(screen.get_height() / 75,screen.get_height() / 55))

    def stvoriAvione():#stvaranje aviona
        for i in range(brojAviona):
            #noviW i noviH
            AvionW.append(random.uniform(zmaj_w*2, zmaj_w*1.7))
            AvionH.append(random.uniform(zmaj_h*0.6, zmaj_h*0.45))
            #noviY
            avionNoviY = random.uniform(screen.get_height()/4, screen.get_height()*0.8) #stvaranje x pozicije protivnika koja može bit od početka do kraja screena
            if i == 0: #za prvog protivnika uzima se bilo koji x
                AvionY.append(avionNoviY)
            else: #za ostale protivnike se uzima bilo koji x, ali ako je x u blizini prijašnjeg neprijatelja, bira se novi x. Tako neće doći do preklapanja protivnika
                while abs(AvionY[i-1]-avionNoviY) < AvionH[i]:
                    avionNoviY = random.uniform(screen.get_height()/4, screen.get_height()*0.8)
                else:
                    AvionY.append(avionNoviY)
            #noviX
            if i == 0: #uzima se određeni y na kome će se stvoriti 1. neprijatelj
                AvionX.append(-AvionW[i])
            else: #ostali neprijatelji uzimaju prošli y i stvaraju se za istu visinu višu od prošloga
                AvionX.append(AvionX[i-1]-AvionW[i]*brzinaStvaranja*2)
            #slika Protivnika 
            AvionSlika.append(pygame.transform.scale(avion_og, (AvionW[i], AvionH[i])))
            #brzina Protivnika
            AvionPomakX.append(random.uniform(screen.get_width() / 120,screen.get_width() / 80))

    def stvoriMeteore():
        for i in range(brojMeteora): #stvaranje meteora
            #noviW i noviH
            meteoriNoviWiH = zmaj_w/random.uniform(zmaj_w/2.5, zmaj_w/2)
            MeteorW.append(zmaj_w/meteoriNoviWiH)
            MeteorH.append(zmaj_h/meteoriNoviWiH)
            #noviX
            meteoriNoviX = random.uniform(0, screen.get_width()*0.834895-MeteorW[i]) #stvaranje x pozicije protivnika koja može bit od početka do kraja screena
            if i == 0: #za prvog protivnika uzima se bilo koji x
                MeteorX.append(meteoriNoviX)
            else: #za ostale protivnike se uzima bilo koji x, ali ako je x u blizini prijašnjeg neprijatelja, bira se novi x. Tako neće doći do preklapanja protivnika
                while abs(MeteorX[i-1]-meteoriNoviX) < MeteorW[i]:
                    meteoriNoviX = random.uniform(0, screen.get_width()*0.834895-MeteorW[i])
                else:
                    MeteorX.append(meteoriNoviX)
            #noviY
            if i == 0: #uzima se određeni y na kome će se stvoriti 1. neprijatelj
                MeteorY.append(-MeteorH[i])
            else: #ostali neprijatelji uzimaju prošli y i stvaraju se za istu visinu višu od prošloga
                MeteorY.append(MeteorY[i-1]-MeteorH[i]*brzinaStvaranja*2)
            #slika Protivnika
            MeteorSlika.append(pygame.transform.scale(meteor_og, (MeteorW[i], MeteorH[i])))
            #brzina Protivnika
            MeteorPomakX.append(random.uniform(screen.get_width() / 110,screen.get_width() / 80))
            MeteorPomakY.append(random.uniform(screen.get_height() / 70,screen.get_height() / 50))

    def stvoriVjetar():
        for i in range(brojVjetra):
            #noviW i noviH
            VjetarW.append(random.uniform(zmaj_w*1.5, zmaj_w*1))
            VjetarH.append(random.uniform(zmaj_h*0.8, zmaj_h*0.6))
            #noviY
            vjetarNoviY = random.uniform(screen.get_height()/2.5, screen.get_height()*0.8) #stvaranje x pozicije protivnika koja može bit od početka do kraja screena
            if i == 0: #za prvog protivnika uzima se bilo koji x
                VjetarY.append(vjetarNoviY)
            else: #za ostale protivnike se uzima bilo koji x, ali ako je x u blizini prijašnjeg neprijatelja, bira se novi x. Tako neće doći do preklapanja protivnika
                while abs(VjetarY[i-1]-vjetarNoviY) < VjetarH[i]:
                    vjetarNoviY = random.uniform(0, screen.get_height()/2)
                else:
                    VjetarY.append(vjetarNoviY)
            #noviX
            if i == 0: #uzima se određeni y na kome će se stvoriti 1. neprijatelj
                VjetarX.append(screen.get_width()+VjetarW[i]*brzinaStvaranja)
            else: #ostali neprijatelji uzimaju prošli y i stvaraju se za istu visinu višu od prošloga
                VjetarX.append(VjetarX[i-1]+VjetarW[i])
            #slika Protivnika
            VjetarSlika.append(pygame.transform.scale(vjetar_og, (VjetarW[i], VjetarH[i])))
            #brzina Protivnika
            VjetarPomakX.append(random.uniform(screen.get_width() / 120,screen.get_width() / 80))
        
    def stvoriVanzemaljca():
        for i in range(brojVanzemaljca): #stvaranje meteora
            #noviW i noviH
            VanzemaljacW.append(random.uniform(zmaj_w*1.1, zmaj_w*0.9))
            VanzemaljacH.append(random.uniform(zmaj_h*0.7, zmaj_h*0.6))
            #noviX
            vanzemaljacNoviX = random.uniform(0, screen.get_width()*0.834895-VanzemaljacW[i]) #stvaranje x pozicije protivnika koja može bit od početka do kraja screena
            if i == 0: #za prvog protivnika uzima se bilo koji x
                VanzemaljacX.append(vanzemaljacNoviX)
            else: #za ostale protivnike se uzima bilo koji x, ali ako je x u blizini prijašnjeg neprijatelja, bira se novi x. Tako neće doći do preklapanja protivnika
                while abs(VanzemaljacX[i-1]-vanzemaljacNoviX) < VanzemaljacW[i]:
                    vanzemaljacNoviX = random.uniform(0, screen.get_width()*0.834895-VanzemaljacW[i])
                else:
                    VanzemaljacX.append(vanzemaljacNoviX)
            #noviY
            if i == 0: #uzima se određeni y na kome će se stvoriti 1. neprijatelj
                VanzemaljacY.append(-VanzemaljacH[i])
            else: #ostali neprijatelji uzimaju prošli y i stvaraju se za istu visinu višu od prošloga
                VanzemaljacY.append(VanzemaljacY[i-1]-VanzemaljacH[i]*brzinaStvaranja*2)
            #slika Protivnika
            VanzemaljacSlika.append(pygame.transform.scale(vanzemaljac_og, (VanzemaljacW[i], VanzemaljacH[i])))
            #brzina Protivnika
            VanzemaljacPomakX.append(random.uniform(screen.get_width() / 200,screen.get_width() / 180))
            VanzemaljacPomakY.append(random.uniform(screen.get_height() / 150,screen.get_height() / 130))
        
            VanzemaljacPucanjX.append(VanzemaljacX[i]+VanzemaljacW[i]/2)
            VanzemaljacPucanjY.append(VanzemaljacY[i]+VanzemaljacH[i]/2)
            VanzemaljacPucanjPomakY.append(random.uniform(screen.get_height() / 100,screen.get_height() / 80))
            vanzemaljac_pucanje.append(False)
                
    def vratiProtivnika(i):
        ProtivnikY[i] = min(ProtivnikY) - ProtivnikH[i]*brzinaStvaranja #vraća protivnika natrag gore (isti kod kao i kod spawnanja)
        noviX = random.randint(0, int(screen.get_width()*0.834895-ProtivnikW[i]))
        while abs(ProtivnikX[i-1]-noviX) < ProtivnikW[i]:
            noviX = random.randint(0, int(screen.get_width()*0.834895-ProtivnikW[i]))
        else:
            ProtivnikX[i] = noviX

    def vratiAvion(i):
        if min(AvionX) >= 0:
            AvionX[i] = 0 - AvionW[i]*brzinaStvaranja #vraća protivnika natrag gore (isti kod kao i kod spawnanja)
            avionNoviY = random.uniform(screen.get_height()/4, screen.get_height()*0.8)
            while abs(AvionY[i-1]-avionNoviY) < AvionH[i]:
                avionNoviY = random.uniform(screen.get_height()/4, screen.get_height()*0.8)
            else:
                AvionY[i] = avionNoviY
        else:
            AvionX[i] = screen.get_width()

    def vratiMeteor(i):
        if min(MeteorY) >= 0: #vraćanje ptica
            MeteorY[i] = 0 - MeteorH[i]*brzinaStvaranja #vraća protivnika natrag gore (isti kod kao i kod spawnanja)
            meteoriNoviX = random.uniform(0, screen.get_width()*0.834895- MeteorW[i])
            while abs(ProtivnikX[i-1]-meteoriNoviX) < MeteorW[i]:
                meteoriNoviX = random.uniform(0, screen.get_width()*0.834895- MeteorW[i])
            else:
                MeteorX[i] = meteoriNoviX
        else:
            MeteorY[i] = screen.get_height()

    def vratiVjetar(i):
        if min(VjetarX) < screen.get_width()*0.834895:
            VjetarX[i] = screen.get_width() + VjetarW[i] #vraća protivnika natrag gore (isti kod kao i kod spawnanja)
            vjetarNoviY = random.uniform(screen.get_height()/2.5, screen.get_height()*0.8)
            while abs(VjetarY[i-1]-vjetarNoviY) < VjetarH[i]:
                vjetarNoviY = random.uniform(screen.get_height()/2.5, screen.get_height()-VjetarH[i])
            else:
                VjetarY[i] = vjetarNoviY
        else:
            VjetarX[i] = 0

    def vratiVanzemaljca(i):
        VanzemaljacY[i] = 0 - VanzemaljacH[i]*brzinaStvaranja #vraća protivnika natrag gore (isti kod kao i kod spawnanja)
        VanzemaljacPomakY[i]= random.uniform(screen.get_height() / 150,screen.get_height() / 130)
        vanzemaljacNoviX = random.uniform(0, screen.get_width()*0.834895- VanzemaljacW[i])
        while abs(ProtivnikX[i-1]-vanzemaljacNoviX) < VanzemaljacW[i]:
            vanzemaljacNoviX = random.uniform(0, screen.get_width()*0.834895- VanzemaljacW[i])
        else:
            VanzemaljacX[i] = vanzemaljacNoviX

    #stvaranje neprijatelja
    stvoriProtivnike() 
    if avioni_state == True:
        stvoriAvione()
    if meteori_state == True:
        stvoriMeteore()
    if vjetar_state == True:
        stvoriVjetar()
    if vanzemaljac_state == True:
        stvoriVanzemaljca()


    run = True
    while run:
        clock = pygame.time.Clock()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spremi_igru()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    pause_menu()
                if event.key == pygame.K_SPACE: #pucanje powerupa
                    if ispaljeno1 == False and (vrijeme -timer_cooldown1) > cooldown1 and power_birac == 0:
                        timer_cooldown1 = vrijeme
                        power1_y = zmaj_y-zmaj_h/5 #u trenutku pucanja stavlja pucanj kod zmaja
                        power1_x = zmaj_x+(zmaj_w/2.1)
                        ispaljeno1 = True
                    if ispaljeno2 == False and (vrijeme -timer_cooldown2) > cooldown2 and power_birac == 1:
                        timer_cooldown2 = vrijeme
                        power2_y = zmaj_y-zmaj_h/3.5 #u trenutku pucanja stavlja pucanj kod zmaja
                        power2_x = zmaj_x+(zmaj_w/3)
                        ispaljeno2 = True
                    if ispaljeno3 == False and (vrijeme -timer_cooldown3) > cooldown3 and power_birac == 2:
                        timer_cooldown3 = vrijeme
                        ispaljeno3 = True
                    if ispaljeno4 == False and (vrijeme -timer_cooldown4) > cooldown4 and power_birac == 3:
                        for i in range(3):
                            power4_y[i] = zmaj_y-zmaj_h/5 #u trenutku pucanja stavlja pucanj kod zmaja
                            power4_x[i] = zmaj_x+(zmaj_w/2.1)
                            timer_cooldown4 = vrijeme
                            ispaljeno4 = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if powerups != 0:
                        if power_birac == powerups-1:
                            power_birac = 0
                        else:
                            power_birac +=1
                if event.button == 3:
                    if powerups != 0:
                        if power_birac < 1:
                            power_birac = powerups-1
                        else:
                            power_birac -= 1
                if event.button == 5:
                    if powerups != 0:
                        if power_birac == powerups-1:
                            power_birac = 0
                        else:
                            power_birac +=1
                if event.button == 4:
                    if powerups != 0:
                        if power_birac < 1:
                            power_birac = powerups-1
                        else:
                            power_birac -= 1

        screen.blit(pozadina, (0,0))

        progress = vrijeme/final_vrijeme

        #pomak pucnja
        if ispaljeno1 == True:
            power1_y += pucanjPomak
            screen.blit(pygame.transform.scale(fireball_og,(power1_w,power1_h)), (power1_x, power1_y))
        else: #kada ne puca, stavlja pucanj off screen
            power1_y = screen.get_height() + power1_h*2
            power1_x = -power1_w*2

        #ograničenje pucnja
        if power1_y < 0:
            ispaljeno1 = False

        #pomak pucnja
        if ispaljeno2 == True:
            power2_y += pucanjPomak
            screen.blit(pygame.transform.scale(powerup2_og,(power2_w,power2_h)), (power2_x, power2_y))
        else: #kada ne puca, stavlja pucanj off screen
            power2_y = screen.get_height() + power2_h*2
            power2_x = -power2_w*2

        #ograničenje pucnja
        if power2_y < 0:
            ispaljeno2 = False 

        #pomak pucnja
        if ispaljeno3 == True:
            if vrijeme - timer_cooldown3 < 6:
                isHit = True
                timer1 = 0 
                power3_y = zmaj_y-zmaj_h/4 #u trenutku pucanja stavlja pucanj kod zmaja
                power3_x = zmaj_x-zmaj_w/8
                screen.blit(pygame.transform.scale(powerup3_og,(power3_w,power3_h)), (power3_x, power3_y))
            else:
                ispaljeno3 = False
                isHit = False
        else: #kada ne puca, stavlja pucanj off screen
            power3_y = screen.get_height() + power2_h*2
            power3_x = -power2_w*2
        
        #pomak pucnja
        if ispaljeno4 == True:
            for i in range(3):
                if i == 0:
                    pucanjPomakY = -1*(screen.get_height() / 60)
                    pucanjPomakX = -1*(screen.get_width() / 200)
                if i == 1:
                    pucanjPomakY = -1*(screen.get_height() / 60)
                    pucanjPomakX = 0
                if i == 2:
                    pucanjPomakY = -1*(screen.get_height() / 60)
                    pucanjPomakX = screen.get_width() / 200
                power4_y[i] += pucanjPomakY
                power4_x[i] += pucanjPomakX
                screen.blit(pygame.transform.scale(powerup2_og,(power4_w,power4_h)), (power4_x[i], power4_y[i]))

                #ograničenje pucnja
                if max(power4_y) < 0:
                    ispaljeno4 = False

        else:
            for i in range(3):
                power4_y[i] = 0
                power4_x[i] = 0
            
        #pomak zmaja
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
        if zmaj_x + zmaj_w> screen.get_width()*0.834895:
            zmaj_x = screen.get_width()*0.834895 - zmaj_w
        if zmaj_y < 0:
            zmaj_y = 0
        if zmaj_y + zmaj_h> screen.get_height():
            zmaj_y = screen.get_height() - zmaj_h

        for i in range(brojPtica): 
            ProtivnikY[i] += protivnikPomakY[i] #micanje protivnika
            screen.blit(ProtivnikSlika[i], (ProtivnikX[i],ProtivnikY[i])) #crtanje protivnika

            if ProtivnikY[i] > screen.get_height(): #respawnanje protivnika
                vratiProtivnika(i)
                
            if pygame.Rect(ProtivnikX[i]+ProtivnikW[i]*0.05, ProtivnikY[i]+ProtivnikH[i]*0.05, ProtivnikW[i]*0.9, ProtivnikH[i]*0.9).colliderect(pygame.Rect(zmaj_x+zmaj_w*0.1,zmaj_y+zmaj_h*0.1,zmaj_w*0.8,zmaj_h*0.8)) and isHit == False: #collision protivnika
                život -= 1
                isHit = True
                timer1 = vrijeme
            
            if pygame.Rect(ProtivnikX[i], ProtivnikY[i], ProtivnikW[i], ProtivnikH[i]).colliderect(pygame.Rect(power1_x, power1_y, power1_w, power1_h)): #collision pucnja i protivnika
                ispaljeno1 = False
                uništeniProtivnici += 1
                vratiProtivnika(i)
            
            if ispaljeno2 == True:
                if pygame.Rect(ProtivnikX[i], ProtivnikY[i], ProtivnikW[i], ProtivnikH[i]).colliderect(pygame.Rect(power2_x, power2_y, power2_w, power2_h)): #collision pucnja i protivnika
                    uništeniProtivnici += 1
                    vratiProtivnika(i)
            
            if ispaljeno3 == True:
                if pygame.Rect(ProtivnikX[i], ProtivnikY[i], ProtivnikW[i], ProtivnikH[i]).colliderect(pygame.Rect(power3_x, power3_y, power3_w, power3_h)): #collision pucnja i protivnika
                    uništeniProtivnici += 1
                    vratiProtivnika(i)
            
            if ispaljeno4 == True:
                for l in range(3):
                    if pygame.Rect(ProtivnikX[i], ProtivnikY[i], ProtivnikW[i], ProtivnikH[i]).colliderect(pygame.Rect(power4_x[l], power4_y[l], power4_w, power4_h)): #collision pucnja i protivnika
                        uništeniProtivnici += 1
                        vratiProtivnika(i)

        if avioni_state == True:
            for i in range(brojAviona): 
                AvionX[i] += AvionPomakX[i] #micanje protivnika
                screen.blit(AvionSlika[i], (AvionX[i],AvionY[i])) #crtanje protivnika

                if AvionX[i] > screen.get_width()*0.834895:
                    vratiAvion(i)
                    
                if pygame.Rect(AvionX[i]+AvionW[i]*0.1, AvionY[i]+AvionH[i]*0.1, AvionW[i]*0.8, AvionH[i]*0.8).colliderect(pygame.Rect(zmaj_x+zmaj_w*0.15,zmaj_y+zmaj_h*0.15,zmaj_w*0.7,zmaj_h*0.7)) and isHit == False: #collision protivnika
                    život -= 1
                    isHit = True
                    timer1 = vrijeme
                
                if pygame.Rect(AvionX[i], AvionY[i], AvionW[i], AvionH[i]).colliderect(pygame.Rect(power1_x, power1_y, power1_w, power1_h)): #collision pucnja i protivnika
                    ispaljeno1 = False
                    uništeniProtivnici += 1
                    vratiAvion(i)
                
                if ispaljeno2 == True:
                    if pygame.Rect(AvionX[i], AvionY[i], AvionW[i], AvionH[i]).colliderect(pygame.Rect(power2_x, power2_y, power2_w, power2_h)): #collision pucnja i protivnika
                        uništeniProtivnici += 1
                        vratiAvion(i)
                
                if ispaljeno3 == True:
                    if pygame.Rect(AvionX[i], AvionY[i], AvionW[i], AvionH[i]).colliderect(pygame.Rect(power3_x, power3_y, power3_w, power3_h)): #collision pucnja i protivnika
                        uništeniProtivnici += 1
                        vratiAvion(i)

                if ispaljeno4 == True:
                    for l in range(3):
                        if pygame.Rect(AvionX[i], AvionY[i], AvionW[i], AvionH[i]).colliderect(pygame.Rect(power4_x[l], power4_y[l], power4_w, power4_h)): #collision pucnja i protivnika
                            uništeniProtivnici += 1
                            vratiAvion(i)

        if meteori_state == True:
            for i in range(brojMeteora): 
                MeteorY[i] += MeteorPomakY[i] #micanje protivnika
                MeteorX[i] += MeteorPomakX[i]
                screen.blit(MeteorSlika[i], (MeteorX[i],MeteorY[i])) #crtanje protivnika

                if MeteorY[i] > screen.get_height(): #respawnanje protivnika
                    vratiMeteor(i)
                
                if MeteorX[i] > screen.get_width()*0.834895-MeteorW[i] or MeteorX[i] <= 0: #ako meteor dira granice, odbija se u drugu stranu
                    MeteorPomakX[i] = -1*MeteorPomakX[i]

                if pygame.Rect(MeteorX[i]+MeteorW[i]*0.1, MeteorY[i]+MeteorH[i]*0.1, MeteorW[i]*0.8, MeteorH[i]*0.8).colliderect(pygame.Rect(zmaj_x+zmaj_w*0.15,zmaj_y+zmaj_h*0.15,zmaj_w*0.7,zmaj_h*0.7)) and isHit == False: #collision protivnika
                    život -= 1
                    isHit = True
                    timer1 = vrijeme
                
                if ispaljeno1 == True:
                    if pygame.Rect(MeteorX[i], MeteorY[i], MeteorW[i], MeteorH[i]).colliderect(pygame.Rect(power1_x, power1_y, power1_w, power1_h)): #collision pucnja i protivnika
                        ispaljeno1 = False

                if ispaljeno2 == True:
                    if pygame.Rect(MeteorX[i], MeteorY[i], MeteorW[i], MeteorH[i]).colliderect(pygame.Rect(power2_x, power2_y, power2_w, power2_h)): #collision pucnja i protivnika
                        ispaljeno2 = False
                        uništeniProtivnici += 1
                        vratiMeteor(i)

                if ispaljeno3 == True:
                    if pygame.Rect(MeteorX[i], MeteorY[i], MeteorW[i], MeteorH[i]).colliderect(pygame.Rect(power3_x, power3_y, power3_w, power3_h)): #collision pucnja i protivnika
                        uništeniProtivnici += 1
                        vratiMeteor(i)
                
                if ispaljeno4 == True:
                    for l in range(3):
                        if pygame.Rect(MeteorX[i], MeteorY[i], MeteorW[i], MeteorH[i]).colliderect(pygame.Rect(power4_x[l], power4_y[l], power4_w, power4_h)): #collision pucnja i protivnika
                            uništeniProtivnici += 1
                            vratiMeteor(i)

        if vjetar_state == True:
            for i in range(brojVjetra): 
                VjetarX[i] -= VjetarPomakX[i] #micanje protivnika
                screen.blit(VjetarSlika[i], (VjetarX[i],VjetarY[i])) #crtanje protivnika

                if VjetarX[i] < -VjetarW[i]:
                    vratiVjetar(i)
                    
                if pygame.Rect(VjetarX[i], VjetarY[i], VjetarW[i], VjetarH[i]).colliderect(pygame.Rect(zmaj_x,zmaj_y,zmaj_w,zmaj_h)): #collision protivnika
                    zmaj_x -= VjetarPomakX[i]
                
                if ispaljeno3 == True:
                    if pygame.Rect(VjetarX[i], VjetarY[i], VjetarW[i], VjetarH[i]).colliderect(pygame.Rect(power3_x,power3_y,power3_w,power3_h)): #collision protivnika
                        uništeniProtivnici += 1
                        vratiVjetar(i)
                
        if vanzemaljac_state == True:
            for i in range(brojVanzemaljca): 
                VanzemaljacY[i] += VanzemaljacPomakY[i] #micanje protivnika
                screen.blit(VanzemaljacSlika[i], (VanzemaljacX[i],VanzemaljacY[i])) #crtanje protivnika

                if VanzemaljacY[i] >= screen.get_height()/5: #respawnanje protivnika
                    VanzemaljacPomakY[i] = 0
                    vanzemaljac_pucanje[i] = True
                    VanzemaljacX[i] += VanzemaljacPomakX[i]

                if VanzemaljacX[i] > screen.get_width()*0.834895-VanzemaljacW[i] or VanzemaljacX[i] <= 0: #ako meteor dira granice, odbija se u drugu stranu
                    VanzemaljacPomakX[i] = -1*VanzemaljacPomakX[i]

                if pygame.Rect(VanzemaljacX[i]+VanzemaljacW[i]*0.1, VanzemaljacY[i]+VanzemaljacH[i]*0.1, VanzemaljacW[i]*0.8, VanzemaljacH[i]*0.8).colliderect(pygame.Rect(zmaj_x+zmaj_w*0.15,zmaj_y+zmaj_h*0.15,zmaj_w*0.7,zmaj_h*0.7)) and isHit == False: #collision protivnika
                    život -= 1
                    isHit = True
                    timer1 = vrijeme
                
                if ispaljeno1 == True:
                    if pygame.Rect(VanzemaljacX[i], VanzemaljacY[i], VanzemaljacW[i], VanzemaljacH[i]).colliderect(pygame.Rect(power1_x, power1_y, power1_w, power1_h)): #collision pucnja i protivnika
                        ispaljeno1 = False
                        vanzemaljac_pucanje[i] = False
                        uništeniProtivnici += 1
                        vratiVanzemaljca(i)
                
                if ispaljeno2 == True:
                    if pygame.Rect(VanzemaljacX[i], VanzemaljacY[i], VanzemaljacW[i], VanzemaljacH[i]).colliderect(pygame.Rect(power2_x, power2_y, power2_w, power2_h)): #collision pucnja i protivnika
                        vanzemaljac_pucanje[i] = False
                        uništeniProtivnici += 1
                        vratiVanzemaljca(i)
                
                if ispaljeno3 == True:
                    if pygame.Rect(VanzemaljacX[i], VanzemaljacY[i], VanzemaljacW[i], VanzemaljacH[i]).colliderect(pygame.Rect(power3_x, power3_y, power3_w, power3_h)): #collision pucnja i protivnika
                        vanzemaljac_pucanje[i] = False
                        uništeniProtivnici += 1
                        vratiVanzemaljca(i)
                
                if ispaljeno4 == True:
                    for l in range(3):
                        if pygame.Rect(VanzemaljacX[i], VanzemaljacY[i], VanzemaljacW[i], VanzemaljacH[i]).colliderect(pygame.Rect(power4_x[l], power4_y[l], power4_w, power4_h)): #collision pucnja i protivnika
                            vanzemaljac_pucanje[i] = False
                            uništeniProtivnici += 1
                            vratiVanzemaljca(i)

                if vanzemaljac_pucanje[i] == True:
                    VanzemaljacPucanjY[i] += VanzemaljacPucanjPomakY[i]
                    screen.blit(pygame.transform.scale(vanzemaljac_pucanj_og, (power1_w, power1_h*1.5)), (VanzemaljacPucanjX[i], VanzemaljacPucanjY[i])) #crtanje pucnja
                else:
                    VanzemaljacPucanjX[i] = VanzemaljacX[i] + VanzemaljacW[i]/2
                    VanzemaljacPucanjY[i] = VanzemaljacY[i] + VanzemaljacH[i]/2
                    #ograničenje pucnja
                if VanzemaljacPucanjY[i] > screen.get_height():
                    VanzemaljacPucanjX[i] = VanzemaljacX[i] +VanzemaljacW[i]/2
                    VanzemaljacPucanjY[i] = VanzemaljacY[i] + VanzemaljacH[i]/2
                
                if pygame.Rect(VanzemaljacPucanjX[i], VanzemaljacPucanjY[i], power1_w, power1_h*1.5).colliderect(pygame.Rect(zmaj_x+zmaj_w*0.15,zmaj_y+zmaj_h*0.15,zmaj_w*0.7,zmaj_h*0.7)) and isHit == False: #collision protivnika
                    život -= 1
                    isHit = True
                    timer1 = vrijeme
                    VanzemaljacPucanjX[i] = VanzemaljacX[i] +VanzemaljacW[i]/2
                    VanzemaljacPucanjY[i] = VanzemaljacY[i] + VanzemaljacH[i]/2
                
                if ispaljeno1 == True:
                    if pygame.Rect(VanzemaljacPucanjX[i], VanzemaljacPucanjY[i], power1_w, power1_h*1.5).colliderect(pygame.Rect(power1_x, power1_y, power1_w, power1_h)): #collision protivnika
                        VanzemaljacPucanjX[i] = VanzemaljacX[i] +VanzemaljacW[i]/2
                        VanzemaljacPucanjY[i] = VanzemaljacY[i] + VanzemaljacH[i]/2
                        ispaljeno1 = False
                
                if ispaljeno2 == True:
                    if pygame.Rect(VanzemaljacPucanjX[i], VanzemaljacPucanjY[i], power1_w, power1_h*1.5).colliderect(pygame.Rect(power2_x, power2_y, power2_w, power2_h)): #collision protivnika
                        VanzemaljacPucanjX[i] = VanzemaljacX[i] +VanzemaljacW[i]/2
                        VanzemaljacPucanjY[i] = VanzemaljacY[i] + VanzemaljacH[i]/2
                
                if ispaljeno3 == True:
                    if pygame.Rect(VanzemaljacPucanjX[i], VanzemaljacPucanjY[i], power1_w, power1_h*1.5).colliderect(pygame.Rect(power3_x, power3_y, power3_w, power3_h)): #collision protivnika
                        VanzemaljacPucanjX[i] = VanzemaljacX[i] +VanzemaljacW[i]/2
                        VanzemaljacPucanjY[i] = VanzemaljacY[i] + VanzemaljacH[i]/2

                if ispaljeno4 == True:
                    for l in range(3):
                        if pygame.Rect(VanzemaljacPucanjX[i], VanzemaljacPucanjY[i], power1_w, power1_h*1.5).colliderect(pygame.Rect(power4_x[l], power4_y[l], power4_w, power4_h)): #collision pucnja i protivnika
                            VanzemaljacPucanjX[i] = VanzemaljacX[i] +VanzemaljacW[i]/2
                            VanzemaljacPucanjY[i] = VanzemaljacY[i] + VanzemaljacH[i]/2

        if isHit == True: #ako pogođen
            if vrijeme - timer1 > 1:
                isHit = False
                zmaj_slika.set_alpha(256) #vraća transparency
            elif vrijeme - timer1 <=1 and vrijeme-timer1 >0:
                zmaj_slika.set_alpha(120) #stvara sliku transparentnu
                draw_text(f"{round(vrijeme - timer1,2)}s",text_font,(0,0,0),screen.get_width()/2,screen.get_height()/2)

        #crtanje zmaja
        screen.blit(zmaj_slika, (zmaj_x, zmaj_y))
        #vrijeme
        t2 = time.perf_counter()
        vrijeme =round((t2-t1)-tp,1)

        #sidebar
        if power_birac == -1:
            screen.blit(sidebar,(screen.get_width()*0.834895, 0))
        if power_birac == 0:
            screen.blit(sidebar1,(screen.get_width()*0.834895, 0))
            if ispaljeno1 == False and (vrijeme -timer_cooldown1) > cooldown1:
                fireball_nepucan = pygame.transform.scale(fireball_og,(power1_w,power1_h))
                fireball_nepucan.set_alpha(150)
                screen.blit(fireball_nepucan, (zmaj_x+(zmaj_w/2.1), zmaj_y-zmaj_h/5))
        if power_birac == 1:
            screen.blit(sidebar2,(screen.get_width()*0.834895, 0))
            if ispaljeno2 == False and (vrijeme -timer_cooldown2) > cooldown2:
                plavi_nepucan = pygame.transform.scale(powerup2_og,(power2_w,power2_h))
                plavi_nepucan.set_alpha(150)
                screen.blit(plavi_nepucan, (zmaj_x+(zmaj_w/3), zmaj_y-zmaj_h/3.5))
        if power_birac == 2:
            screen.blit(sidebar3,(screen.get_width()*0.834895, 0))
            if ispaljeno3 == False and (vrijeme -timer_cooldown3) > cooldown3:
                plavi_nepucan = pygame.transform.scale(powerup3_og,(power3_w,power3_h))
                plavi_nepucan.set_alpha(150)
                screen.blit(plavi_nepucan, (zmaj_x-zmaj_w/8, zmaj_y-zmaj_h/4))
        if power_birac == 3:
            screen.blit(sidebar4,(screen.get_width()*0.834895, 0))
            if ispaljeno4 == False and (vrijeme -timer_cooldown4) > cooldown4:
                plavi_nepucan = pygame.transform.scale(powerup2_og,(power4_w,power4_h))
                plavi_nepucan.set_alpha(150)
                screen.blit(plavi_nepucan, (zmaj_x+(zmaj_w/3), zmaj_y-zmaj_h/3.5))
                screen.blit(plavi_nepucan, (zmaj_x+(zmaj_w/8), zmaj_y-zmaj_h/3.5))
                screen.blit(plavi_nepucan, (zmaj_x+(zmaj_w/2), zmaj_y-zmaj_h/3.5))

        #pisanje teksta u sidebar
        draw_text(f"{odabrani_level}",text_font,(0,0,0),screen.get_width()*0.865,screen.get_height()*0.92)
        draw_text(f"{ime}",text_font,(0,0,0),screen.get_width()*0.862,screen.get_height()*0.05)
        for i in range(život+1):
            x = screen.get_width()*0.05
            screen.blit(srce,(screen.get_width()*0.84375+x*i,screen.get_height()*0.145))

        #slike powerupova u sidebaru
        if int(level_state[-3]) > 1:
            if vrijeme - timer_cooldown1 < cooldown1: #crtanje powerupa u sidebaru
                draw_text(f"{round((vrijeme - timer_cooldown1),1)}s",text_font,(0,0,0),screen.get_width()*0.85,screen.get_height()*0.28)
                fireball_menu.set_alpha(150)
                screen.blit(fireball_menu,(screen.get_width()*0.847,screen.get_height()*0.27))
            else:
                fireball_menu.set_alpha(256)
                screen.blit(fireball_menu,(screen.get_width()*0.847,screen.get_height()*0.27))
        else:
            screen.blit(nema_sign,(screen.get_width()*0.842,screen.get_height()*0.27))
        
        if int(level_state[-3]) > 2:
            if vrijeme - timer_cooldown2 < cooldown2: #crtanje powerupa u sidebaru
                draw_text(f"{round((vrijeme - timer_cooldown2),1)}s",text_font,(0,0,0),screen.get_width()*0.85,screen.get_height()*0.45)
                powerup2_menu.set_alpha(150)
                screen.blit(powerup2_menu,(screen.get_width()*0.847,screen.get_height()*0.45))
            else:
                powerup2_menu.set_alpha(256)
                screen.blit(powerup2_menu,(screen.get_width()*0.847,screen.get_height()*0.45))
        else:
            screen.blit(nema_sign,(screen.get_width()*0.842,screen.get_height()*0.45))
        
        if int(level_state[-3]) > 3:
            if vrijeme - timer_cooldown3 < cooldown3: #crtanje powerupa u sidebaru
                draw_text(f"{round((vrijeme - timer_cooldown3),1)}s",text_font,(0,0,0),screen.get_width()*0.85,screen.get_height()*0.62)
                powerup3_menu.set_alpha(150)
                screen.blit(powerup3_menu,(screen.get_width()*0.848,screen.get_height()*0.62))
            else:
                powerup3_menu.set_alpha(256)
                screen.blit(powerup3_menu,(screen.get_width()*0.848,screen.get_height()*0.62))
        else:
            screen.blit(nema_sign,(screen.get_width()*0.842,screen.get_height()*0.62))

        if int(level_state[-3]) > 4:
            if vrijeme - timer_cooldown4 < cooldown4: #crtanje powerupa u sidebaru
                draw_text(f"{round((vrijeme - timer_cooldown4),1)}s",text_font,(0,0,0),screen.get_width()*0.85,screen.get_height()*0.79)
                powerup4_menu.set_alpha(150)
                screen.blit(powerup4_menu,(screen.get_width()*0.843,screen.get_height()*0.79))
            else:
                powerup4_menu.set_alpha(256)
                screen.blit(powerup4_menu,(screen.get_width()*0.843,screen.get_height()*0.79))
        else:
            screen.blit(nema_sign,(screen.get_width()*0.842,screen.get_height()*0.79))

        screen.blit(zmaj_menu, (screen.get_width()*0.93,screen.get_height()*0.816+(-1*screen.get_height()*0.52*progress)))
        
        if progress == 1: #runda je gotova
            if život == 2: #nisi pogođen
                postignuce[0] = "da"
            if uništeniProtivnici >= 100:
                postignuce[1] = "da"
            if level_state == "Level 5-2":
                postignuce[2] = "da"
            if impossible_state == True: #nemogući level
                postignuce[3] = "da"
                main_menu()
            if bozic_state == True:
                postignuce[4] = "da"
                main_menu()
            if postignuce[0] == "da" and postignuce[1] == "da" and postignuce[2] == "da" and postignuce[3] == "da" and postignuce[4] == "da":
                postignuce[5] = "da"
                
            if replay_state == False and impossible_state == False and bozic_state == False:
                if level_state == "Level 1-1": #mijenjanje levela
                    level_state = "Level 1-2"
                elif level_state == "Level 1-2":
                    level_state = "Level 2-1"
                elif level_state == "Level 2-1":
                    level_state = "Level 2-2"
                elif level_state == "Level 2-2":
                    level_state = "Level 3-1"
                elif level_state == "Level 3-1":
                    level_state = "Level 3-2"
                elif level_state == "Level 3-2":
                    level_state = "Level 4-1"
                elif level_state == "Level 4-1":
                    level_state = "Level 4-2"
                elif level_state == "Level 4-2":
                    level_state = "Level 5-1"
                elif level_state == "Level 5-1":
                    level_state = "Level 5-2"
                elif level_state == "Level 5-2":
                    run = False
                    main_menu()
            run = False
            level_menu()
        if život < 0: #pokrece game_over funkciju ako ostaneš bez života
            run = False
            game_over()
        
        pygame.display.update()

if __name__ == "__main__":
    main()
