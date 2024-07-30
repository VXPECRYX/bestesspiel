from sys import float_repr_style
import pygame
from pygame.draw import rect
from shared import *
import math


class Taste():
    tastenliste = []
    mausgedrueckt = False   

    def __init__(self,screen,x,y,key):
        self.x = x
        self.y = y
        self.key = key
        Taste.tastenliste.append(self)
        self.size = 40
        self.rect = pygame.Rect(x,y,self.size,self.size)
        self.screen = screen
        self.ausgewählt = False
        self.istsichtbar = True
        self.callback = None



    def zeichnen(self):
        if self.istsichtbar:
            pygame.draw.rect(self.screen,(250,250,250) if self.ausgewählt else (0,0,0),self.rect,3) 
            taste = font.render(self.getKey(), 1, (255, 255, 255))
            self.screen.blit(taste, (self.x+self.size/2-taste.get_rect().width/2, self.y+self.size/2-taste.get_rect().height/2))

    def setzesichtbar(self,istsichtbar):
        self.istsichtbar = istsichtbar

    def onchange(self,callback):
        self.callback = callback


    def getKey(self):
        return self.key

    def click(self):
        x,y = pygame.mouse.get_pos()
        self.ausgewählt = self.rect.collidepoint(x,y)

    def istAusgewählt(self):
        return self.ausgewählt 

    def setKey(self,key):
        if len(key)<=3:
            self.key = key.upper()
