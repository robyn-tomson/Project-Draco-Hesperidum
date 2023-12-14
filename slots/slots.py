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
    def drawRect(self):
        button = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.varv, button, 0, 7)
        if self.tekst != "":
            self.drawText()
    def drawText(self):
        text_surf = self.font.render(self.tekst, True, (0,0,0))
        text_rect = text_surf.get_rect(center=(self.x+self.width//2, self.y+self.height//2))
        self.screen.blit(text_surf, text_rect)
         

pygame.init()
SCREEN_WIDTH=1100
SCREEN_HEIGHT=700
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
for i in range(4):
    ruudud1.append(ruut(kohadx[0], kohady[i],120, 110, white, nimed[i], pygame.font.Font('freesansbold.ttf', 40), 0, screen))
    ruudud2.append(ruut(kohadx[1], kohady[i],120, 110, white, nimed[i], pygame.font.Font('freesansbold.ttf', 40), 0, screen))
    ruudud3.append(ruut(kohadx[2], kohady[i],120, 110, white, nimed[i], pygame.font.Font('freesansbold.ttf', 40), 0, screen))
         
while True:
    mouse = pygame.mouse.get_pos()  
    for ev in pygame.event.get():  
            if ev.type == pygame.QUIT: 
                 pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:  
                if 100 <= mouse[0] <= 200 and 400 <= mouse[1] <= +460: 
                     kiirus=2
                     vajutus=True
    screen.fill(red)
    pygame.draw.rect(screen,(0,0,0),[400,200,400,400], 0, 0)
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