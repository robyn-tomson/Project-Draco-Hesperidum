import pygame
#klassid nuppu, teksti ja teksti koos taustaga.
class Button:
    def __init__(self, x, y, height, width, colour, border, curve, text, textColour, screen, font):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour
        self.border = border
        self.curve = curve
        self.text = text
        self.textColour = textColour
        self.screen = screen
        self.font = font

    def drawRect(self):
        button = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.colour, button, self.border, self.curve)
        if self.text != "":
            self.drawText()
        return button
    def tee(event, button):
        if event.type == pygame.MOUSEBUTTONUP:
            if button.collidepoint(event.pos):
                return True
        return False
    def drawText(self):
        text_surf = self.font.render(self.text, True, self.textColour)
        text_rect = text_surf.get_rect(center=(self.x+self.width//2, self.y+self.height//2))
        self.screen.blit(text_surf, text_rect)
class Tekstivali():
    def __init__(self, x, y, height, width, colour, border, curve, text, textColour, screen, font):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour
        self.border = border
        self.curve = curve
        self.text = text
        self.textColour = textColour
        self.font = font
        self.screen=screen
    def drawRect(self):
        button = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.colour, button, self.border, self.curve)
        if self.text != "":
            self.drawText()
    def drawText(self):
        text_surf = self.font.render(self.text, True, self.textColour)
        text_rect = text_surf.get_rect(center=(self.x+self.width//2, self.y+self.height//2))
        self.screen.blit(text_surf, text_rect)
def set_text(string, coordx, coordy, fontSize): #Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    text = font.render(string, True, (0, 0, 250)) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)