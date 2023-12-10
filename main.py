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
    global screen, text_font, text_font2, run
    pygame.init()

    #font i tekst
    text_font = pygame.font.SysFont("Arial",50)
    text_font2 = pygame.font.SysFont("Arial",80)
    screen = None

    os.environ["SDL_VIDEO_CENTERED"]="1"
    info=pygame.display.Info()
    screen_width, screen_height=info.current_w,info.current_h
    screen = pygame.display.set_mode((screen_width-int(0.005*screen_width),screen_height-int(0.06*screen_height)), pygame.FULLSCREEN)
    pygame.display.set_caption("Zmajevi")

    run = False
    while not run:
        run = main_menu()

user1ime = ""
user2ime = ""
ime = ""
def user_birac():
    global screen, text_font, pozadina_slika, koji_user, ime
    pozadina_slika = pygame.image.load("slike/users_bg.png")
    pozadina = pygame.Surface((screen.get_width(), screen.get_height()))
    pozadina.fill("Black")
    pozadina.set_alpha(100)
    screen.blit(pozadina, (0,0))
    screen.blit(pygame.transform.scale(pozadina_slika, (screen.get_width()*0.9, screen.get_height()*0.9)), (screen.get_width()/2-screen.get_width()*0.45, screen.get_height()/2-screen.get_height()*0.45))
    draw_text("Birač računa",text_font,"black",screen.get_width()/2.35,screen.get_height()/6)
    koji_user = ""
    run = True
    while run == True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        USER1_BUTTON = Button(f"{user1ime}", 70, "White", (220, 120), "Light Grey", "White", (screen.get_width()/2, screen.get_height()/2))
        USER2_BUTTON = Button(f"{user2ime}", 70, "White", (220, 120), "Light Grey", "White", (screen.get_width()/2, screen.get_height()/1.5))

        for gumb in [USER1_BUTTON, USER2_BUTTON]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if USER1_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    if user1ime == "":
                        koji_user = "1"
                        player_name()
                    else:
                        ime = user1ime
                        main_menu()
                if USER2_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    if user2ime == "":
                        koji_user = "2"
                        player_name()
                    else:
                        ime = user2ime
                        main_menu()

        pygame.display.update()

def player_name():
    global screen, ime, user1ime, user2ime
    font = pygame.font.Font(None, 60)
    ime = ""
    text_box = pygame.Rect(screen.get_width()*0.45, screen.get_height()*0.5, screen.get_width()*0.1, screen.get_height()*0.05)
    pozadina = pygame.Surface((screen.get_width(), screen.get_height()))
    pozadina.fill("Black")
    pozadina.set_alpha(100)
    screen.blit(pozadina, (0,0))
    screen.blit(pygame.transform.scale(pozadina_slika, (screen.get_width()*0.7, screen.get_height()*0.7)), (screen.get_width()/2-screen.get_width()*0.35, screen.get_height()/2-screen.get_height()*0.35))
    draw_text("Unesi ime:",font,"black",screen.get_width()/2.35,screen.get_height()/2.5)
    run = True
    while run == True:
        pygame.draw.rect(screen,"black", text_box, 4)
        surf1 = font.render(ime,True,'white')
        screen.blit(surf1, (text_box.x +5 , text_box.y +5))
        text_box.w = max(100, surf1.get_width()+10)
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        POTVRDA_BUTTON = Button(f"Potvrdi", 50, "Black", (220, 120), "Light Grey", "White", (screen.get_width()/2, screen.get_height()/1.5))
        for gumb in [POTVRDA_BUTTON]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if POTVRDA_BUTTON.checkForCollision(MENU_MOUSE_POS) and len(ime) > 1:
                    with open("igraci", "a") as datoteka:
                        datoteka.write(koji_user + "/" + ime + "\n")
                    run = False
                    main_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    ime = ime[:-1]
                else:
                    ime += event.unicode

        if koji_user == "1":
            user1ime = ime
        elif koji_user == "2":
            user2ime = ime
        pygame.display.update()

def main_menu():
    global screen, text_font, text_font2, skinovi, skin_brojac
    zmajko_pozadina = pygame.transform.scale(pygame.image.load("slike/pozadina_mainmenu.png"), (screen.get_width(), screen.get_height()))
    skin1 = pygame.transform.scale(pygame.image.load("slike/zmaj.png"), (screen.get_width()*0.2265, screen.get_height()*0.365))
    skin2 = pygame.transform.scale(pygame.image.load("slike/zmaj2.jpg"), (screen.get_width()*0.2265, screen.get_height()*0.365))
    skin_brojac = 0
    skinovi = [skin1, skin2]
    arrow = pygame.transform.rotate(pygame.image.load("slike/arrow.png"),90)
    strijelica1 = Button_Slika(screen.get_width()/8.5,screen.get_height()*0.82,arrow, 0.3)
    strijelica2 = Button_Slika(screen.get_width()/6,screen.get_height()*0.82,pygame.transform.flip(arrow, True, False), 0.3)
    run = True
    while run == True:
        screen.blit(zmajko_pozadina, (0,0))    
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #gumbovi na desnoj strani
        IGRAJ_GUMB = Button("Kampanja", 70, "Black", (screen.get_width()/3.5, screen.get_height()/9), "lightsalmon", "darksalmon", (screen.get_width()*0.8, screen.get_height()/2.5))
        LEVEL_GUMB = Button("Nemoguć level", 70, "Black", (screen.get_width()/3.5, screen.get_height()/9), "lightsalmon", "darksalmon", (screen.get_width()*0.8, screen.get_height()/1.85))
        ACHIEVEMENTS_GUMB = Button("Postignuća", 70, "Black", (screen.get_width()/3.5, screen.get_height()/9), "lightsalmon", "darksalmon", (screen.get_width()*0.8, screen.get_height()/1.45))
        QUIT_BUTTON = Button("Izađi", 70, "Black", (screen.get_width()/3.5, screen.get_height()/9), "lightsalmon", "darksalmon", (screen.get_width()*0.8, screen.get_height()/1.175))
        USERS_BUTTON = Button("Promijeni igrača", 50, "Blue", (screen.get_width()/5.5, screen.get_height()/20), "lightsalmon", "darksalmon", (screen.get_width()*0.172, screen.get_height()/3.2))
        for gumb in [IGRAJ_GUMB, QUIT_BUTTON, LEVEL_GUMB, ACHIEVEMENTS_GUMB, USERS_BUTTON]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)
        
        #skinovi
        screen.blit(skinovi[skin_brojac], (screen.get_width()*0.055, screen.get_height()*0.47))
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
            draw_text(f"{ime}",text_font,(0,0,0),screen.get_width()/8,screen.get_height()/6)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if IGRAJ_GUMB.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    level_menu()
                if USERS_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    user_birac()
                if QUIT_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def pause_menu():
    global screen, text_font
    paused = True
    pozadina = pygame.Surface((screen.get_width(), screen.get_height()))
    pozadina.fill("Black")
    pozadina.set_alpha(100)
    screen.blit(pozadina, (0,0))
    while paused:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        pauzirano_logo = pygame.transform.scale(pygame.image.load("slike/pauzirano_logo.png"), (screen.get_width()/3, screen.get_height()/5))

        PLAY_BUTTON = Button("Nastavi", 70, "White", (220, 120), "Light Grey", "Green", (screen.get_width()/2, screen.get_height()/2))
        QUIT_BUTTON = Button("Izađi", 70, "White", (220, 120), "Light Grey", "Red", (screen.get_width()/2, screen.get_height()/1.5))

        screen.blit(pauzirano_logo, (screen.get_width()/3,screen.get_height()/10))

        for gumb in [PLAY_BUTTON, QUIT_BUTTON]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    paused = False
                if QUIT_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                if event.key == pygame.K_ESCAPE:
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
        PLAY_BUTTON = Button("Igraj ponovno", 70, "White", (360, 120), "Light Grey", "Green", (screen.get_width()/2, screen.get_height()/2))
        MAIN_BUTTON = Button("Glavni izbornik", 70, "White", (360, 120), "Light Grey", "dimgray", (screen.get_width()/2, screen.get_height()/1.5))
        QUIT_BUTTON = Button("Izađi", 70, "White", (360, 120), "Light Grey", "Red", (screen.get_width()/2, screen.get_height()/1.2))
        
        kraj_logo = pygame.transform.scale(pygame.image.load("slike/kraj_logo.png"), (screen.get_width()/3, screen.get_height()/5))
        screen.blit(kraj_logo, (screen.get_width()/3,screen.get_height()/10))

        for gumb in [PLAY_BUTTON,MAIN_BUTTON, QUIT_BUTTON]:
            if gumb.checkForCollision(MENU_MOUSE_POS):
                gumb.changeButtonColor()
            gumb.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    igra()
                if QUIT_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if MAIN_BUTTON.checkForCollision(MENU_MOUSE_POS):
                    run = False
                    main_menu()

        pygame.display.update()

level_state = "Level 1-1"
world_state = "1"

def promijeni_level():
    global level_state, brojPtica, brzinaStvaranja, final_vrijeme, avioni_state, meteori_state, vjetar_state, brojAviona, brojMeteora, brojVjetra, vanzemaljac_state, brojVanzemaljca, world_state, pozadina, replay_state, odabrani_level
    if (level_state == "Level 1-1" and replay_state == False) or (odabrani_level == "Level 1-1" and replay_state == True): #leveli igrice
        pozadina = pygame.transform.scale(pygame.image.load("slike/world1_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 20 
        brzinaStvaranja = 2.5
        final_vrijeme = 20
        avioni_state=False
        meteori_state = False
        vjetar_state = False
        vanzemaljac_state = False
        world_state = "1"
    elif (level_state == "Level 1-2" and replay_state == False) or (odabrani_level == "Level 1-2" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("slike/world1_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 20
        brzinaStvaranja = 1.5
        final_vrijeme = 20
        avioni_state=False
        meteori_state = False
        vjetar_state = False
        vanzemaljac_state = False
        world_state = "1"
    elif (level_state == "Level 2-1" and replay_state == False) or (odabrani_level == "Level 2-1" and replay_state == True):   
        pozadina = pygame.transform.scale(pygame.image.load("slike/world2_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 20
        brzinaStvaranja = 2
        final_vrijeme = 20
        avioni_state=True
        meteori_state = False
        vjetar_state = False
        vanzemaljac_state = False
        brojAviona = 3
        world_state = "2"
    elif (level_state == "Level 2-2" and replay_state == False) or (odabrani_level == "Level 2-2" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("slike/world2_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 20
        brzinaStvaranja = 1.5
        final_vrijeme = 20
        avioni_state=True
        meteori_state = False
        vjetar_state = False
        vanzemaljac_state = False
        brojAviona = 5
        world_state = "2"
    elif (level_state == "Level 3-1" and replay_state == False) or (odabrani_level == "Level 3-1" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("slike/world3_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 10
        brzinaStvaranja = 2.5
        final_vrijeme = 20
        avioni_state=True
        meteori_state = True
        vjetar_state = False
        vanzemaljac_state = False
        brojAviona = 3
        brojMeteora = 3
        world_state = "3"
    elif (level_state == "Level 3-2" and replay_state == False) or (odabrani_level == "Level 3-2" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("slike/world3_bg.jpg"), (screen.get_width(), screen.get_height()))
        brojPtica = 15
        brzinaStvaranja = 2.5
        final_vrijeme = 20
        avioni_state=True
        meteori_state = True
        vjetar_state = False
        vanzemaljac_state = False
        brojAviona = 4
        brojMeteora = 5
        world_state = "3"
    elif (level_state == "Level 4-1" and replay_state == False) or (odabrani_level == "Level 4-1" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("slike/world4_bg.jpg"), (screen.get_width(), screen.get_height()))
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
        world_state = "4"
    elif (level_state == "Level 4-2" and replay_state == False) or (odabrani_level == "Level 4-2" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("slike/world4_bg.jpg"), (screen.get_width(), screen.get_height()))
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
        world_state = "4"
    elif (level_state == "Level 5-1" and replay_state == False) or (odabrani_level == "Level 5-1" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("slike/world5_bg.jpg"), (screen.get_width(), screen.get_height()))
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
        world_state = "5"
    elif (level_state == "Level 5-2" and replay_state == False) or (odabrani_level == "Level 5-2" and replay_state == True):
        pozadina = pygame.transform.scale(pygame.image.load("slike/world5_bg.jpg"), (screen.get_width(), screen.get_height()))
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
        world_state = "5"

def level_menu():
    global screen, text_font, text_font2, world_state, level_state, replay_state, odabrani_level
    pozadina_y = int(world_state)
    arrow = pygame.image.load("slike/arrow.png")
    run = True
    odabrani_level = level_state
    replay_state = False
    while run == True:
        if pozadina_y == 1: #pozicija leveli slike po svijetovima
            leveli_pozadina = pygame.transform.scale(pygame.image.load("slike/level_wrd1.jpg"), (screen.get_width(), screen.get_height()))
            LEVEL1_GUMB = Button("1-1", 70, "White", (120, 120), "Light Grey", "Green", (screen.get_width()*0.312, screen.get_height()*0.73))
            LEVEL2_GUMB = Button("1-2", 70, "White", (120, 120), "Light Grey", "Green", (screen.get_width()*0.6825, screen.get_height()*0.345))
        elif pozadina_y == 2:
            leveli_pozadina = pygame.transform.scale(pygame.image.load("slike/level_wrd2.jpg"), (screen.get_width(), screen.get_height()))
            LEVEL1_GUMB = Button("2-1", 70, "White", (120, 120), "Light Grey", "Green", (screen.get_width()*0.68, screen.get_height()*0.665))
            LEVEL2_GUMB = Button("2-2", 70, "White", (120, 120), "Light Grey", "Green", (screen.get_width()*0.312, screen.get_height()*0.285))
        elif pozadina_y == 3:
            leveli_pozadina = pygame.transform.scale(pygame.image.load("slike/level_wrd3.jpg"), (screen.get_width(), screen.get_height()))
            LEVEL1_GUMB = Button("3-1", 70, "White", (120, 120), "Light Grey", "Green", (screen.get_width()*0.312, screen.get_height()*0.73))
            LEVEL2_GUMB = Button("3-2", 70, "White", (120, 120), "Light Grey", "Green", (screen.get_width()*0.6825, screen.get_height()*0.345))
        elif pozadina_y == 4:
            leveli_pozadina = pygame.transform.scale(pygame.image.load("slike/level_wrd4.jpg"), (screen.get_width(), screen.get_height()))
            LEVEL1_GUMB = Button("4-1", 70, "White", (120, 120), "Light Grey", "Green", (screen.get_width()*0.6825, screen.get_height()*0.73))
            LEVEL2_GUMB = Button("4-2", 70, "White", (120, 120), "Light Grey", "Green", (screen.get_width()*0.312, screen.get_height()*0.345))
        elif pozadina_y == 5:
            leveli_pozadina = pygame.transform.scale(pygame.image.load("slike/level_wrd5.jpg"), (screen.get_width(), screen.get_height()))
            LEVEL1_GUMB = Button("5-1", 70, "White", (120, 120), "Light Grey", "Green", (screen.get_width()*0.32, screen.get_height()*0.655))
            LEVEL2_GUMB = Button("5-2", 70, "White", (120, 120), "Light Grey", "Green", (screen.get_width()*0.69, screen.get_height()*0.28))
        screen.blit(leveli_pozadina, (0,0))
        gore_arrow = Button_Slika(screen.get_width()/2.5,screen.get_height()*0.1,arrow, 0.5)
        dolje_arrow = Button_Slika(screen.get_width()/2.5,screen.get_height()*0.9,pygame.transform.flip(arrow, False, True), 0.5)
        if gore_arrow.draw(screen) and pozadina_y < 5:
            pozadina_y +=1
            time.sleep(0.2)
        if dolje_arrow.draw(screen) and pozadina_y > 1:
            pozadina_y -=1
            time.sleep(0.2)
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        IGRAJ_GUMB = Button("Nastavi", 70, "White", (220, 120), "Light Grey", "Green", (screen.get_width()*0.9, screen.get_height()*0.9))
        MAIN_GUMB = Button("Vrati se", 70, "White", (220, 120), "Light Grey", "Red", (screen.get_width()*0.1, screen.get_height()*0.9))
        draw_text(f"{odabrani_level}",text_font,(0,0,0),screen.get_width()/3,screen.get_height()/10)

        if level_state[-1] == "2": #stvori drugi gumb
            for gumb in [IGRAJ_GUMB, MAIN_GUMB, LEVEL1_GUMB, LEVEL2_GUMB]:
                        if gumb.checkForCollision(MENU_MOUSE_POS):
                            gumb.changeButtonColor()
                        gumb.update(screen)
        else: #stvori samo 1. gumb
            for gumb in [IGRAJ_GUMB, MAIN_GUMB, LEVEL1_GUMB]:
                if gumb.checkForCollision(MENU_MOUSE_POS):
                    gumb.changeButtonColor()
                gumb.update(screen)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
                    odabrani_level = "Level "+LEVEL1_GUMB.text_input
                    replay_state = True
                if LEVEL2_GUMB.checkForCollision(MENU_MOUSE_POS):
                    odabrani_level = "Level "+LEVEL2_GUMB.text_input
                    replay_state = True
        
        pygame.display.update()

def igra():
    global screen, text_font, brojPtica, brzinaStvaranja, final_vrijeme, avioni_state, meteori_state, vjetar_state, brojMeteora, brojVjetra, world_state, pozadina, skin_brojac, skinovi, level_state
    #slike
    zmaj_slika_og = skinovi[skin_brojac] #slika zmaja po skinu
    protivnik_og = pygame.image.load("slike/birds.png")
    sidebar = pygame.transform.scale(pygame.image.load("slike/sidebar.png"), (screen.get_width()*0.1651, screen.get_height()))
    sidebar1 = pygame.transform.scale(pygame.image.load("slike/sidebar1.png"), (screen.get_width()*0.1651, screen.get_height()))
    sidebar2 = pygame.transform.scale(pygame.image.load("slike/sidebar2.png"), (screen.get_width()*0.1651, screen.get_height()))
    sidebar3 = pygame.transform.scale(pygame.image.load("slike/sidebar3.png"), (screen.get_width()*0.1651, screen.get_height()))
    sidebar4 = pygame.transform.scale(pygame.image.load("slike/sidebar4.png"), (screen.get_width()*0.1651, screen.get_height()))
    zmaj_menu = pygame.transform.scale(zmaj_slika_og, (screen.get_width()*0.045, screen.get_height()*0.085))
    srce = pygame.transform.scale(pygame.image.load("slike/srce.png"), (screen.get_width()*0.05, screen.get_height()*0.08))
    fireball_og = pygame.image.load("slike/fireball.png")
    fireball_menu = pygame.transform.scale(fireball_og, (screen.get_width()*0.055, screen.get_height()*0.095))
    avion_og = pygame.image.load("slike/avion.png")
    meteor_og = pygame.image.load("slike/meteor.png")
    vjetar_og = pygame.transform.flip(pygame.image.load("slike/vjetar.png"), True, False)
    vanzemaljac_og = pygame.image.load("slike/alien.png")
    vanzemaljac_pucanj_og = pygame.image.load("slike/purple.png")
    powerup2_og = pygame.image.load("slike/blue.png")
    powerup2_menu = pygame.transform.scale(powerup2_og, (screen.get_width()*0.055, screen.get_height()*0.095))
    powerup3_og = pygame.image.load("slike/powerup3.png")
    powerup3_menu = pygame.transform.scale(powerup3_og, (screen.get_width()*0.055, screen.get_height()*0.095))
    powerup4_menu = pygame.transform.scale(pygame.image.load("slike/3balls.png"), (screen.get_width()*0.065, screen.get_height()*0.1))

    powerups = []
    #aktivacija powerupova određeni po svijetu
    if world_state == "1":
        powerups = []
        power_birac = -1
    if world_state == "2": 
        powerups = ["vatra"]
        power_birac = 0
    elif world_state == "3":
        powerups = ["vatra", "plava"]
        power_birac = 0
    elif world_state == "4":
        powerups = ["vatra", "plava", "riganje"]
        power_birac = 0
    elif world_state == "5":
        powerups = ["vatra", "plava", "riganje", "ciljanje"]
        power_birac = 0

    #vrijeme
    vrijeme = 0
    t1 = time.perf_counter()

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

    #nova slika zmaja
    zmaj_slika = pygame.transform.scale(zmaj_slika_og, (zmaj_w, zmaj_h))

    def stvoriProtivnike():
        for i in range(brojPtica): #stvaranje ptica
            #noviW i noviH
            noviWiH = zmaj_w/random.uniform(zmaj_w/2.5, zmaj_w/2)
            ProtivnikW.append(zmaj_w/noviWiH)
            ProtivnikH.append(zmaj_h/noviWiH)
            #noviX
            noviX = random.randint(0, int(screen.get_width()*0.834895-ProtivnikW[i])) #stvaranje x pozicije protivnika koja može bit od početka do kraja screena
            if i == 0: #za prvog protivnika uzima se bilo koji x
                ProtivnikX.append(noviX)
            else: #za ostale protivnike se uzima bilo koji x, ali ako je x u blizini prijašnjeg neprijatelja, bira se novi x. Tako neće doći do preklapanja protivnika
                while abs(ProtivnikX[i-1]-noviX) < ProtivnikW[i]:
                    noviX = random.randint(0, int(screen.get_width()*0.834895-ProtivnikW[i]))
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
            protivnikPomakY.append(random.uniform(screen.get_height() / 80,screen.get_height() / 50))

        if avioni_state == True: #stvaranje aviona
            for i in range(brojAviona):
                #noviW i noviH
                AvionW.append(random.uniform(zmaj_w*1.9, zmaj_w*1.6))
                AvionH.append(random.uniform(zmaj_h*0.45, zmaj_h*0.35))
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

        if meteori_state == True:
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

        if vjetar_state == True:
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
        
        if vanzemaljac_state == True:
            for i in range(brojVanzemaljca): #stvaranje meteora
                #noviW i noviH
                vanzemaljacNoviWiH = zmaj_w/random.uniform(zmaj_w, zmaj_w/1.2)
                VanzemaljacW.append(zmaj_w/vanzemaljacNoviWiH)
                VanzemaljacH.append(zmaj_h/vanzemaljacNoviWiH)
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
        if min(ProtivnikY) >= 0: #vraćanje ptica
            ProtivnikY[i] = 0 - ProtivnikH[i]*brzinaStvaranja #vraća protivnika natrag gore (isti kod kao i kod spawnanja)
            noviX = random.randint(0, int(screen.get_width()*0.834895-ProtivnikW[i]))
            while abs(ProtivnikX[i-1]-noviX) < ProtivnikW[i]:
                noviX = random.randint(0, int(screen.get_width()*0.834895-ProtivnikW[i]))
            else:
                ProtivnikX[i] = noviX
        else:
            ProtivnikY[i] = screen.get_height()

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

    def igrac(x,y):
        screen.blit(zmaj_slika, (x, y))
    
    def protivnik(x,y, i):
        screen.blit(ProtivnikSlika[i], (x, y))

    def avion(x,y, i):
        screen.blit(AvionSlika[i], (x, y))
    
    def meteor(x,y, i):
        screen.blit(MeteorSlika[i], (x, y))
    
    def vjetar(x,y,i):
        screen.blit(VjetarSlika[i], (x, y))

    def vanzemaljac(x,y,i):
        screen.blit(VanzemaljacSlika[i], (x, y))
    
    def vanzemaljacPucanj(x,y, i):
        screen.blit(pygame.transform.scale(vanzemaljac_pucanj_og, (power1_w, power1_h*1.5)), (x, y))

    stvoriProtivnike() #stvaranje neprijatelja

    run = True
    while run:
        clock = pygame.time.Clock()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
                    if len(powerups) != 0:
                        if power_birac == len(powerups)-1:
                            power_birac = 0
                        else:
                            power_birac +=1
                if event.button == 3:
                    if len(powerups) != 0:
                        if power_birac < 1:
                            power_birac = len(powerups)-1
                        else:
                            power_birac -= 1
                if event.button == 5:
                    if len(powerups) != 0:
                        if power_birac == len(powerups)-1:
                            power_birac = 0
                        else:
                            power_birac +=1
                if event.button == 4:
                    if len(powerups) != 0:
                        if power_birac < 1:
                            power_birac = len(powerups)-1
                        else:
                            power_birac -= 1

        screen.blit(pozadina, (0,0))

        progress = vrijeme/final_vrijeme

        #PRVI POWERUP
        power1_w = zmaj_w/4
        power1_h = zmaj_h/4
        pucanjPomak = -1*(screen.get_height() / 60)

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

        #DRUGI POWERUP
        power2_w = zmaj_w/2
        power2_h = zmaj_h/2
        pucanjPomak = -1*(screen.get_height() / 60)

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

        #TRECI POWERUP
        power3_w = zmaj_w*1.5
        power3_h = zmaj_h*1.5
        pucanjPomak = -1*(screen.get_height() / 60)
        
        #pomak pucnja
        if ispaljeno3 == True:
            if vrijeme - timer_cooldown3 < 6:
                isHit = True
                timer1 = 0 
                power3_y = zmaj_y-zmaj_h/4 #u trenutku pucanja stavlja pucanj kod zmaja
                power3_x = zmaj_x-zmaj_w/4
                screen.blit(pygame.transform.scale(powerup3_og,(power3_w,power3_h)), (power3_x, power3_y))
            else:
                ispaljeno3 = False
                isHit = False
        else: #kada ne puca, stavlja pucanj off screen
            power3_y = screen.get_height() + power2_h*2
            power3_x = -power2_w*2
        
        #CETVRTI POWERUP
        power4_w = zmaj_w/3.5
        power4_h = zmaj_h/3.5

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
            protivnik(ProtivnikX[i],ProtivnikY[i], i) #crtanje protivnika

            if ProtivnikY[i] > screen.get_height(): #respawnanje protivnika
                if vrijeme < final_vrijeme-3: #ograničenje da se ne respawnaju zauvijek
                    vratiProtivnika(i)
                
            if pygame.Rect(ProtivnikX[i], ProtivnikY[i], ProtivnikW[i], ProtivnikH[i]).colliderect(pygame.Rect(zmaj_x,zmaj_y,zmaj_w,zmaj_h)) and isHit == False: #collision protivnika
                život -= 1
                isHit = True
                timer1 = vrijeme
            
            if pygame.Rect(ProtivnikX[i], ProtivnikY[i], ProtivnikW[i], ProtivnikH[i]).colliderect(pygame.Rect(power1_x, power1_y, power1_w, power1_h)): #collision pucnja i protivnika
                ispaljeno1 = False
                vratiProtivnika(i)
            
            if ispaljeno2 == True:
                if pygame.Rect(ProtivnikX[i], ProtivnikY[i], ProtivnikW[i], ProtivnikH[i]).colliderect(pygame.Rect(power2_x, power2_y, power2_w, power2_h)): #collision pucnja i protivnika
                    vratiProtivnika(i)
            
            if ispaljeno3 == True:
                if pygame.Rect(ProtivnikX[i], ProtivnikY[i], ProtivnikW[i], ProtivnikH[i]).colliderect(pygame.Rect(power3_x, power3_y, power3_w, power3_h)): #collision pucnja i protivnika
                    vratiProtivnika(i)
            
            if ispaljeno4 == True:
                for l in range(3):
                    if pygame.Rect(ProtivnikX[i], ProtivnikY[i], ProtivnikW[i], ProtivnikH[i]).colliderect(pygame.Rect(power4_x[l], power4_y[l], power4_w, power4_h)): #collision pucnja i protivnika
                        vratiProtivnika(i)

        if avioni_state == True:
            for i in range(brojAviona): 
                AvionX[i] += AvionPomakX[i] #micanje protivnika
                avion(AvionX[i],AvionY[i], i) #crtanje protivnika

                if AvionX[i] > screen.get_width()*0.834895:
                    if vrijeme < final_vrijeme-3: #ograničenje da se ne respawnaju zauvijek
                        vratiAvion(i)
                    
                if pygame.Rect(AvionX[i], AvionY[i], AvionW[i], AvionH[i]).colliderect(pygame.Rect(zmaj_x,zmaj_y,zmaj_w,zmaj_h)) and isHit == False: #collision protivnika
                    život -= 1
                    isHit = True
                    timer1 = vrijeme
                
                if pygame.Rect(AvionX[i], AvionY[i], AvionW[i], AvionH[i]).colliderect(pygame.Rect(power1_x, power1_y, power1_w, power1_h)): #collision pucnja i protivnika
                    ispaljeno1 = False
                    vratiAvion(i)
                
                if ispaljeno2 == True:
                    if pygame.Rect(AvionX[i], AvionY[i], AvionW[i], AvionH[i]).colliderect(pygame.Rect(power2_x, power2_y, power2_w, power2_h)): #collision pucnja i protivnika
                        vratiAvion(i)
                
                if ispaljeno3 == True:
                    if pygame.Rect(AvionX[i], AvionY[i], AvionW[i], AvionH[i]).colliderect(pygame.Rect(power3_x, power3_y, power3_w, power3_h)): #collision pucnja i protivnika
                        vratiAvion(i)

                if ispaljeno4 == True:
                    for l in range(3):
                        if pygame.Rect(AvionX[i], AvionY[i], AvionW[i], AvionH[i]).colliderect(pygame.Rect(power4_x[l], power4_y[l], power4_w, power4_h)): #collision pucnja i protivnika
                            vratiAvion(i)

        if meteori_state == True:
            for i in range(brojMeteora): 
                MeteorY[i] += MeteorPomakY[i] #micanje protivnika
                MeteorX[i] += MeteorPomakX[i]
                meteor(MeteorX[i],MeteorY[i], i) #crtanje protivnika

                if MeteorY[i] > screen.get_height(): #respawnanje protivnika
                    if vrijeme < final_vrijeme-3: #ograničenje da se ne respawnaju zauvijek
                        vratiMeteor(i)
                
                if MeteorX[i] > screen.get_width()*0.834895-MeteorW[i] or MeteorX[i] <= 0: #ako meteor dira granice, odbija se u drugu stranu
                    MeteorPomakX[i] = -1*MeteorPomakX[i]

                if pygame.Rect(MeteorX[i], MeteorY[i], MeteorW[i], MeteorH[i]).colliderect(pygame.Rect(zmaj_x,zmaj_y,zmaj_w,zmaj_h)) and isHit == False: #collision protivnika
                    život -= 1
                    isHit = True
                    timer1 = vrijeme
                
                if ispaljeno1 == True:
                    if pygame.Rect(MeteorX[i], MeteorY[i], MeteorW[i], MeteorH[i]).colliderect(pygame.Rect(power1_x, power1_y, power1_w, power1_h)): #collision pucnja i protivnika
                        ispaljeno1 = False

                if ispaljeno2 == True:
                    if pygame.Rect(MeteorX[i], MeteorY[i], MeteorW[i], MeteorH[i]).colliderect(pygame.Rect(power2_x, power2_y, power2_w, power2_h)): #collision pucnja i protivnika
                        ispaljeno2 = False
                        vratiMeteor(i)

                if ispaljeno3 == True:
                    if pygame.Rect(MeteorX[i], MeteorY[i], MeteorW[i], MeteorH[i]).colliderect(pygame.Rect(power3_x, power3_y, power3_w, power3_h)): #collision pucnja i protivnika
                        vratiMeteor(i)
                
                if ispaljeno4 == True:
                    for l in range(3):
                        if pygame.Rect(MeteorX[i], MeteorY[i], MeteorW[i], MeteorH[i]).colliderect(pygame.Rect(power4_x[l], power4_y[l], power4_w, power4_h)): #collision pucnja i protivnika
                            vratiMeteor(i)

        if vjetar_state == True:
            for i in range(brojVjetra): 
                VjetarX[i] -= VjetarPomakX[i] #micanje protivnika
                vjetar(VjetarX[i],VjetarY[i], i) #crtanje protivnika

                if VjetarX[i] < -VjetarW[i]:
                    if vrijeme < final_vrijeme-3: #ograničenje da se ne respawnaju zauvijek
                        vratiVjetar(i)
                    
                if pygame.Rect(VjetarX[i], VjetarY[i], VjetarW[i], VjetarH[i]).colliderect(pygame.Rect(zmaj_x,zmaj_y,zmaj_w,zmaj_h)): #collision protivnika
                    zmaj_x -= VjetarPomakX[i]
                
                if ispaljeno3 == True:
                    if pygame.Rect(VjetarX[i], VjetarY[i], VjetarW[i], VjetarH[i]).colliderect(pygame.Rect(power3_x,power3_y,power3_w,power3_h)): #collision protivnika
                        vratiVjetar(i)
                
        if vanzemaljac_state == True:
            for i in range(brojVanzemaljca): 
                VanzemaljacY[i] += VanzemaljacPomakY[i] #micanje protivnika
                vanzemaljac(VanzemaljacX[i],VanzemaljacY[i], i) #crtanje protivnika

                if VanzemaljacY[i] >= screen.get_height()/5: #respawnanje protivnika
                    VanzemaljacPomakY[i] = 0
                    vanzemaljac_pucanje[i] = True
                    VanzemaljacX[i] += VanzemaljacPomakX[i]

                if VanzemaljacX[i] > screen.get_width()*0.834895-VanzemaljacW[i] or VanzemaljacX[i] <= 0: #ako meteor dira granice, odbija se u drugu stranu
                    VanzemaljacPomakX[i] = -1*VanzemaljacPomakX[i]

                if pygame.Rect(VanzemaljacX[i], VanzemaljacY[i], VanzemaljacW[i], VanzemaljacH[i]).colliderect(pygame.Rect(zmaj_x,zmaj_y,zmaj_w,zmaj_h)) and isHit == False: #collision protivnika
                    život -= 1
                    isHit = True
                    timer1 = vrijeme
                
                if ispaljeno1 == True:
                    if pygame.Rect(VanzemaljacX[i], VanzemaljacY[i], VanzemaljacW[i], VanzemaljacH[i]).colliderect(pygame.Rect(power1_x, power1_y, power1_w, power1_h)): #collision pucnja i protivnika
                        ispaljeno1 = False
                        vanzemaljac_pucanje[i] = False
                        vratiVanzemaljca(i)
                
                if ispaljeno2 == True:
                    if pygame.Rect(VanzemaljacX[i], VanzemaljacY[i], VanzemaljacW[i], VanzemaljacH[i]).colliderect(pygame.Rect(power2_x, power2_y, power2_w, power2_h)): #collision pucnja i protivnika
                        vanzemaljac_pucanje[i] = False
                        vratiVanzemaljca(i)
                
                if ispaljeno3 == True:
                    if pygame.Rect(VanzemaljacX[i], VanzemaljacY[i], VanzemaljacW[i], VanzemaljacH[i]).colliderect(pygame.Rect(power3_x, power3_y, power3_w, power3_h)): #collision pucnja i protivnika
                        vanzemaljac_pucanje[i] = False
                        vratiVanzemaljca(i)
                
                if ispaljeno4 == True:
                    for l in range(3):
                        if pygame.Rect(VanzemaljacX[i], VanzemaljacY[i], VanzemaljacW[i], VanzemaljacH[i]).colliderect(pygame.Rect(power4_x[l], power4_y[l], power4_w, power4_h)): #collision pucnja i protivnika
                            vanzemaljac_pucanje[i] = False
                            vratiVanzemaljca(i)

                if vanzemaljac_pucanje[i] == True:
                    VanzemaljacPucanjY[i] += VanzemaljacPucanjPomakY[i]
                    vanzemaljacPucanj(VanzemaljacPucanjX[i], VanzemaljacPucanjY[i], i)
                else:
                    VanzemaljacPucanjX[i] = VanzemaljacX[i] + VanzemaljacW[i]/2
                    VanzemaljacPucanjY[i] = VanzemaljacY[i] + VanzemaljacH[i]/2
                    #ograničenje pucnja
                if VanzemaljacPucanjY[i] > screen.get_height():
                    VanzemaljacPucanjX[i] = VanzemaljacX[i] +VanzemaljacW[i]/2
                    VanzemaljacPucanjY[i] = VanzemaljacY[i] + VanzemaljacH[i]/2
                
                if pygame.Rect(VanzemaljacPucanjX[i], VanzemaljacPucanjY[i], power1_w, power1_h*1.5).colliderect(pygame.Rect(zmaj_x,zmaj_y,zmaj_w,zmaj_h)) and isHit == False: #collision protivnika
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
        igrac(zmaj_x,zmaj_y)
        #vrijeme
        t2 = time.perf_counter()
        vrijeme =round(t2-t1,1)

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
                screen.blit(plavi_nepucan, (zmaj_x-zmaj_w/4, zmaj_y-zmaj_h/4))
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
        draw_text(f"{ime}",text_font,(0,0,0),screen.get_width()*0.865,screen.get_height()*0.05)
        for i in range(život+1):
            x = screen.get_width()*0.05
            screen.blit(srce,(screen.get_width()*0.84375+x*i,screen.get_height()*0.145))

        #slike powerupova u sidebaru
        if world_state != "1":
            if vrijeme - timer_cooldown1 < cooldown1: #crtanje powerupa u sidebaru
                draw_text(f"{round((vrijeme - timer_cooldown1),1)}s",text_font,(0,0,0),screen.get_width()*0.85,screen.get_height()*0.28)
                fireball_menu.set_alpha(150)
                screen.blit(fireball_menu,(screen.get_width()*0.847,screen.get_height()*0.27))
            else:
                fireball_menu.set_alpha(256)
                screen.blit(fireball_menu,(screen.get_width()*0.847,screen.get_height()*0.27))
        
        if world_state != "1" and world_state != "2":
            if vrijeme - timer_cooldown2 < cooldown2: #crtanje powerupa u sidebaru
                draw_text(f"{round((vrijeme - timer_cooldown2),1)}s",text_font,(0,0,0),screen.get_width()*0.85,screen.get_height()*0.45)
                powerup2_menu.set_alpha(150)
                screen.blit(powerup2_menu,(screen.get_width()*0.847,screen.get_height()*0.45))
            else:
                powerup2_menu.set_alpha(256)
                screen.blit(powerup2_menu,(screen.get_width()*0.847,screen.get_height()*0.45))
        
        if world_state == "4" or world_state == "5":
            if vrijeme - timer_cooldown3 < cooldown3: #crtanje powerupa u sidebaru
                draw_text(f"{round((vrijeme - timer_cooldown3),1)}s",text_font,(0,0,0),screen.get_width()*0.85,screen.get_height()*0.62)
                powerup3_menu.set_alpha(150)
                screen.blit(powerup3_menu,(screen.get_width()*0.847,screen.get_height()*0.62))
            else:
                powerup3_menu.set_alpha(256)
                screen.blit(powerup3_menu,(screen.get_width()*0.847,screen.get_height()*0.62))
            
        if world_state == "5":
            if vrijeme - timer_cooldown4 < cooldown4: #crtanje powerupa u sidebaru
                draw_text(f"{round((vrijeme - timer_cooldown4),1)}s",text_font,(0,0,0),screen.get_width()*0.85,screen.get_height()*0.79)
                powerup4_menu.set_alpha(150)
                screen.blit(powerup4_menu,(screen.get_width()*0.842,screen.get_height()*0.79))
            else:
                powerup4_menu.set_alpha(256)
                screen.blit(powerup4_menu,(screen.get_width()*0.842,screen.get_height()*0.79))

        x = - screen.get_height()*0.52
        screen.blit(zmaj_menu, (screen.get_width()*0.93,screen.get_height()*0.816+(x*progress)))
        
        if progress == 1:
            run = False
            if replay_state == False:
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
            level_menu()

        if život < 0: #pokrece game_over funkciju ako ostaneš bez života
            run = False
            game_over()
        
        pygame.display.update()

if __name__ == "__main__":
    main()
