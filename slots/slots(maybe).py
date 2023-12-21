import pygame
import sys
import random

WIDTH, HEIGHT = 800, 600
SLOT_WIDTH, SLOT_HEIGHT = 200, 150
SLOT_MARGIN = 20
FONT_SIZE = 36
REEL_SYMBOLS = ['kirsid', 'õnn', 'Täringud']

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slot Machine")

symbol_images = {symbol: pygame.image.load(f'{symbol}.jpg') for symbol in REEL_SYMBOLS}

background_image = pygame.image.load('pokkermenubr.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

font = pygame.font.Font(None, FONT_SIZE)

class Slot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((SLOT_WIDTH, SLOT_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.symbols = [random.choice(REEL_SYMBOLS) for _ in range(3)]
    def spin(self):
        self.symbols = [random.choice(REEL_SYMBOLS) for _ in range(3)]

slots = [Slot(x, HEIGHT // 2 - SLOT_HEIGHT // 2) for x in range(WIDTH // 2 - SLOT_WIDTH - SLOT_MARGIN,
                                                                  WIDTH // 2 + SLOT_MARGIN,
                                                                  SLOT_WIDTH + SLOT_MARGIN)]

clock = pygame.time.Clock()
running = True
spinning = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not spinning:
                spinning = True

    if spinning:
        for slot in slots:
            slot.spin()

        if all(slot.symbols[0] == slot.symbols[1] == slot.symbols[2] for slot in slots):
            print("Võitsid!")

        spinning = False

    screen.blit(background_image, (0, 0))

    for slot in slots:
        for i, symbol in enumerate(slot.symbols):
            symbol_image = symbol_images[symbol]
            screen.blit(symbol_image, (slot.rect.x + i * SLOT_WIDTH, slot.rect.y))

    pygame.display.flip()
    clock.tick(10)