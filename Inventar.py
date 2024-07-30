import pygame
from shared import *

class Inventar():
    def __init__(self,screen):
        self.screen = screen
        self.hoehe = 60
        self.breite = 183
        self.pos = vec(BREITE-self.breite-20,HOEHE-self.hoehe-8)


    def zeichnen(self):
        self.screen.blit(inventar,self.pos)