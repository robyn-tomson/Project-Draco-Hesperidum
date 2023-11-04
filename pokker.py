import pygame
from button import Button
from button import Tekstivali
from button import set_text
import kaardipakk
from kaardipakk import kaartidimg
from kaardipakk import kaardigen
import random
#MAIN skript
pygame.init()
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
red = (255,67,89)
white = (255,255,255)
#teeb nuppu, ei ole veel ekraanile kuvatud
#vajalikud muutujad
round=0
ettevalmistus=1
algus=0
imp=[]
imp2=[]
impsina=[]
impsina2=[]
kaartid=[]
sinukaartid=[]
vaenlasekaartid=[]
active=False
run= True
user_text=""
panus=5
sinuraha=100
vaenlaseraha=100
buttonOne = Button(150, 150, 200, 200, red, 0, 7, "RAISE", white, screen, pygame.font.Font('freesansbold.ttf', 40))
Tekst = Tekstivali(30, 300, 70, 70, (0,0,250), 0, 7, str(round), white, screen, pygame.font.Font('freesansbold.ttf', 40))
sinurahab=Tekstivali(600, 0, 70, 70, (0,0,250), 0, 7, str(sinuraha), white, screen, pygame.font.Font('freesansbold.ttf', 40))
vaenlaserahab=Tekstivali(500, 0, 70, 70, red, 0, 7, str(sinuraha), white, screen, pygame.font.Font('freesansbold.ttf', 40))
#mida kood teeb töö ajal
while run:
    #teeb valmis kaartid kuvamiseks
    if ettevalmistus==1 and round==1:
        for i in range(3):         
            kaartid.append(kaardipakk.kaardigen(kaartid))
            print(kaartid)
        for l in range(3):
            imp.append(pygame.image.load("C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid\\"+kaardipakk.kaartidimg(kaartid[l])).convert())
            imp2.append(pygame.transform.scale(imp[l], (125, 181)))
        ettevalmistus=0
    if ettevalmistus==1 and round==0:
        for i in range(2): 
            sinukaartid.append(kaardipakk.kaardigen(sinukaartid))
            vaenlasekaartid.append(kaardipakk.kaardigen(vaenlasekaartid))
            print(kaartid)
        for l in range(2):
            impsina.append(pygame.image.load("C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid\\"+kaardipakk.kaartidimg(sinukaartid[l])).convert())
            impsina2.append(pygame.transform.scale(impsina[l], (125, 181)))
        ettevalmistus=0
    #täidab ekraani mustaga
    screen.fill((0,0,0))
    #paneb kaartid ekraanile
    for el in imp2:
        screen.blit(el, (algus, 0))
        algus+=125
    algus=0
    for al in impsina2:
        screen.blit(al, (algus, 400))
        algus+=125
    algus=0
    #paneb teksti ekraanile
    Tekst.drawRect()
    #muudab teksti
    Tekst.text=str(panus)
    sinurahab.drawRect()
    vaenlaserahab.drawRect()
    #muudab teksti
    sinurahab.text=str(sinuraha)
    vaenlaserahab.text=str(vaenlaseraha)
    #paneb nuppu ekraanile
    button=buttonOne.drawRect()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        #tuvastab nuppule vajutusi
        if Button.tee(event, button):
                active = True
        if active:
            buttonOne.text=user_text
        if event.type == pygame.KEYDOWN and active: 
            if event.key == pygame.K_0:
                sinuraha+=100
            if event.key == pygame.K_RETURN:
                buttonOne.text="RAISE"
                try:
                    if int(user_text)>sinuraha:
                        buttonOne.text="vale"
                    else:
                        panus+=int(user_text)
                        sinuraha-=int(user_text)
                        round=1
                        ettevalmistus=1
                except:
                    user_text=""
                    buttonOne.text="vale"
                user_text=""
                active=False
            elif event.key == pygame.K_BACKSPACE:
                user_text= user_text[:-1]
            else: 
                user_text += event.unicode
    #uuendab ekraani
    pygame.display.update()
pygame.quit()