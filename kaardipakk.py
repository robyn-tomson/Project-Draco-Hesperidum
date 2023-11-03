import random
import pygame
import os
from os import listdir

#tagastab suvalise kaart, mis ei ole veel mängus
def kaardigen(kaartid):
    kaartilist=["2♣","2♦","2♥","2♠","3♣","3♦","3♥","3♠","4♣","4♦","4♥","4♠","5♣","5♦","5♥","5♠",
                "6♣","6♦","6♥","6♠", "7♣","7♦","7♥","7♠","8♣","8♦","8♥","8♠","9♣","9♦","9♥","9♠",
                "10♣","10♦","10♥","10♠", "11♣","11♦","11♥","11♠","12♣","12♦","12♥","12♠",
                "13♣","13♦","13♥","13♠","14♣","14♦","14♥","14♠"]
    while True:
        a=random.choice(kaartilist)
        if a not in kaartid:
            return a
#tagastab kaarti nime PNGkaartid kausta
def kaartidimg(kaart):
    folder_dir = "C:\\Users\\kasutaja\\Projekt\\pokker\\PNGkaartid"
    kaartdic= {}
    for i in range(2, 15):
        for image in os.listdir(folder_dir):
            if str(i) in image:
                if "clubs" in image:
                    kaartdic.update({str(i)+"♣": image})
                if "diamonds" in image:
                    kaartdic.update({str(i)+"♦": image})
                if "hearts" in image:
                    kaartdic.update({str(i)+"♥": image})
                if "spades" in image:
                    kaartdic.update({str(i)+"♠": image})
    return(kaartdic[kaart])