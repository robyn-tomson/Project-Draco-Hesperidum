import pygame
import sys
from menu import menu
from kaotusvõit import kaotusvõit
from pokker1 import pokker1
sys.path.insert(0, 'Project-Draco-Hesperidum\slots') 
from slots import slots

SCREEN_WIDTH=1100
SCREEN_HEIGHT=700
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
koht="menu"
while True:
    
    if koht=="menu":
      koht=menu(screen)
    if koht=="pokker":
      koht=pokker1(screen)
    if koht=="võit":
      koht=kaotusvõit(screen, "võit")
    if koht=="kaotus":
      koht=kaotusvõit(screen, "kaotus")
    if koht=="slots":
      koht=slots(screen)
    try:
      pygame.display.update()
    except:
      break