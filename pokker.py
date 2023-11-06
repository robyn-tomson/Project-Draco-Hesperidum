import pygame
from button import Button
from button import Tekstivali
from button import set_text
import kaardipakk
from kaardipakk import kaartidimg
from kaardipakk import kaardigen
import random
from pokkerikäsi import pokerhand
from vaenlane import vaenlane
#MAIN skript
pygame.init()
SCREEN_WIDTH=1100
SCREEN_HEIGHT=700
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
raha=0
sinuraha=100
vaenlaseraha=100
vaenlasekäik=False
vaenlaseraise=False
tekstväärtus=False
uusround= Button(100, 200, 50, 400, (50,50,50), 0, 7, "UUS ROUND", white, screen, pygame.font.Font('freesansbold.ttf', 40))
call= Button(350, 400, 100, 200, red, 0, 7, "CALL", white, screen, pygame.font.Font('freesansbold.ttf', 40))
fold=Button(875, 400, 100, 200, red, 0, 7, "FOLD", white, screen, pygame.font.Font('freesansbold.ttf', 40))
raisep = Button(625, 400, 100, 200, red, 0, 7, "RAISE", white, screen, pygame.font.Font('freesansbold.ttf', 40))
Tekst = Tekstivali(30, 300, 70, 200, (0,0,250), 0, 7, "panus: "+str(panus), white, screen, pygame.font.Font('freesansbold.ttf', 40))
võitja = Tekstivali(600, 300, 50, 400, (0,0,250), 0, 7, "", white, screen, pygame.font.Font('freesansbold.ttf', 40))
rahab=Tekstivali(250, 300, 70, 200, (0,0,250), 0, 7, "hunnik: "+str(raha), white, screen, pygame.font.Font('freesansbold.ttf', 40))
sinurahab=Tekstivali(700, 0, 70, 375, (0,0,250), 0, 7, "sinu raha: "+str(sinuraha), white, screen, pygame.font.Font('freesansbold.ttf', 40))
vaenlaserahab=Tekstivali(700, 100, 70, 375, red, 0, 7, "vaenlase raha: "+str(vaenlaseraha), white, screen, pygame.font.Font('freesansbold.ttf', 40))
#mida kood teeb töö ajal
while run:
    #teeb valmis kaartid kuvamiseks
    if ettevalmistus==1 and round==1:
        panus=0
        for i in range(3):         
            kaartid.append(kaardipakk.kaardigen(kaartid))
            print(kaartid)
        for l in range(3):
            imp.append(pygame.image.load("C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid\\"+kaardipakk.kaartidimg(kaartid[l])).convert())
            imp2.append(pygame.transform.scale(imp[l], (125, 181)))
        ettevalmistus=0
    if ettevalmistus==1 and round==2:  
        panus=0     
        kaartid.append(kaardipakk.kaardigen(kaartid))
        imp.append(pygame.image.load("C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid\\"+kaardipakk.kaartidimg(kaartid[-1])).convert())
        imp2.append(pygame.transform.scale(imp[-1], (125, 181)))
        ettevalmistus=0
    if ettevalmistus==1 and round==3: 
        panus=5     
        kaartid.append(kaardipakk.kaardigen(kaartid))
        imp.append(pygame.image.load("C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid\\"+kaardipakk.kaartidimg(kaartid[-1])).convert())
        imp2.append(pygame.transform.scale(imp[-1], (125, 181)))
        ettevalmistus=0
        if random.randint(1,10)>5:
            sinuraha+=raha
            tekstväärtus=True
            võitja.text="sa võitsid"
        else:
            tekstväärtus=True
            võitja.text="vaenlane võitis"
            vaenlaseraha+=raha
        raha=0
        round=0
        ettevalmistus=1
        kaartid=[]
        imp=[]
        imp2=[]
        sinukaartid=[]
        vaenlasekaartid=[]
        impsina2=[]
        impsina=[]
    if ettevalmistus==1 and round==0:
        panus=5 
        raha=0
        for i in range(2): 
            sinukaartid.append(kaardipakk.kaardigen(sinukaartid))
            vaenlasekaartid.append(kaardipakk.kaardigen(vaenlasekaartid))
            print(kaartid)
        for l in range(2):
            impsina.append(pygame.image.load("C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid\\"+kaardipakk.kaartidimg(sinukaartid[l])).convert())
            impsina2.append(pygame.transform.scale(impsina[l], (125, 181)))
        ettevalmistus=0
    #täidab ekraani mustaga
    screen.fill((0,150,0))
    #paneb kaartid ekraanile
    for el in imp2:
        screen.blit(el, (algus, 50))
        algus+=125
    algus=50
    for al in impsina2:
        screen.blit(al, (algus, 400))
        algus+=125
    algus=50
    #paneb teksti ekraanile
    Tekst.drawRect()
    #muudab teksti
    sinurahab.drawRect()
    vaenlaserahab.drawRect()
    rahab.drawRect()
    fold.drawRect()
    if tekstväärtus:
        uusroundpu=uusround.drawRect()
        võitja.drawRect()
    #muudab teksti
    sinurahab.text="sinu raha: "+str(sinuraha)
    vaenlaserahab.text="vaenlase raha: "+str(vaenlaseraha)
    Tekst.text="panus: "+str(panus)
    rahab.text="hunnik: "+str(raha)
    #paneb nuppu ekraanile
    foldpu=fold.drawRect()
    raisepu=raisep.drawRect()
    callpu=call.drawRect()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        #tuvastab nuppule vajutusi
        if Button.tee(event, callpu):
                if vaenlasekäik==False:
                    raha+=panus
                    sinuraha-=panus
                    vaenlasekäik=True
                if vaenlaseraise:
                    round+=1
                    ettevalmistus=1
                    vaenlaseraise=False
        if tekstväärtus and Button.tee(event, uusroundpu):
            tekstväärtus=False
        if Button.tee(event, foldpu):
                vaenlaseraha+=raha
                tekstväärtus=True
                võitja.text="vaenlane võitis"
                raha=0
                round=0
                ettevalmistus=1
                kaartid=[]
                imp=[]
                imp2=[]
                sinukaartid=[]
                vaenlasekaartid=[]
                impsina2=[]
                impsina=[]
                vaenlaseraha+=raha
        if Button.tee(event, raisepu):
                if vaenlasekäik==False:
                    active = True
        if active:
            raisepu.text=user_text
        if event.type == pygame.KEYDOWN and active: 
            if event.key == pygame.K_RETURN:
                raisepu.text="RAISE"
                try:
                    if int(user_text)>sinuraha or int(user_text)<=panus:
                        raisepu.text="vale"
                    else:
                        vaenlasekäik=True
                        panus=int(user_text)
                        sinuraha-=int(user_text)
                except:
                    user_text=""
                    raisepu.text="vale"
                user_text=""
                active=False
            elif event.key == pygame.K_BACKSPACE:
                user_text= user_text[:-1]
            else: 
                user_text += event.unicode
        if vaenlasekäik:
            tegu=vaenlane(1, round,  sinuraha, vaenlaseraha, panus)
            print(tegu)
            if isinstance(tegu, int):
                panus=tegu
                raha+=panus
                vaenlaseraha-=panus
                vaenlasekäik=False
                vaenlaseraise=True
            elif tegu=="call":
                round+=1
                ettevalmistus=1
                raha+=panus
                vaenlaseraha-=panus
                vaenlasekäik=False
            else:
                tekstväärtus=True
                võitja.text="sa võitsid"
                sinuraha+=raha
                round=0
                ettevalmistus=1
                kaartid=[]
                imp=[]
                imp2=[]
                sinukaartid=[]
                vaenlasekaartid=[]
                impsina2=[]
                impsina=[]
    #uuendab ekraani
    pygame.display.update()
pygame.quit()