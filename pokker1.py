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

def pokker1(screen):
    pygame.init()
    red = (255,67,89)
    white = (255,255,255)
    #teeb nuppu, ei ole veel ekraanile kuvatud
    #vajalikud muutujad
    round=0
    ettevalmistus=1
    algus=0
    imp=[]
    impsina=[]
    impvaenlane=[]
    kaartid=[]
    sinukaartid=[]
    vaenlasekaartid=[]
    active=False
    run= True
    user_text=""
    panus=5
    raha=0
    vaenpanraha=0
    sinupanraha=0
    sinuraha=100
    vaenlaseraha=100
    vaenlasekäik=False
    vaenlaseraise=False
    sinuraise=True
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
    pygame.mixer.music.load("Project-Draco-Hesperidum\\muusika\\mang.mp3")#music file 
    pygame.mixer.music.play(-1)
    while run:
    #teeb valmis kaartid kuvamiseks
        if ettevalmistus==1 and round==0:
            panus=5 
            raha=0
            impsina=[]
            impvaenlane=[]
            for i in range(2): 
                sinukaartid.append(kaardipakk.kaardigen(sinukaartid))
                vaenlasekaartid.append(kaardipakk.kaardigen(vaenlasekaartid))
            for l in range(2):
                impsina.append(pygame.transform.scale(pygame.image.load("C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid\\"+kaardipakk.kaartidimg(sinukaartid[l])).convert(), (125, 181)))
                impvaenlane.append(pygame.transform.scale(pygame.image.load("C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid\\"+kaardipakk.kaartidimg(vaenlasekaartid[l])).convert(), (125, 181)))
            ettevalmistus=0
        if ettevalmistus==1 and round==1:
            panus=0
            for i in range(3):         
                kaartid.append(kaardipakk.kaardigen(kaartid))
            for l in range(3):
                imp.append(pygame.transform.scale(pygame.image.load("C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid\\"+kaardipakk.kaartidimg(kaartid[l])).convert(), (125, 181)))
            ettevalmistus=0
        if ettevalmistus==1 and round==2:  
            panus=0     
            kaartid.append(kaardipakk.kaardigen(kaartid))
            imp.append(pygame.transform.scale(pygame.image.load("C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid\\"+kaardipakk.kaartidimg(kaartid[-1])).convert(), (125, 181)))
            ettevalmistus=0
        if ettevalmistus==1 and round==3: 
            panus=5     
            kaartid.append(kaardipakk.kaardigen(kaartid))
            imp.append(pygame.transform.scale(pygame.image.load("C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid\\"+kaardipakk.kaartidimg(kaartid[-1])).convert(), (125, 181)))
            ettevalmistus=0
        if round==4:
            round=6
            if pokerhand(sinukaartid+kaartid)>pokerhand(vaenlasekaartid+kaartid):
                sinuraha+=raha
                tekstväärtus=True
                võitja.text="sa võitsid"
            elif pokerhand(sinukaartid+kaartid)<pokerhand(vaenlasekaartid+kaartid):
                tekstväärtus=True
                võitja.text="vaenlane võitis"
                vaenlaseraha+=raha
            else:
                tekstväärtus=True
                võitja.text="viik"
                vaenlaseraha+=raha//2
                sinuraha+=raha//2
            if sinuraha<=0:
                return "kaotus"
            if vaenlaseraha<=0:
                return "võit"
        #täidab ekraani mustaga
        screen.fill((0,150,0))
        #paneb kaartid ekraanile
        algus=50
        for el in imp:
            screen.blit(el, (algus, 50))
            algus+=125
        algus=50
        for al in impsina:
            screen.blit(al, (algus, 400))
            algus+=125
        algus=50
        #paneb teksti ekraanile
        Tekst.drawRect()
        sinurahab.drawRect()
        vaenlaserahab.drawRect()
        rahab.drawRect()
        fold.drawRect()

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
            if tekstväärtus and Button.tee(event, uusroundpu):
                    round=0
                    tekstväärtus=False
            if round!=6:
                if Button.tee(event, callpu):
                        if vaenlasekäik==False:
                            raha+=(panus-sinupanraha)
                            sinuraha-=(panus-sinupanraha)
                            sinupanraha+=panus
                            vaenlasekäik=True
                            if vaenlaseraise:
                                round+=1
                                ettevalmistus=1
                                sinupanraha=0
                                vaenpanraha=0
                                vaenlasekäik=False
                                vaenlaseraise=False
                if Button.tee(event, foldpu):
                        vaenlaseraha+=raha
                        tekstväärtus=True
                        võitja.text="vaenlane võitis"
                if Button.tee(event, raisepu):
                        if vaenlasekäik==False:
                            active = True
                if active:
                    raisep.text=user_text
                if event.type == pygame.KEYDOWN and active: 
                    if event.key == pygame.K_RETURN:
                        raisep.text="RAISE"
                        try:
                            if int(user_text)>sinuraha or int(user_text)<=panus:
                                raisep.text="vale"
                            else:
                                vaenlasekäik=True
                                panus=int(user_text)
                                sinuraha-=(int(user_text)-sinupanraha)
                                raha+=(panus-sinupanraha)
                                sinupanraha=panus
                        except:
                            user_text=""
                            raisep.text="vale"
                        user_text=""
                        active=False
                    elif event.key == pygame.K_BACKSPACE:
                        user_text= user_text[:-1]
                    else: 
                        user_text += event.unicode
            if vaenlasekäik:
                tegu=vaenlane(pokerhand(vaenlasekaartid+kaartid), round,  sinuraha, vaenlaseraha, panus)
                print(tegu)
                if isinstance(tegu, int):
                    panus=tegu
                    raha+=(panus-vaenpanraha)
                    vaenlaseraha-=(panus-vaenpanraha)
                    vaenpanraha=panus
                    vaenlasekäik=False
                    vaenlaseraise=True
                elif tegu=="call":
                    raha+=(panus-vaenpanraha)
                    vaenlaseraha-=(panus-vaenpanraha)
                    vaenpanraha=0
                    sinupanraha=0
                    round+=1
                    ettevalmistus=1
                    vaenlasekäik=False
                else:
                    tekstväärtus=True
                    võitja.text="sa võitsid"
                    sinuraha+=raha
        if tekstväärtus:
            uusroundpu=uusround.drawRect()
            võitja.drawRect()
            algus=0
            for ef in impvaenlane:
                screen.blit(ef, (algus, 0))
                algus+=125
            raha=0
            ettevalmistus=1
            kaartid=[]
            imp=[]
            sinukaartid=[]
            vaenlasekaartid=[]
            vaenpanraha=0
            sinupanraha=0
            vaenlaseraise=False
            algus=50
        #uuendab ekraani
        pygame.display.update()
    pygame.quit()