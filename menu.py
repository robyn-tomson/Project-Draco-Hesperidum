import pygame  
import sys  
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
  
def menu(screen):
    # initializing the constructor  
    pygame.init()  
  
    # screen resolution   
  
    # opens up a window  
  
    # white color  
    color = (255,255,255)  
    background_image = pygame.image.load('Project-Draco-Hesperidum\pokkermenubr.jpg')
    background_image = pygame.transform.scale(background_image, (1100, 700))
    settings=False
  
    # light shade of the button  
    color_light = (170,170,170)  
  
    # dark shade of the button  
    color_dark = (100,100,100)  
  
    # stores the width of the  
    # screen into a variable  
    width = screen.get_width()  
  
    # stores the height of the  
    # screen into a variable  
    height = screen.get_height()  
  
    # defining a font  
    smallfont = pygame.font.SysFont('Corbel',35)  
  
    # rendering a text written in  
    # this font  
    text = smallfont.render('quit' , True , color)  
    text2 = smallfont.render('start' , True , color)
    text3 = smallfont.render('settings' , True , color)

    slider = Slider(screen, 40, 60, 100, 20, min=0, max=99, step=1)
    slider.value=round(pygame.mixer.music.get_volume()*100)+1
    output = TextBox(screen, 130, 0, 50, 50, fontSize=30)
    textset = smallfont.render('volume' , True , (0,0,0))

    output.disable()

    pygame.mixer.music.load("Project-Draco-Hesperidum\\muusika\\menu.mp3")#music file 
    pygame.mixer.music.play(-1)
  
    while True:  
      
        for ev in pygame.event.get():  
          
            if ev.type == pygame.QUIT:  
                pygame.quit()  
              
            #checks if a mouse is clicked  
            if ev.type == pygame.MOUSEBUTTONDOWN:  
                
            #if the mouse is clicked on the  
            # button the game is terminated  
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
                    pygame.quit()
                if width/2 <= mouse[0] <= width/2+140 and height/3 <= mouse[1] <= height/3+40:  
                    pygame_widgets.WidgetHandler.removeWidget(slider)
                    pygame_widgets.WidgetHandler.removeWidget(output)
                    pygame.mixer.music.stop()
                    return "pokker"
                if width/2 <= mouse[0] <= width/2+140 and height/2.4 <= mouse[1] <= height/2.4+40: 
                    if settings==True:
                        settings=False
                    else:
                        settings=True 

    # fills the screen with a color  
        screen.blit(background_image, (0, 0))  
      
    # stores the (x,y) coordinates into  
    # the variable as a tuple  
        mouse = pygame.mouse.get_pos()  
      
    # if mouse is hovered on a button it  
    # changes to lighter shade  
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
            pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])  
          
        else:  
            pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])

        if width/2 <= mouse[0] <= width/2+140 and height/3 <= mouse[1] <= height/3+40:  
            pygame.draw.rect(screen,color_light,[width/2,height/3,140,40])  
          
        else:  
            pygame.draw.rect(screen,color_dark,[width/2,height/3,140,40])

        if width/2 <= mouse[0] <= width/2+140 and height/2.4 <= mouse[1] <= height/2.4+40:  
            pygame.draw.rect(screen,color_light,[width/2,height/2.4,140,40])  
          
        else:  
            pygame.draw.rect(screen,color_dark,[width/2,height/2.4,140,40])
      
    # superimposing the text onto our button  
        screen.blit(text , (width/2+30,height/2)) 
        screen.blit(text2 , (width/2+30,height/3))
        screen.blit(text3 , (width/2+30,height/2.4))  
        if settings:
            pygame.draw.rect(screen,(255,255,100),[0,0,200,200])
            screen.blit(textset , (10,10))
            output.setText(slider.getValue())
            pygame.mixer.music.set_volume(slider.getValue()/100)
            pygame_widgets.update(ev)
    # updates the frames of the game  
        pygame.display.update()  