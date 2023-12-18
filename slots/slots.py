import pygame
import sys
from options import result
import random
class ruut:
    def __init__(self,  x, y, width, height, varv, tekst, font, pilt, screen):
         self.x = x
         self.y = y
         self.width = width
         self.height = height
         self.varv = varv
         self.tekst = tekst
         self.font = font
         self.pilt = pilt
         self.height = height
         self.screen = screen
    def drawRect(self,):
        self.screen.blit(self.pilt, (self.x, self.y))
def slots(screen):
    pygame.init()
    red = (255,67,89)
    white = (255,255,255)
    nimed=("a", "b", "c", "g", "f", "v", "w", "h", "z")
    kohadx=(400, 540, 680)
    kohady=(60, 200, 340, 480)
    ruudud1=[]
    ruudud2=[]
    ruudud3=[]
    kiirus=0
    vajutus=False

    smallfont = pygame.font.SysFont('Corbel',60)
    text = smallfont.render('MENU' , True , white)  
    pilt1=(pygame.transform.scale(pygame.image.load("Project-Draco-Hesperidum\kirsid.jpg").convert(), (110, 120)))
    pilt2= (pygame.transform.scale(pygame.image.load("Project-Draco-Hesperidum\Täringud.jpg").convert(), (110, 120)))
    pilt3=(pygame.transform.scale(pygame.image.load("Project-Draco-Hesperidum\õnn.jpg").convert(), (110, 120)))
    pilt4=(pygame.transform.scale(pygame.image.load("Project-Draco-Hesperidum\õnn.jpg").convert(), (110, 120)))
    pildid=[pilt1, pilt2, pilt3, pilt4]
    for i in range(4):
        ruudud1.append(ruut(kohadx[0], kohady[i],120, 110, white, nimed[i], pygame.font.Font('freesansbold.ttf', 40),pildid[i] , screen))
        ruudud2.append(ruut(kohadx[1], kohady[i],120, 110, white, nimed[i], pygame.font.Font('freesansbold.ttf', 40),pildid[i], screen))
        ruudud3.append(ruut(kohadx[2], kohady[i],120, 110, white, nimed[i], pygame.font.Font('freesansbold.ttf', 40), pildid[i], screen))

    while True:
        mouse = pygame.mouse.get_pos()  
        for ev in pygame.event.get():  
            if ev.type == pygame.QUIT: 
                    pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:  
                if 100 <= mouse[0] <= 200 and 400 <= mouse[1] <= +460: 
                        kiirus=2
                        vajutus=True
                if 0 <= mouse[0]<= 200 and 0 <= mouse[1] <= 100: 
                    return("menu")
        screen.fill(red)
        pygame.draw.rect(screen,(0,0,0),[0,0,200,100],0,0)
        pygame.draw.rect(screen,(0,0,0),[400,200,400,400], 0, 0)
        screen.blit(text, (0,0))
        for el in ruudud1: 
            el.drawRect()
        for el in ruudud2: 
            el.drawRect()
        for el in ruudud3: 
            el.drawRect()
        for el in ruudud1:
            if el.y>600:
                el.y=50
            else:
                el.y+=0.5*kiirus
        for el in ruudud2:
            if el.y>600:
                el.y=50
            else:
                el.y+=0.7*kiirus
        for el in ruudud3:
            if el.y>600:
                el.y=50
            else:
             el.y+=0.8*kiirus
        if kiirus>0:
            kiirus-=0.0001*random.randint(1,5)
        if vajutus and kiirus<0.01:
            for el in ruudud1:
                if 480<=el.y<=600:
                    print(el.tekst)
            for el in ruudud2:
                if 480<=el.y<=600:
                 print(el.tekst)
            for el in ruudud3:
                if 480<=el.y<=600:
                 print(el.tekst)
        vajutus=False

        pygame.draw.rect(screen,red,[400,600,400,600], 0, 0)
        pygame.draw.rect(screen,red,[400,0,400,200], 0, 0)
        pygame.draw.rect(screen,white,[100,400,100,60], 0, 7)
        pygame.display.update()

SCREEN_WIDTH=1100
SCREEN_HEIGHT=700
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
lots(screen)
