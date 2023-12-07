import pygame
from button import Button
from button import Tekstivali
import kaardipakk
from kaardipakk import kaartidimg
from kaardipakk import kaardigen
from pokkerikäsi import pokerhand
from vaenlane import vaenlane
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
#MAIN skript

def pokker1(screen):
    pygame.init()
    red = (255,67,89)
    white = (255,255,255)
    #teeb nuppu, ei ole veel ekraanile kuvatud
    #vajalikud muutujad
    rounds=0
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
    tekstväärtus=False
    timer=0.0
    clock = pygame.time.Clock()
    uusround= Button(100, 200, 50, 400, (50,50,50), 0, 7, "UUS ROUND", white, screen, pygame.font.Font('freesansbold.ttf', 40))
    call= Button(350, 550, 100, 200, red, 0, 7, "CALL", white, screen, pygame.font.Font('freesansbold.ttf', 40))
    fold=Button(875, 550, 100, 200, red, 0, 7, "FOLD", white, screen, pygame.font.Font('freesansbold.ttf', 40))
    raisep = Button(625, 550, 100, 200, red, 0, 7, "RAISE", white, screen, pygame.font.Font('freesansbold.ttf', 40))
    Menu=Button(875, 550, 100, 200, red, 0, 7, "FOLD", white, screen, pygame.font.Font('freesansbold.ttf', 40))
    Tekst = Tekstivali(660, 240, 70, 200, (0,0,250), 0, 7, "panus: "+str(panus), white, screen, pygame.font.Font('freesansbold.ttf', 40))
    võitja = Tekstivali(100, 100, 50, 400, (0,0,250), 0, 7, "", white, screen, pygame.font.Font('freesansbold.ttf', 40))
    vaenlasebet=Tekstivali(100, 250, 150, 390, red, 0, 7, "", white, screen, pygame.font.Font('freesansbold.ttf', 40))
    sinupanus=Tekstivali(740, 350, 70, 300, (0,0,250), 0, 7, "", white, screen, pygame.font.Font('freesansbold.ttf', 40))
    rahab=Tekstivali(880, 240, 70, 200, (0,0,250), 0, 7, "hunnik: "+str(raha), white, screen, pygame.font.Font('freesansbold.ttf', 40))
    sinurahab=Tekstivali(700, 0, 70, 375, (0,0,250), 0, 7, "sinu raha: "+str(sinuraha), white, screen, pygame.font.Font('freesansbold.ttf', 40))
    vaenlaserahab=Tekstivali(700, 100, 70, 375, red, 0, 7, "vaenlase raha: "+str(vaenlaseraha), white, screen, pygame.font.Font('freesansbold.ttf', 40))
    #mida kood teeb töö ajal
    pygame.mixer.music.load("Project-Draco-Hesperidum\\muusika\\mang.mp3")#music file 
    pygame.mixer.music.play(-1)
    settings=False
    smallfont = pygame.font.SysFont('Corbel',35)
    slider = Slider(screen, 40, 165, 100, 20, min=0, max=99, step=1)
    slider.value=round(pygame.mixer.music.get_volume()*100)+1
    output = TextBox(screen, 130, 100, 50, 50, fontSize=30)
    textset = smallfont.render('volume' , True , (0,0,0))
    settingsp=Button(0, 0, 50, 200, red, 0, 7, "Settings", white, screen, pygame.font.Font('freesansbold.ttf', 30))
    output.disable()
    while run:
    #teeb valmis kaartid kuvamiseks
        if ettevalmistus==1 and rounds==0:
            panus=5 
            raha=0
            imp=[]
            impsina=[]
            impvaenlane=[]
            for i in range(2): 
                sinukaartid.append(kaardipakk.kaardigen(sinukaartid))
                vaenlasekaartid.append(kaardipakk.kaardigen(vaenlasekaartid))
            for l in range(2):
                impsina.append(pygame.transform.scale(pygame.image.load("Project-Draco-Hesperidum\\PNGkaartid\\"+kaardipakk.kaartidimg(sinukaartid[l])).convert(), (125, 181)))
                impvaenlane.append(pygame.transform.scale(pygame.image.load("Project-Draco-Hesperidum\\PNGkaartid\\"+kaardipakk.kaartidimg(vaenlasekaartid[l])).convert(), (125, 181)))
            ettevalmistus=0
        if ettevalmistus==1 and rounds==1:
            panus=0
            for i in range(3):         
                kaartid.append(kaardipakk.kaardigen(kaartid))
            for l in range(3):
                imp.append(pygame.transform.scale(pygame.image.load("Project-Draco-Hesperidum\\PNGkaartid\\"+kaardipakk.kaartidimg(kaartid[l])).convert(), (125, 181)))
            ettevalmistus=0
        if ettevalmistus==1 and rounds==2:  
            panus=0     
            kaartid.append(kaardipakk.kaardigen(kaartid))
            imp.append(pygame.transform.scale(pygame.image.load("Project-Draco-Hesperidum\\PNGkaartid\\"+kaardipakk.kaartidimg(kaartid[-1])).convert(), (125, 181)))
            ettevalmistus=0
        if ettevalmistus==1 and rounds==3: 
            panus=5     
            kaartid.append(kaardipakk.kaardigen(kaartid))
            imp.append(pygame.transform.scale(pygame.image.load("Project-Draco-Hesperidum\\PNGkaartid\\"+kaardipakk.kaartidimg(kaartid[-1])).convert(), (125, 181)))
            ettevalmistus=0
        if rounds==4:
            rounds=6
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
            screen.blit(al, (algus, 470))
            algus+=125
        algus=50
        #paneb teksti ekraanile
        Tekst.drawRect()
        sinurahab.drawRect()
        vaenlaserahab.drawRect()
        sinupanus.drawRect()
        rahab.drawRect()
        #muudab teksti
        sinupanus.text="sinu panus: " +str(sinupanraha)
        sinurahab.text="sinu raha: "+str(sinuraha)
        vaenlaserahab.text="vaenlase raha: "+str(vaenlaseraha)
        Tekst.text="panus: "+str(panus)
        rahab.text="hunnik: "+str(raha)
        #paneb nuppu ekraanile
        foldpu=fold.drawRect()
        raisepu=raisep.drawRect()
        callpu=call.drawRect()
        settingspu=settingsp.drawRect()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            #tuvastab nuppule vajutusi
            if tekstväärtus and Button.tee(event, uusroundpu):
                    rounds=0
                    tekstväärtus=False

            if Button.tee(event, callpu) and rounds!=6:
                    if vaenlasekäik==False:
                        raha+=(panus-sinupanraha)
                        sinuraha-=(panus-sinupanraha)
                        sinupanraha+=panus
                        vaenlasekäik=True
                        if vaenlaseraise:
                            rounds+=1
                            ettevalmistus=1
                            sinupanraha=0
                            vaenpanraha=0
                            vaenlasekäik=False
                            vaenlaseraise=False
            if Button.tee(event, foldpu) and rounds!=6:
                    rounds=6
                    vaenlaseraha+=raha
                    tekstväärtus=True
                    võitja.text="vaenlane võitis"
            if Button.tee(event, raisepu) and rounds!=6:
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
            if Button.tee(event, settingspu):
                if settings==True:
                    settings=False
                else:
                    settings=True
        if settings:
            pygame.draw.rect(screen,(255,255,100),[0,100,200,200])
            screen.blit(textset , (10,110))
            output.setText(slider.getValue())
            pygame.mixer.music.set_volume(slider.getValue()/100)
            pygame_widgets.update(event)
        if vaenlasekäik:
            tegu=vaenlane(pokerhand(vaenlasekaartid+kaartid), rounds,  sinuraha, vaenlaseraha, panus)
            if isinstance(tegu, int):
                panus=tegu
                raha+=(panus-vaenpanraha)
                vaenlaseraha-=(panus-vaenpanraha)
                vaenlasekäik=False
                vaenlaseraise=True
                vaenlasebet.text="vaenlane raiseis "+str(panus-vaenpanraha)
                timer=3*clock.get_fps()
                vaenpanraha=panus
            elif tegu=="call":
                raha+=(panus-vaenpanraha)
                vaenlaseraha-=(panus-vaenpanraha)
                vaenpanraha=0
                sinupanraha=0
                rounds+=1
                ettevalmistus=1
                vaenlasekäik=False
                vaenlasebet.text="vaenlane callis"
                timer=5*clock.get_fps()
            else:
                vaenlasekäik=False
                rounds=6
                tekstväärtus=True
                võitja.text="sa võitsid"
                sinuraha+=raha
                vaenlasebet.text="vaenlane foldis"
                timer=2.5*clock.get_fps()
        if tekstväärtus:
            uusroundpu=uusround.drawRect()
            võitja.drawRect()
            algus=50
            for ef in impvaenlane:
                screen.blit(ef, (algus, 250))
                algus+=125
            raha=0
            ettevalmistus=1
            kaartid=[]
            sinukaartid=[]
            vaenlasekaartid=[]
            vaenpanraha=0
            sinupanraha=0
            vaenlaseraise=False
            algus=50
        if timer>0:
            timer-=1
            if rounds !=6 or vaenlasebet.text=="vaenlane foldis":
                vaenlasebet.drawRect()
            else:
                timer=0
        #uuendab ekraani
        pygame.display.update()
        clock.tick(60)
    pygame.quit()