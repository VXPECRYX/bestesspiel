import pygame
from welt import Welt
from shared import *


class Boden(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.height = 75
        self.pos = vec((0, self.screen.get_height() - self.height))
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.screen.get_width(), self.height)

    def zeichnen(self):
        self.pos.x = Welt.getPos()
        self.rect.left = self.pos.x
        # Wir malen den Boden in schwarz ein, als Test... wenn du boden.zeichnen() nicht mehr aufrust wird er auch nichtmehr gemalt
        pygame.draw.rect(self.screen, (255,0,0), (0, self.pos.y, self.screen.get_width(), self.height), 1)

    def gethoehe(self):
        return self.height